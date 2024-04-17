"""Utility functions for testing evaluation code."""

from pyspark.sql import types as T


def _are_data_types_equal(type1: T.DataType, type2: T.DataType) -> bool:
    """Compares two data types, ignoring nullability."""
    if type(type1) != type(type2):
        return False

    if isinstance(type1, T.StructType):
        return schemas_equal(type1, type2)
    elif isinstance(type1, T.ArrayType):
        return _are_data_types_equal(type1.elementType, type2.elementType)
    elif isinstance(type1, T.MapType):
        return _are_data_types_equal(
            type1.keyType, type2.keyType
        ) and _are_data_types_equal(type1.valueType, type2.valueType)
    else:
        return type1 == type2


def schemas_equal(schema1: T.StructType, schema2: T.StructType) -> bool:
    """Compares two schemas, ignoring nullability of fields."""
    if len(schema1.fields) != len(schema2.fields):
        return False

    for field1, field2 in zip(schema1.fields, schema2.fields):
        if field1.name != field2.name or not _are_data_types_equal(
            field1.dataType, field2.dataType
        ):
            return False

    return True
