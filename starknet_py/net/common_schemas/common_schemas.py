from typing import Any, Union, Mapping

from marshmallow import fields, ValidationError

from starknet_py.net.client_models import (
    TransactionStatus,
    BlockStatus,
    TransactionType,
)

# pylint: disable=unused-argument
# pylint: disable=no-self-use


class Felt(fields.Field):
    # TODO test that serialization and deserialization is correct
    """
    Field that serializes int to felt (hex encoded string)
    """

    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        if value is None:
            return None
        return str(hex(value))

    def _deserialize(
        self,
        value: Any,
        attr: Union[str, None],
        data: Union[Mapping[str, Any], None],
        **kwargs,
    ):
        try:
            assert isinstance(value, str) and value.startswith("0x")
            return int(value, 16)
        except (ValueError, AssertionError) as error:
            raise ValidationError("Invalid felt") from error


class StatusField(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        # TODO should we serialize to string?
        return value.name if value is not None else ""

    def _deserialize(
        self,
        value: Any,
        attr: Union[str, None],
        data: Union[Mapping[str, Any], None],
        **kwargs,
    ) -> TransactionStatus:
        values = [v.value for v in TransactionStatus]

        if value == "NOT_RECEIVED":
            return TransactionStatus.UNKNOWN

        if value not in values:
            raise ValidationError("Invalid TransactionStatus enum key")

        return TransactionStatus(value)


class BlockStatusField(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        # TODO should we serialize to string?
        return value.name if value is not None else ""

    def _deserialize(
        self,
        value: Any,
        attr: Union[str, None],
        data: Union[Mapping[str, Any], None],
        **kwargs,
    ) -> BlockStatus:
        # TODO maybe simplify
        values = [v.value for v in BlockStatus]

        if value not in values:
            raise ValidationError("Invalid BlockStatus enum key")

        return BlockStatus(value)


class TransactionTypeField(fields.Field):
    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        # TODO should we serialize to string?
        return value.name if value is not None else ""

    def _deserialize(
        self,
        value: Any,
        attr: Union[str, None],
        data: Union[Mapping[str, Any], None],
        **kwargs,
    ) -> TransactionType:
        values = [v.value for v in TransactionType]

        if value not in values:
            # TODO should we use different default type?
            return TransactionType.INVOKE

        return TransactionType(value)
