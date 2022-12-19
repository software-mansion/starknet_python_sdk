from collections import OrderedDict
from dataclasses import dataclass, InitVar, field
from typing import Dict, Generator

from starknet_py.cairo.serialization._context import (
    SerializationContext,
    DeserializationContext,
)
from starknet_py.cairo.serialization.data_serializers._common import (
    deserialize_to_dict,
    serialize_from_dict_by_key,
    serialize_from_dict,
)
from starknet_py.cairo.serialization.data_serializers.array_serializer import (
    ArraySerializer,
)
from starknet_py.cairo.serialization.data_serializers.cairo_data_serializer import (
    CairoDataSerializer,
)
from starknet_py.cairo.serialization.data_serializers.felt_serializer import (
    FeltSerializer,
)

from starknet_py.cairo.serialization.serialized_payload import SerializedPayload

from starknet_py.utils.tuple_dataclass import TupleDataclass

SIZE_SUFFIX = "_len"
SIZE_SUFFIX_LEN = len(SIZE_SUFFIX)


@dataclass
class PayloadSerializer(CairoDataSerializer[Dict, TupleDataclass]):
    """
    Serializer for payloads like function arguments/function outputs/events.
    Can serialize a dictionary.
    Deserializes data to a TupleDataclass.
    """

    # Value present only in constructor.
    # We don't want to mutate the serializers received in constructor.
    input_serializers: InitVar[OrderedDict[str, CairoDataSerializer]]

    serializers: OrderedDict[str, CairoDataSerializer] = field(init=False)

    def __post_init__(self, input_serializers):
        """
        ABI adds ARG_len for every argument ARG that is an array. We parse length as a part of ArraySerializer, so we
        need to remove those lengths from args.
        """
        self.serializers = OrderedDict(
            (key, serializer)
            for key, serializer in input_serializers.items()
            if not self._is_len_arg(key, input_serializers)
        )

    # This is added because PreparedFunctionCall has a dict with every member serialized.
    def serialize_members(self, members: Dict) -> SerializedPayload:
        """
        Method accepting members as a dictionary and serializing them separately.

        :return: Members serialized separately in SerializedPayload.
        """
        with SerializationContext.create() as context:
            return SerializedPayload(
                (name, list(values))
                for name, values in serialize_from_dict_by_key(
                    self.serializers, context, members
                )
            )

    def deserialize_with_context(
        self, context: DeserializationContext
    ) -> TupleDataclass:
        as_dictionary = deserialize_to_dict(self.serializers, context)
        return TupleDataclass.from_dict(as_dictionary)

    def serialize_with_context(
        self, context: SerializationContext, value: Dict
    ) -> Generator[int, None, None]:
        yield from serialize_from_dict(self.serializers, context, value)

    @staticmethod
    def _is_len_arg(arg_name: str, serializers: Dict[str, CairoDataSerializer]) -> bool:
        return (
            arg_name.endswith(SIZE_SUFFIX)
            and isinstance(serializers[arg_name], FeltSerializer)
            # There is an ArraySerializer under key that is arg_name without the size suffix
            and isinstance(
                serializers.get(arg_name[:-SIZE_SUFFIX_LEN]), ArraySerializer
            )
        )
