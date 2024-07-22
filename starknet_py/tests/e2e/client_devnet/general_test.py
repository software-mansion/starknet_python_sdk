from typing import List

import pytest

from starknet_py.devnet.devnet_client_models import PredeployedAccount


@pytest.mark.asyncio
async def test_mint(devnet_client, account_devnet):
    amount = 1000

    balance_before_mint = await account_devnet.get_balance()
    await devnet_client.mint(account_devnet.address, amount)
    balance_after_mint = await account_devnet.get_balance()

    assert balance_after_mint == balance_before_mint + amount


@pytest.mark.asyncio
async def test_create_blocks(devnet_client):
    block_hash = await devnet_client.create_block()
    assert block_hash is not None


@pytest.mark.asyncio
async def test_abort_blocks(devnet_client):
    block_hash = await devnet_client.create_block()
    for _ in range(5):
        await devnet_client.create_block()

    aborted_blocks = await devnet_client.abort_block(block_hash)
    assert len(aborted_blocks) == 6


@pytest.mark.asyncio
async def test_predeployed_accounts(devnet_client):
    accounts = await devnet_client.get_predeployed_accounts()

    isinstance(accounts, List)
    assert len(accounts) > 0
    isinstance(accounts[0], PredeployedAccount)