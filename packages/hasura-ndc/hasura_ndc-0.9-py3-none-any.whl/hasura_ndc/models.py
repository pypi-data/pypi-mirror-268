from __future__ import annotations
from typing import Union, List, Dict, Optional, Literal, Any
from pydantic import BaseModel, model_validator


class RootModel(BaseModel):

    def dict(self, **kwargs):
        return super().model_dump(**kwargs, exclude_none=True)


class Type(RootModel):
    type: Literal["named", "nullable", "array", "predicate"]
    name: Optional[str] = None
    underlying_type: Optional['Type'] = None
    element_type: Optional['Type'] = None
    object_type_name: Optional[str] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     name = data.get('name')
    #     underlying_type = data.get('underlying_type')
    #     element_type = data.get('element_type')
    #     object_type_name = data.get('object_type_name')
    #
    #     if type_t == 'named':
    #         if not name:
    #             raise ValueError("name is required when type is 'named'")
    #         if any([underlying_type, element_type, object_type_name]):
    #             raise ValueError("Only 'name' should be set when type is 'named'")
    #     elif type_t == 'nullable':
    #         if not underlying_type:
    #             raise ValueError("underlying_type is required when type is 'nullable'")
    #         if any([name, element_type, object_type_name]):
    #             raise ValueError("Only 'underlying_type' should be set when type is 'nullable'")
    #     elif type_t == 'array':
    #         if not element_type:
    #             raise ValueError("element_type is required when type is 'array'")
    #         if any([name, underlying_type, object_type_name]):
    #             raise ValueError("Only 'element_type' should be set when type is 'array'")
    #     elif type_t == 'predicate':
    #         if not object_type_name:
    #             raise ValueError("object_type_name is required when type is 'predicate'")
    #         if any([name, underlying_type, element_type]):
    #             raise ValueError("Only 'object_type_name' should be set when type is 'predicate'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class Aggregate(RootModel):
    type: Literal["column_count", "single_column", "star_count"]
    column: Optional[str] = None
    distinct: Optional[bool] = None
    function: Optional[str] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     column = data.get('column')
    #     distinct = data.get('distinct')
    #     function = data.get('function')
    #
    #     if type_t == 'column_count':
    #         if not column:
    #             raise ValueError("column is required when type is 'column_count'")
    #         if distinct is None:
    #             raise ValueError("distinct is required when type is 'column_count'")
    #         if function is not None:
    #             raise ValueError("Only 'column' and 'distinct' should be set when type is 'column_count'")
    #     elif type_t == 'single_column':
    #         if not column:
    #             raise ValueError("column is required when type is 'single_column'")
    #         if function is None:
    #             raise ValueError("function is required when type is 'single_column'")
    #         if distinct is not None:
    #             raise ValueError("Only 'column' and 'function' should be set when type is 'single_column'")
    #     elif type_t == 'star_count':
    #         if column is not None:
    #             raise ValueError("'star_count' does not have any arguments")
    #         if distinct is not None:
    #             raise ValueError("'star_count' does not have any arguments")
    #         if function is not None:
    #             raise ValueError("'star_count' does not have any arguments")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class Argument(RootModel):
    type: Literal["variable", "literal"]
    name: Optional[str] = None
    value: Optional[Any] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     name = data.get('name')
    #     value = data.get('value')
    #
    #     if type_t == "variable":
    #         if not name:
    #             raise ValueError("name is required when type is 'variable'")
    #         if value is not None:
    #             raise ValueError("Only 'name' should be set when type is 'variable'")
    #     elif type_t == "literal":
    #         if name is not None:
    #             raise ValueError("Only 'value' should be set when type is 'literal'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class ComparisonTarget(RootModel):
    type: Literal["column", "root_collection_column"]
    name: str
    path: Optional['PathElement'] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     path = data.get("path")
    #
    #     if type_t == "column":
    #         if path is None:
    #             raise ValueError("path is required when type is 'column'")
    #     elif type_t == "root_collection_column":
    #         if path is not None:
    #             raise ValueError("Only 'name' should be set when type is 'root_collection_column'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class ComparisonValue(RootModel):
    type: Literal["column", "scalar", "variable"]
    column: Optional['ComparisonTarget'] = None
    value: Optional[Any] = None
    name: Optional[str] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     column = data.get("column")
    #     value = data.get("value")
    #     name = data.get("name")
    #
    #     if type_t == "column":
    #         if column is None:
    #             raise ValueError("column is required when type is 'column'")
    #         if value is not None:
    #             raise ValueError("Only 'column' should be set when type is 'column'")
    #         if name is not None:
    #             raise ValueError("Only 'column' should be set when type is 'column'")
    #     elif type_t == "scalar":
    #         if column is not None:
    #             raise ValueError("Only 'value' should be set when type is 'scalar'")
    #         if name is not None:
    #             raise ValueError("Only 'value' should be set when type is 'scalar'")
    #     elif type_t == "variable":
    #         if column is not None:
    #             raise ValueError("Only 'name' should be set when type is 'variable'")
    #         if value is not None:
    #             raise ValueError("Only 'name' should be set when type is 'variable'")
    #         if name is None:
    #             raise ValueError("name is required when type is 'variable'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


