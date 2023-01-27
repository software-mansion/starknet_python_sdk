import warnings
from typing import List, Literal, Optional, Union, cast

from starknet_py.compile.compiler import Compiler, StarknetCompilationSource
from starknet_py.net.client_models import CompiledContract, ContractClass
from starknet_py.net.schemas.gateway import CompiledContractSchema, ContractClassSchema


def create_compiled_contract(
    compilation_source: Optional[StarknetCompilationSource] = None,
    compiled_contract: Optional[str] = None,
    search_paths: Optional[List[str]] = None,
) -> ContractClass:
    warnings.warn(
        "Function create_compiled_contract is deprecated and will be removed in the future. "
        "Consider using create_contract_class instead.",
        category=DeprecationWarning,
    )

    if not compiled_contract:
        if not compilation_source:
            raise ValueError(
                "One of compiled_contract or compilation_source is required."
            )

        compiled_contract = Compiler(
            contract_source=compilation_source, cairo_path=search_paths
        ).compile_contract()
    definition = create_contract_class(compiled_contract)
    return definition


def _create_compiled_contract(compiled_contract: str) -> CompiledContract:
    """
    Creates CompiledContract from already compiled contract.

    :return: a CompiledContract instance.
    """
    return cast(CompiledContract, CompiledContractSchema().loads(compiled_contract))


def create_contract_class(
    compiled_contract: str,
) -> ContractClass:
    """
    Creates ContractClass from already compiled contract.

    :return: a ContractClass.
    """
    return cast(ContractClass, ContractClassSchema().loads(compiled_contract))


def int_from_hex(number: Union[str, int]) -> int:
    return number if isinstance(number, int) else int(number, 16)


def int_from_bytes(
    value: bytes,
    byte_order: Literal["big", "little"] = "big",
    signed: bool = False,
) -> int:
    """
    Converts the given bytes object (parsed according to the given byte order) to an integer.
    """
    return int.from_bytes(value, byteorder=byte_order, signed=signed)
