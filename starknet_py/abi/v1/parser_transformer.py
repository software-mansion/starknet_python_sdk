import os
from typing import Any, List, Optional

import lark
from lark import Token, Transformer

from starknet_py.cairo.data_types import (
    ArrayType,
    BoolType,
    CairoType,
    FeltType,
    OptionType,
    TupleType,
    TypeIdentifier,
    UintType,
    UnitType,
)


class ParserTransformer(Transformer):
    """
    Transforms the lark tree into CairoTypes.
    """

    # pylint: disable=no-self-use

    def __default__(self, data: str, children, meta):
        raise TypeError(f"Unable to parse tree node of type {data}.")

    def type(self, value: List[Optional[CairoType]]) -> Optional[CairoType]:
        """
        Tokens are read bottom-up, so here all of them are parsed and should be just returned.
        `Optional` is added in case of the unit type.
        """
        assert len(value) == 1
        return value[0]

    def type_felt(self, _value: List[Any]) -> FeltType:
        """
        Felt does not contain any additional arguments, so `_value` is just an empty list.
        """
        return FeltType()

    def type_bool(self, _value: List[Any]) -> BoolType:
        """
        Bool does not contain any additional arguments, so `_value` is just an empty list.
        """
        return BoolType()

    def type_uint(self, value: List[Token]) -> UintType:
        """
        Uint type contains information about its size. It is present in the value[0].
        """
        return UintType(int(value[0]))

    def type_unit(self, _value: List[Any]) -> UnitType:
        """
        `()` type.
        """
        return UnitType()

    def type_option(self, value: List[CairoType]) -> OptionType:
        """
        Option includes an information about which type it eventually represents.
        `Optional` is added in case of the unit type.
        """
        return OptionType(value[0])

    def type_array(self, value: List[CairoType]) -> ArrayType:
        """
        Array contains values of type under `value[0]`.
        """
        return ArrayType(value[0])

    def type_span(self, value: List[CairoType]) -> ArrayType:
        """
        Span contains values of type under `value[0]`.
        """
        return ArrayType(value[0])

    def type_identifier(self, tokens: List[Token]) -> TypeIdentifier:
        """
        Structs and enums are defined as follows: (IDENTIFIER | "::")+ [some not important info]
        where IDENTIFIER is a string.

        Tokens would contain strings and types (if it is present).
        We are interested only in the strings because a structure (or enum) name can be built from them.
        """
        name = "::".join(token for token in tokens if isinstance(token, str))
        return TypeIdentifier(name)

    def type_contract_address(self, _value: List[Any]) -> FeltType:
        """
        ContractAddress is represented by the felt252.
        """
        return FeltType()

    def type_class_hash(self, _value: List[Any]) -> FeltType:
        """
        ClassHash is represented by the felt252.
        """
        return FeltType()

    def type_storage_address(self, _value: List[Any]) -> FeltType:
        """
        StorageAddress is represented by the felt252.
        """
        return FeltType()

    def tuple(self, types: List[CairoType]) -> TupleType:
        """
        Tuple contains values defined in the `types` argument.
        """
        return TupleType(types)


def parse(
    code: str,
) -> CairoType:
    """
    Parse the given string and return a CairoType.
    """
    with open(
        os.path.join(os.path.dirname(__file__), "abi.ebnf"), "r", encoding="utf-8"
    ) as grammar_file:
        grammar = grammar_file.read()

    grammar_parser = lark.Lark(
        grammar=grammar,
        start="type",
        parser="earley",
    )
    parsed = grammar_parser.parse(code)

    transformed = ParserTransformer().transform(parsed)

    return transformed