UnaryComparisonOperator = "is_null"


class Expression(RootModel):
    type: Literal["and", "or", "not", "unary_comparison_operator", "binary_comparison_operator", "exists"]
    expressions: Optional[List['Expression']] = None
    expression: Optional['Expression'] = None
    column: Optional['ComparisonTarget'] = None
    operator: Optional[str] = None
    value: Optional['ComparisonValue'] = None
    in_collection: Optional['ExistsInCollection'] = None
    predicate: Optional['Expression'] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     expressions = data.get("expressions")
    #     expression = data.get("expression")
    #     column = data.get("column")
    #     operator = data.get("operator")
    #     value = data.get("value")
    #     in_collection = data.get("in_collection")
    #     predicate = data.get("predicate")
    #
    #     if type_t == "and":
    #         if expressions is None:
    #             raise ValueError("expressions is required when type is 'and'")
    #         elif any([expression, column, operator, value, in_collection, predicate]):
    #             raise ValueError("Only 'expressions' should be set when type is 'and'")
    #     elif type_t == "or":
    #         if expressions is None:
    #             raise ValueError("expressions is required when type is 'or'")
    #         elif any([expression, column, operator, value, in_collection, predicate]):
    #             raise ValueError("Only 'expressions' should be set when type is 'or'")
    #     elif type_t == "not":
    #         if expression is None:
    #             raise ValueError("expression is required when type is 'not'")
    #         elif any([expressions, column, operator, value, in_collection, predicate]):
    #             raise ValueError("Only 'expression' should be set when type is 'not'")
    #     elif type_t == "unary_comparison_operator":
    #         if column is None:
    #             raise ValueError("column is required when type is 'unary_comparison_operator'")
    #         if operator != UnaryComparisonOperator:
    #             raise ValueError(f"operator must be {UnaryComparisonOperator} when type is 'unary_comparison_operator'")
    #         if any([expressions, expression, value, in_collection, predicate]):
    #             raise ValueError("Only 'column' and 'operator' should be set when type is 'unary_comparison_operator'")
    #     elif type_t == "binary_comparison_operator":
    #         if column is None:
    #             raise ValueError("column is required when type is 'binary_comparison_operator'")
    #         if operator is None:
    #             raise ValueError("operator is required when type is 'binary_comparison_operator'")
    #         if value is None:
    #             raise ValueError("value is required when type is 'binary_comparison_operator'")
    #         if any([expressions, expression, in_collection, predicate]):
    #             raise ValueError(
    #                 "Only 'column' and 'operator' and 'value' should be set when type is 'binary_comparison_operator'")
    #     elif type_t == "exists":
    #         if in_collection is None:
    #             raise ValueError("in_collection is required when type is 'exists'")
    #         if any([expressions, expression, column, operator, value]):
    #             raise ValueError("Only 'in_collection' and 'predicate' should be set when type is 'exists'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class PathElement(RootModel):
    relationship: str
    arguments: Dict[str, 'RelationshipArgument']
    predicate: Optional['Expression'] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     relationship = data.get("relationship")
    #     arguments = data.get("arguments")
    #
    #     if not relationship:
    #         raise ValueError("relationship is required")
    #     if not arguments:
    #         raise ValueError("arguments must not be empty")
    #     return data


OrderDirection = Literal["asc", "desc"]


class OrderByTarget(RootModel):
    type: Literal["column", "single_column_aggregate", "star_count_aggregate"]
    name: Optional[str]
    column: Optional[str]
    function: Optional[str]
    path: List['PathElement']

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     name = data.get('name')
    #     column = data.get('column')
    #     function = data.get('function')
    #
    #     if type_t == 'column':
    #         if not name:
    #             raise ValueError("name is required when type is 'column'")
    #         if any([column, function]):
    #             raise ValueError("Only 'name' and 'path' should be set when type is 'column'")
    #     elif type_t == 'single_column_aggregate':
    #         if not column or not function:
    #             raise ValueError("both 'column' and 'function' are required when type is 'single_column_aggregate'")
    #         if name is not None:
    #             raise ValueError(
    #                 "Only 'column', 'function', and 'path' should be set when type is 'single_column_aggregate'")
    #     elif type_t == 'star_count_aggregate':
    #         if any([name, column, function]):
    #             raise ValueError("Only 'path' should be set when type is 'star_count_aggregate'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class OrderBy(RootModel):
    elements: List['OrderByElement']


