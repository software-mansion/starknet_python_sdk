from typing import Optional, List

from starkware.starknet.services.api.gateway.transaction import DECLARE_SENDER_ADDRESS

from starknet_py.common import create_compiled_contract
from starknet_py.compile.compiler import StarknetCompilationSource
from starknet_py.net.models.transaction import Declare


def make_declare_tx(
    compilation_source: Optional[StarknetCompilationSource] = None,
    compiled_contract: Optional[str] = None,
    version: int = 0,
    cairo_path: Optional[List[str]] = None,
    max_fee: int = 0,
    signature: Optional[List[int]] = None,
    nonce: int = 0,
) -> Declare:
    """
    Create declaration tx.
    Either `compilation_source` or `compiled_contract` is required.

    :param compilation_source: string containing source code or a list of source files paths
    :param compiled_contract: string containing compiled contract bytecode.
                              Useful for reading compiled contract from a file
    :param version: PreparedFunctionCall version
    :param cairo_path: a ``list`` of paths used by starknet_compile to resolve dependencies within contracts
    :param max_fee: a maximum fee to be paid for declaring a contract on StarkNet
    :param signature: a transaction signature
    :param nonce: a nonce of the transaction
    :return: A "Declare" transaction object
    """
    # pylint: disable=too-many-arguments
    compiled_contract = create_compiled_contract(
        compilation_source, compiled_contract, cairo_path
    )
    return Declare(
        contract_class=compiled_contract,
        sender_address=DECLARE_SENDER_ADDRESS,
        max_fee=max_fee,
        signature=signature or [],
        nonce=nonce,
        version=version,
    )
