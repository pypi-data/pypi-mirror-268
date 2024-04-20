from opentelemetry import trace, metrics
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.composite import CompositePropagator
from opentelemetry.propagators.b3 import B3Format
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.baggage.propagation import W3CBaggagePropagator
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import Status, StatusCode

import os

sdk = None

USER_VISIBLE_SPAN_ATTRIBUTE = {
    "internal.visibility": "user",
}


def init_telemetry(default_service_name="hasura-ndc", default_endpoint="http://localhost:4318"):
    global sdk

    if is_initialized():
        raise Exception("Telemetry has already been initialized!")

    service_name = os.environ.get("OTEL_SERVICE_NAME", default_service_name)
    endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", default_endpoint)

    resource = Resource.create(attributes={"service.name": service_name})

    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)

    span_processor = BatchSpanProcessor(
        OTLPSpanExporter(endpoint=f"{endpoint}/v1/traces")
    )
    tracer_provider.add_span_processor(span_processor)

    metric_reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(endpoint=f"{endpoint}/v1/metrics")
    )
    metric_provider = MeterProvider(metric_readers=[metric_reader])
    metrics.set_meter_provider(metric_provider)

    FastAPIInstrumentor().instrument(
        server_request_hook=lambda span, request: span.set_attributes(USER_VISIBLE_SPAN_ATTRIBUTE)
    )
    RequestsInstrumentor().instrument(
        tracer_provider=trace.get_tracer_provider(),
        span_callback=lambda span, request, response: span.set_attributes(USER_VISIBLE_SPAN_ATTRIBUTE),
    )
    LoggingInstrumentor().instrument(
        log_hook=lambda span, record, _: record.update(
            {
                "resource.service.name": service_name,
                "parent_span_id": span.get_span_context().span_id,
            }
        )
    )

    propagators = CompositePropagator(
        [
            TraceContextTextMapPropagator(),
            W3CBaggagePropagator(),
            B3Format(),
        ]
    )
    set_global_textmap(propagators)

    sdk = trace.get_tracer_provider()


def is_initialized():
    return sdk is not None


def with_active_span(tracer, name, func, attributes=None):
    return with_internal_active_span(
        tracer,
        name,
        func,
        {**USER_VISIBLE_SPAN_ATTRIBUTE, **attributes} if attributes else USER_VISIBLE_SPAN_ATTRIBUTE,
    )


def with_internal_active_span(tracer, name, func, attributes=None):
    with tracer.start_as_current_span(name, attributes=attributes) as span:
        def handle_error(exc):
            if isinstance(exc, (Exception, str)):
                span.record_exception(exc)
            span.set_status(Status(StatusCode.ERROR))
            span.end()

        try:
            retval = func(span)
            if hasattr(retval, "__iter__") and hasattr(retval, "__next__"):
                for item in retval:
                    yield item
            else:
                return retval
        except Exception as e:
            handle_error(e)
            raise
        finally:
            span.end()
