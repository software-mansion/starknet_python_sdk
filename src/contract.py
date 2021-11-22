import asyncio
import dataclasses
from dataclasses import dataclass
from typing import Iterable, Union, List, Optional

from services.external_api.base_client import RetryConfig
from starkware.cairo.lang.compiler.ast.cairo_types import (
    TypePointer,
    TypeFelt,
    CairoType,
)
from starkware.cairo.lang.compiler.identifier_manager import IdentifierManager
from starkware.cairo.lang.compiler.parser import parse_type
from starkware.cairo.lang.compiler.type_system import mark_type_resolved
from starkware.cairo.lang.compiler.type_utils import check_felts_only_type
from starkware.starknet.public.abi import get_selector_from_name
from starkware.starknet.public.abi_structs import identifier_manager_from_abi
from starkware.starknet.services.api.feeder_gateway.feeder_gateway_client import (
    FeederGatewayClient,
)
from starkware.starknet.services.api.gateway.gateway_client import GatewayClient
from starkware.starknet.services.api.gateway.transaction import InvokeFunction
from starkware.starkware_utils.error_handling import StarkErrorCode

ABI = list
ABIEntry = dict


@dataclass(frozen=True)
class ContractData:
    address: int
    abi: ABI
    identifier_manager: IdentifierManager

    @staticmethod
    def from_abi(address: int, abi: ABI) -> "ContractData":
        return ContractData(
            address=address,
            abi=abi,
            identifier_manager=identifier_manager_from_abi(abi),
        )


dns = "alpha3.starknet.io"


# TODO: REMOVE
def get_feeder_gateway_client() -> FeederGatewayClient:
    feeder_gateway_url = f"https://{dns}/feeder_gateway"
    # Limit the number of retries.
    retry_config = RetryConfig(n_retries=1)
    return FeederGatewayClient(url=feeder_gateway_url, retry_config=retry_config)


# TODO: REMOVE
def get_gateway_client() -> GatewayClient:
    gateway_url = f"https://{dns}/gateway"
    # Limit the number of retries.
    retry_config = RetryConfig(n_retries=1)
    return GatewayClient(url=gateway_url, retry_config=retry_config)


async def wait_for_tx(
    hash, wait_for_accept: Optional[bool] = False, check_interval=5
) -> int:
    """

    :param hash: Transaction's hash
    :param wait_for_accept: If true waits for ACCEPTED_ONCHAIN status, otherwise waits for at least PENDING
    :param check_interval: Defines interval between checks
    :return: number of block
    """
    assert check_interval > 0, "check_interval has to bigger than 0"

    client = get_feeder_gateway_client()
    first_run = True
    while True:
        result = await client.get_transaction(tx_hash=hash)
        status = result["status"]

        if status == "ACCEPTED_ONCHAIN":
            return result["block_id"]
        elif status == "PENDING":
            if not wait_for_accept:
                return result["block_id"]
        elif status == "REJECTED":
            raise Exception(f"Transaction [{hash}] was rejected.")
        elif status == "NOT_RECEIVED":
            if not first_run:
                raise Exception(f"Transaction [{hash}] was not received.")
        elif status != "RECEIVED":
            raise Exception(f"Unknown status [{status}]")

        first_run = False
        await asyncio.sleep(check_interval)


@dataclass(frozen=True)
class InvocationResult:
    hash: str
    contract: ContractData
    status: Optional[str] = None
    block_number: Optional[int] = None

    async def wait_for_acceptance(
        self, wait_for_accept: Optional[bool] = False, check_interval=5
    ) -> "InvocationResult":
        block_number = await wait_for_tx(
            int(self.hash, 16),
            wait_for_accept=wait_for_accept,
            check_interval=check_interval,
        )
        return dataclasses.replace(
            self,
            status="ACCEPTED_ONCHAIN" if wait_for_accept else "PENDING",
            block_number=block_number,
        )


class ContractFunction:
    def __init__(self, name: str, abi: ABIEntry, contract_data: ContractData):
        self.name = name
        self.inputs = abi["inputs"]
        self.contract_data = contract_data

    async def call(
        self,
        block_hash: Optional[str] = None,
        block_number: Optional[int] = None,
        signature: Optional[List[str]] = None,
        **kwargs,
    ):
        tx = self._make_invoke_function(signature=signature, **kwargs)
        feeder_client = get_feeder_gateway_client()
        result = await feeder_client.call_contract(
            invoke_tx=tx, block_hash=block_hash, block_number=block_number
        )
        return result["result"]

    async def invoke(self, signature: Optional[List[str]] = None, **kwargs):
        tx = self._make_invoke_function(signature=signature, **kwargs)
        gateway_client = get_gateway_client()
        gateway_response = await gateway_client.add_transaction(tx=tx)
        assert (
            gateway_response["code"] == StarkErrorCode.TRANSACTION_RECEIVED.name
        ), f"Failed to send transaction. Response: {gateway_response}."
        return InvocationResult(
            hash=gateway_response["transaction_hash"],  # noinspection PyTypeChecker
            contract=self.contract_data,
        )

    @property
    def selector(self):
        return get_selector_from_name(self.name)

    def _make_invoke_function(self, signature=None, **kwargs):
        return InvokeFunction(
            contract_address=self.contract_data.address,
            entry_point_selector=self.selector,
            calldata=self._make_calldata(**kwargs),
            signature=signature or [],
        )

    def _make_calldata(self, **kwargs) -> List[int]:
        calldata: List[int] = []
        for input_desc in self.inputs:
            name = input_desc["name"]
            assert name in kwargs, f"Input {name} not provided"

            cairo_type = mark_type_resolved(parse_type(input_desc["type"]))
            values = self._get_value(name, kwargs[name], cairo_type)

            calldata.extend(values)
        return calldata

    def _get_value(
        self, name: str, value: Union[int, Iterable[int]], cairo_type: CairoType
    ) -> List[int]:
        if isinstance(cairo_type, TypeFelt):
            return [self._get_int(name, value)]

        typ_size = check_felts_only_type(
            cairo_type=cairo_type,
            identifier_manager=self.contract_data.identifier_manager,
        )
        if typ_size is not None:
            return self._get_n_ints(name, typ_size, value)

        if cairo_type == TypePointer(pointee=TypeFelt()):
            values = self._get_ints(name, value)
            return [len(values), *values]

        raise Exception(f"Type {cairo_type} not supported")

    def _get_int(self, name: str, value: any) -> int:
        assert isinstance(value, int), f"{name} should be int"
        return value

    def _get_ints(self, name: str, values: any) -> List[int]:
        return [self._get_int(f"{name}[{i}]", value) for i, value in enumerate(values)]

    def _get_n_ints(self, name: str, n: int, values: any) -> List[int]:
        values = self._get_ints(name, values)

        assert n > 0, "Can't request less than 1 value"
        assert len(values) == n, f"Length of {name} is {len(values)}. Expected {n}."

        return values


class ContractFunctionsRepository:
    def __init__(self, contract_data: ContractData):
        for abi_entry in contract_data.abi:
            if abi_entry["type"] != "function":
                return

            name = abi_entry["name"]
            setattr(
                self,
                name,
                ContractFunction(
                    name=name,
                    abi=abi_entry,
                    contract_data=contract_data,
                ),
            )


class Contract:
    def __init__(self, address: int, abi: list):
        self.data = ContractData.from_abi(address, abi)
        self.functions = ContractFunctionsRepository(self.data)
