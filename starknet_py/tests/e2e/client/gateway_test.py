from unittest.mock import AsyncMock, patch

import pytest
from starkware.starknet.public.abi import get_storage_var_address

from starknet_py.net.client_errors import ContractNotFoundError
from starknet_py.net.client_models import (
    TransactionStatusResponse,
    TransactionStatus,
    L1HandlerTransaction,
)
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET, MAINNET, CustomGatewayUrls


@pytest.mark.asyncio
async def test_gateway_raises_on_both_block_hash_and_number(
    block_with_declare_number, gateway_client
):
    with pytest.raises(ValueError) as exinfo:
        await gateway_client.get_block(
            block_hash="0x0", block_number=block_with_declare_number
        )

    assert "block_hash and block_number parameters are mutually exclusive" in str(
        exinfo.value
    )


@pytest.mark.asyncio
async def test_get_class_hash_at(contract_address, gateway_client, class_hash):
    class_hash_resp = await gateway_client.get_class_hash_at(
        contract_address=contract_address
    )

    assert class_hash_resp == class_hash


@pytest.mark.asyncio
async def test_get_code(contract_address, gateway_client):
    code = await gateway_client.get_code(contract_address=contract_address)

    assert code.abi is not None
    assert len(code.abi) != 0
    assert code.bytecode is not None
    assert len(code.bytecode) != 0


@pytest.mark.asyncio
async def test_get_code_invalid_address(gateway_client):
    with pytest.raises(
        ContractNotFoundError,
        match="^Client failed: No contract with address 123 found$",
    ):
        await gateway_client.get_code(contract_address=123)

    with pytest.raises(
        ContractNotFoundError,
        match="^Client failed: No contract with address 123 found for block with block_number: latest$",
    ):
        await gateway_client.get_code(contract_address=123, block_number="latest")


@pytest.mark.asyncio
async def test_get_contract_nonce(gateway_client):
    nonce = await gateway_client.get_contract_nonce(
        contract_address=0x1111,
        block_hash="latest",
    )
    assert nonce == 0


@pytest.mark.asyncio
async def test_get_transaction_status(invoke_transaction_hash, gateway_client):
    tx_status_resp = await gateway_client.get_transaction_status(
        invoke_transaction_hash
    )
    assert isinstance(tx_status_resp, TransactionStatusResponse)
    assert tx_status_resp.transaction_status == TransactionStatus.ACCEPTED_ON_L2
    assert isinstance(tx_status_resp.block_hash, int)


# pylint: disable=protected-access
@pytest.mark.parametrize(
    "net, net_address",
    (
        (TESTNET, "https://alpha4.starknet.io"),
        (MAINNET, "https://alpha-mainnet.starknet.io"),
    ),
)
def test_creating_client_from_predefined_network(net, net_address):
    gateway_client = GatewayClient(net=net)

    assert gateway_client.net == net
    assert gateway_client._feeder_gateway_client.url == f"{net_address}/feeder_gateway"
    assert gateway_client._gateway_client.url == f"{net_address}/gateway"


def test_creating_client_with_custom_net():
    custom_net = "custom.net"
    gateway_client = GatewayClient(net=custom_net)

    assert gateway_client.net == custom_net
    assert gateway_client._feeder_gateway_client.url == f"{custom_net}/feeder_gateway"
    assert gateway_client._gateway_client.url == f"{custom_net}/gateway"


def test_creating_client_with_custom_net_dict():
    custom_net = "custom.net"
    net = CustomGatewayUrls(
        feeder_gateway_url=f"{custom_net}/feeder_gateway",
        gateway_url=f"{custom_net}/gateway",
    )

    gateway_client = GatewayClient(net=net)

    assert gateway_client.net == net
    assert gateway_client._feeder_gateway_client.url == net["feeder_gateway_url"]
    assert gateway_client._gateway_client.url == net["gateway_url"]


@pytest.mark.asyncio
async def test_state_update_gateway_client(
    gateway_client,
    block_with_declare_number,
    class_hash,
):
    state_update = await gateway_client.get_state_update(
        block_number=block_with_declare_number
    )

    assert class_hash in state_update.declared_contracts


@pytest.mark.asyncio
async def test_get_storage_at_incorrect_address_gateway_client(gateway_client):
    storage = await gateway_client.get_storage_at(
        contract_address=0x1111,
        key=get_storage_var_address("balance"),
        block_hash="latest",
    )
    assert storage == 0


@pytest.mark.asyncio
async def test_get_l1_handler_transaction_without_nonce(gateway_client):
    with patch(
        "starknet_py.net.http_client.GatewayHttpClient.call", AsyncMock()
    ) as mocked_transaction_call:
        mocked_transaction_call.return_value = {
            "status": "ACCEPTED_ON_L1",
            "block_hash": "0x38ce7678420eaff5cd62597643ca515d0887579a8be69563067fe79a624592b",
            "block_number": 370459,
            "transaction_index": 9,
            "transaction": {
                "version": "0x0",
                "contract_address": "0x278f24c3e74cbf7a375ec099df306289beb0605a346277d200b791a7f811a19",
                "entry_point_selector": "0x2d757788a8d8d6f21d1cd40bce38a8222d70654214e96ff95d8086e684fbee5",
                "calldata": [
                    "0xd8beaa22894cd33f24075459cfba287a10a104e4",
                    "0x3f9c67ef1d31e24b386184b4ede63a869c4659de093ef437ee235cae4daf2be",
                    "0x3635c9adc5dea00000",
                    "0x0",
                    "0x7cb4539b69a2371f75d21160026b76a7a7c1cacb",
                ],
                "transaction_hash": "0x7e1ed66dbccf915857c6367fc641c24292c063e54a5dd55947c2d958d94e1a9",
                "type": "L1_HANDLER",
            },
        }

        transaction = await gateway_client.get_transaction(tx_hash=0x1)

        assert isinstance(transaction, L1HandlerTransaction)
        assert transaction.nonce is None