class OrderByElement(RootModel):
    order_direction: 'OrderDirection'
    target: 'OrderByTarget'


class Query(RootModel):
    aggregates: Optional[Dict[str, 'Aggregate']] = None
    fields: Optional[Dict[str, 'Field']] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    order_by: Optional['OrderBy'] = None
    predicate: Optional['Expression'] = None


class RelationshipArgument(RootModel):
    type: Literal["variable", "literal", "column"]
    name: Optional[str] = None
    value: Optional[Any] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     name = data.get('name')
    #     value = data.get('value')
    #
    #     if type_t == "variable":
    #         if not name:
    #             raise ValueError("name is required when type is 'variable'")
    #         if value is not None:
    #             raise ValueError("value should not be set when type is 'variable'")
    #     elif type_t == "literal":
    #         if name is not None:
    #             raise ValueError("name should not be set when type is 'literal'")
    #     elif type_t == "column":
    #         if not name:
    #             raise ValueError("name is required when type is 'column'")
    #         if value is not None:
    #             raise ValueError("value should not be set when type is 'column'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class NestedField(RootModel):
    type: Literal["object", "array"]
    fields: Union[Dict[str, 'Field'], 'NestedField']

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     fields = data.get("fields")
    #
    #     if type_t == "object":
    #         if not isinstance(fields, dict):
    #             raise ValueError("fields must be a dictionary when type is 'object'")
    #     elif type_t == "array":
    #         if not isinstance(fields, NestedField):
    #             raise ValueError("fields must be a NestedField instance when type is 'array'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class Field(RootModel):
    type: Literal["column", "relationship"]
    column: Optional[str] = None
    fields: Optional['NestedField'] = None
    query: Optional['Query'] = None
    relationship: Optional[str] = None
    arguments: Optional[Dict[str, 'RelationshipArgument']] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get('type')
    #     column = data.get('column')
    #     fields = data.get('fields')
    #     query = data.get('query')
    #     relationship = data.get('relationship')
    #     arguments = data.get('arguments')
    #
    #     if type_t == "column":
    #         if not column:
    #             raise ValueError("column is required when type is 'column'")
    #         if any([query, relationship, arguments]):
    #             raise ValueError("Only 'column' and 'fields' should be set when type is 'column'")
    #     elif type_t == "relationship":
    #         if not query or not relationship or not arguments:
    #             raise ValueError("query, relationship, and arguments are required when type is 'relationship'")
    #         if column is not None or fields is not None:
    #             raise ValueError("column and fields should not be set when type is 'relationship'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class ExistsInCollection(RootModel):
    type: Literal["related", "unrelated"]
    relationship: Optional[str] = None
    collection: Optional[str] = None
    arguments: Dict[str, 'RelationshipArgument']

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     relationship = data.get("relationship")
    #     collection = data.get("collection")
    #     arguments = data.get("arguments")
    #
    #     if type_t == "related":
    #         if not relationship:
    #             raise ValueError("relationship is required when type is 'related'")
    #         if collection is not None:
    #             raise ValueError("collection should not be set when type is 'related'")
    #     elif type_t == "unrelated":
    #         if not collection:
    #             raise ValueError("collection is required when type is 'unrelated'")
    #         if relationship is not None:
    #             raise ValueError("relationship should not be set when type is 'unrelated'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #
    #     if not arguments:
    #         raise ValueError("arguments must not be empty")
    #     return data


RelationshipType = Literal["object", "array"]


class RowSet(RootModel):
    aggregates: Optional[Dict[str, Any]] = None
    rows: Optional[List[Dict[str, Any]]] = None


QueryResponse = List[RowSet]


class Relationship(RootModel):
    column_mapping: Dict[str, str]
    relationship_type: 'RelationshipType'
    target_collection: str
    arguments: Dict[str, 'RelationshipArgument']


class MutationOperation(RootModel):
    type: Literal["procedure"]
    name: str
    arguments: Dict[str, Any]
    fields: Optional['NestedField'] = None


class MutationOperationResults(RootModel):
    type: Literal["procedure"]
    result: Any


class CapabilitiesResponse(RootModel):
    version: str
    capabilities: 'Capabilities'


