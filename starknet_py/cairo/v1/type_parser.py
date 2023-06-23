from __future__ import annotations

from typing import Dict, Union

from lark import UnexpectedToken

from starknet_py.abi.v1.parser_transformer import parse
from starknet_py.cairo.data_types import (
    ArrayType,
    CairoType,
    EnumType,
    StructType,
    TypeIdentifier,
)


class UnknownCairoTypeError(ValueError):
    """
    Error thrown when TypeParser finds type that was not declared prior to parsing.
    """

    type_name: str

    def __init__(self, type_name: str):
        super().__init__(
            f"""Type '{type_name}' is not defined. 
            Please report this issue at https://github.com/software-mansion/starknet.py/issues"""
        )
        self.type_name = type_name


class TypeParser:
    """
    Low level utility class for parsing Cairo types that can be used in external methods.
    """

    defined_types: Dict[str, Union[StructType, EnumType]]

    def __init__(self, defined_types: Dict[str, Union[StructType, EnumType]]):
        """
        TypeParser constructor.

        :param defined_types: dictionary containing all defined types. For now, they can only be structures.
        """
        self.defined_types = defined_types
        for name, defined_type in defined_types.items():
            if name != defined_type.name:
                raise ValueError(
                    f"Keys must match name of type, '{name}' != '{defined_type.name}'."
                )

    def parse_inline_type(self, type_string: str) -> CairoType:
        """
        Inline type is one that can be used inline, for instance as return type. For instance
        (core::felt252, (), (core::felt252,)). Structure can only be referenced in inline type, can't be defined
        this way.

        :param type_string: type to parse.
        """
        try:
            parsed = parse(type_string)
        except UnexpectedToken as err:
            raise ValueError(
                """Unimplemented type occurred in ABI. 
                Please report this issue at https://github.com/software-mansion/starknet.py/issues"""
            ) from err

        if isinstance(parsed, TypeIdentifier):
            return self._get_struct(parsed)

        # TODO (#1079): add recursive support for iterables with structures (tuples?)
        if isinstance(parsed, ArrayType):
            inner_type_string = type_string[
                type_string.find("<") + 1 : type_string.rfind(">")
            ]
            parsed.inner_type = self.parse_inline_type(inner_type_string)

        return parsed

    def _get_struct(self, identifier: TypeIdentifier):
        for struct_name in self.defined_types.keys():
            if identifier.name == struct_name.split("<")[0].strip(":"):
                return self.defined_types[struct_name]
        raise UnknownCairoTypeError(identifier.name)
