from collections import OrderedDict
from typing import Dict, Iterable, Generator, List, Tuple, Set

from starknet_py.cairo.serialization._context import (
    DeserializationContext,
    SerializationContext,
)
from starknet_py.cairo.serialization.data_serializers.cairo_data_serializer import (
    CairoDataSerializer,
)


# The actual serialization logic is actually very similar among all serializers: they either serialize data based on
# position or their name. Having this logic reused adds indirection, but makes sure proper logic is used everywhere.


def deserialize_to_list(
    deserializers: List[CairoDataSerializer], context: DeserializationContext
) -> List:
    """
    Deserializes data from context to list. This logic is used in every sequential type (arrays and tuples).
    """
    result = []

    for index, serializer in enumerate(deserializers):
        with context.push_entity(f"[{index}]"):
            result.append(serializer.deserialize_with_context(context))

    return result


def deserialize_to_dict(
    deserializers: OrderedDict[str, CairoDataSerializer],
    context: DeserializationContext,
) -> OrderedDict:
    """
    Deserializes data from context to dictionary. This logic is used in every type with named fields (structs,
    named tuples and payloads).
    """
    result = OrderedDict()

    for key, serializer in deserializers.items():
        with context.push_entity(key):
            result[key] = serializer.deserialize_with_context(context)

    return result


def serialize_from_list(
    serializers: List[CairoDataSerializer], context: SerializationContext, values: List
) -> Generator[int, None, None]:
    """
    Serializes data from list. This logic is used in every sequential type (arrays and tuples).
    """
    context.ensure_valid_value(
        len(serializers) == len(values),
        f"expected {len(serializers)} elements, {len(values)} provided",
    )

    for index, (serializer, value) in enumerate(zip(serializers, values)):
        with context.push_entity(f"[{index}]"):
            yield from serializer.serialize_with_context(context, value)


def serialize_from_dict(
    serializers: OrderedDict[str, CairoDataSerializer],
    context: SerializationContext,
    values: Dict,
) -> Generator[int, None, None]:
    """
    Serializes data from dict. This logic is used in every type with named fields (structs, named tuples and payloads).
    """
    for _name, data in serialize_from_dict_by_key(serializers, context, values):
        yield from data


def serialize_from_dict_by_key(
    serializers: OrderedDict[str, CairoDataSerializer],
    context: SerializationContext,
    values: Dict,
) -> Generator[Tuple[str, Iterable[int]], None, None]:
    """
    Serializes data from dict. It emits tuples (name, generator for value). This makes it possible to know serialized
    values for each key.
    """
    excessive_keys = get_excessive_keys(serializers.keys(), values)
    context.ensure_valid_value(
        not excessive_keys,
        f"unexpected keys '{','.join(excessive_keys)}' were provided",
    )

    for name, serializer in serializers.items():
        with context.push_entity(name):
            context.ensure_valid_value(name in values, f"key '{name}' is missing")
            yield name, serializer.serialize_with_context(context, values[name])


def get_excessive_keys(expected: Iterable[str], arguments: Dict) -> Set[str]:
    """
    Returns arguments that were provided, but were not defined in the API.
    """
    return set(arguments.keys()).difference(expected)