class Capabilities(RootModel):
    query: 'QueryCapabilities'
    mutation: 'MutationCapabilities'
    relationships: Optional['RelationshipCapabilities'] = None


class SchemaRoot(RootModel):
    capabilities_response: CapabilitiesResponse
    schema_response: 'SchemaResponse'
    query_request: 'QueryRequest'
    query_response: 'QueryResponse'
    mutation_request: 'MutationRequest'
    mutation_response: 'MutationResponse'
    explain_response: 'ExplainResponse'
    error_response: 'ErrorResponse'
    validate_response: 'ValidateResponse'


class LeafCapability(RootModel):
    pass


class QueryCapabilities(RootModel):
    aggregates: Optional['LeafCapability'] = None
    variables: Optional['LeafCapability'] = None
    explain: Optional['LeafCapability'] = None


class MutationCapabilities(RootModel):
    transactional: Optional['LeafCapability'] = None
    explain: Optional['LeafCapability'] = None


class RelationshipCapabilities(RootModel):
    relation_comparisons: Optional['LeafCapability'] = None
    order_by_aggregate: Optional['LeafCapability'] = None


class SchemaResponse(RootModel):
    scalar_types: Dict[str, 'ScalarType']
    object_types: Dict[str, 'ObjectType']
    collections: List['CollectionInfo']
    functions: List['FunctionInfo']
    procedures: List['ProcedureInfo']


class TypeRepresentation(RootModel):
    type: Literal[
        "boolean", "string", "number", "integer", "int8", "int16", "int32", "int64", "float32", "float64", "bigdecimal",
        "uuid", "date", "timestamp", "timestamptz", "geography", "geometry", "bytes", "json", "enum"]
    one_of: Optional[List[str]] = None


class ComparisonOperatorDefinition(RootModel):
    type: Literal["equal", "in", "custom"]
    argument_type: Optional['Type'] = None

    # @model_validator(mode="before")
    # def validate_fields(self, data):
    #     type_t = data.get("type")
    #     argument_type = data.get("argument_type")
    #
    #     if type_t == "equal":
    #         if argument_type is not None:
    #             raise ValueError("argument_type should not be set when type is 'equal'")
    #     elif type_t == "in":
    #         if argument_type is not None:
    #             raise ValueError("argument_type should not be set when type is 'equal'")
    #     elif type_t == "custom":
    #         if argument_type is None:
    #             raise ValueError("argument_type should be set when type is 'custom'")
    #     else:
    #         raise ValueError(f"Invalid type value: {type_t}")
    #     return data


class ScalarType(RootModel):
    representation: Optional['TypeRepresentation'] = None
    aggregate_functions: Dict[str, 'AggregateFunctionDefinition']
    comparison_operators: Dict[str, 'ComparisonOperatorDefinition']


class AggregateFunctionDefinition(RootModel):
    result_type: 'Type'


class ObjectType(RootModel):
    description: Optional[str] = None
    fields: Dict[str, 'ObjectField']


class ObjectField(RootModel):
    description: Optional[str] = None
    type: 'Type'


class CollectionInfo(RootModel):
    name: str
    description: Optional[str] = None
    arguments: Dict[str, 'ArgumentInfo']
    type: str
    uniqueness_constraints: Dict[str, 'UniquenessConstraint']
    foreign_keys: Dict[str, 'ForeignKeyConstraint']


class ArgumentInfo(RootModel):
    description: Optional[str] = None
    type: 'Type'


class UniquenessConstraint(RootModel):
    unique_columns: List[str]


class ForeignKeyConstraint(RootModel):
    column_mapping: Dict[str, str]
    foreign_collection: str


class FunctionInfo(RootModel):
    name: str
    description: Optional[str] = None
    arguments: Dict[str, 'ArgumentInfo']
    result_type: 'Type'


class ProcedureInfo(BaseModel):
    name: str
    description: Optional[str] = None
    arguments: Dict[str, 'ArgumentInfo']
    result_type: 'Type'


class QueryRequest(BaseModel):
    collection: str
    query: 'Query'
    arguments: Dict[str, 'Argument']
    collection_relationships: Dict[str, 'Relationship']
    variables: Optional[Dict[str, Any]] = None


class MutationRequest(BaseModel):
    operations: List['MutationOperation']
    collection_relationships: Dict[str, 'Relationship']


class MutationResponse(BaseModel):
    operation_results: List['MutationOperationResults']


class ExplainResponse(BaseModel):
    details: Dict[str, str]


class ErrorResponse(BaseModel):
    message: str
    details: Dict[str, Any]


class ValidateResponse(BaseModel):
    schema: SchemaResponse
    capabilities: CapabilitiesResponse
    resolved_configuration: str
