import pytest
from starkware.starknet.public.abi import get_selector_from_name

from starknet_py.net.client_models import (
    DeployTransaction,
    InvokeFunction,
)
from starknet_py.tests.e2e.utils import DevnetClientFactory


@pytest.mark.asyncio
async def test_node_get_transaction_by_block_hash_and_index(
    devnet_address,
    block_with_deploy_hash,
    deploy_transaction_hash,
    contract_address,
):
    client = await DevnetClientFactory(devnet_address).make_rpc_client()

    tx = await client.get_transaction_by_block_hash(
        block_hash=block_with_deploy_hash, index=0
    )

    assert tx == DeployTransaction(
        hash=deploy_transaction_hash,
        contract_address=contract_address,
        constructor_calldata=[],
        max_fee=0,
        signature=[],
        # class_hash=class_hash,
    )


@pytest.mark.asyncio
async def test_node_get_transaction_by_block_number_and_index(
    devnet_address, deploy_transaction_hash, contract_address
):
    client = await DevnetClientFactory(devnet_address).make_rpc_client()

    tx = await client.get_transaction_by_block_number(block_number=0, index=0)

    assert tx == DeployTransaction(
        hash=deploy_transaction_hash,
        contract_address=contract_address,
        constructor_calldata=[],
        max_fee=0,
        signature=[],
        # class_hash=class_hash,
    )


@pytest.mark.asyncio
async def test_get_block_throws_on_no_block_hash_and_no_number(devnet_address):
    client = await DevnetClientFactory(devnet_address).make_rpc_client()

    with pytest.raises(ValueError) as exinfo:
        await client.get_block()

    assert "Either block_hash or block_number is required" in str(exinfo.value)
