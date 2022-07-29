import pytest

from starknet_py.contract import Contract

MAX_FEE = int(1e20)

COMPILED_PROXY_SOURCES = ["argent_proxy_compiled.json", "oz_proxy_compiled.json"]


@pytest.mark.asyncio
@pytest.mark.parametrize("compiled_proxy", COMPILED_PROXY_SOURCES, indirect=True)
async def test_argent_contract_from_address_throws_on_too_many_steps(
    gateway_client, map_contract, compiled_proxy
):
    proxy1_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[map_contract.address],
        client=gateway_client,
    )
    proxy2_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[proxy1_deployment.deployed_contract.address],
        client=gateway_client,
    )

    with pytest.raises(RecursionError) as exinfo:
        await Contract.from_address(
            proxy2_deployment.deployed_contract.address,
            client=gateway_client,
            proxy_config={"max_steps": 2},
        )

    assert "Max number of steps exceeded" in str(exinfo.value)


@pytest.mark.asyncio
@pytest.mark.parametrize("compiled_proxy", COMPILED_PROXY_SOURCES, indirect=True)
async def test_contract_from_address_throws_on_proxy_cycle(
    gateway_account_client, compiled_proxy
):
    proxy1_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[0x123],
        client=gateway_account_client,
    )
    proxy2_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[0x123],
        client=gateway_account_client,
    )
    await proxy1_deployment.wait_for_acceptance()
    await proxy2_deployment.wait_for_acceptance()

    proxy1 = proxy1_deployment.deployed_contract
    proxy2 = proxy2_deployment.deployed_contract

    argent_proxy = "_set_implementation" in proxy1.functions

    if argent_proxy:
        await proxy1.functions["_set_implementation"].invoke(
            implementation=proxy2.address, max_fee=MAX_FEE
        )
        await proxy2.functions["_set_implementation"].invoke(
            implementation=proxy1.address, max_fee=MAX_FEE
        )
    else:
        await proxy1.functions["_set_implementation_hash"].invoke(
            new_implementation=proxy2.address, max_fee=MAX_FEE
        )
        await proxy2.functions["_set_implementation_hash"].invoke(
            new_implementation=proxy1.address, max_fee=MAX_FEE
        )

    with pytest.raises(RecursionError) as exinfo:
        await Contract.from_address(
            address=proxy2_deployment.deployed_contract.address,
            client=gateway_account_client,
            proxy_config=True,
        )

    assert "Proxy cycle detected" in str(exinfo.value)


@pytest.mark.asyncio
@pytest.mark.parametrize("compiled_proxy", COMPILED_PROXY_SOURCES, indirect=True)
async def test_contract_from_address_with_1_proxy(
    gateway_client, map_contract, compiled_proxy
):
    deployment_result = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[map_contract.address],
        client=gateway_client,
    )

    proxy_contract = await Contract.from_address(
        deployment_result.deployed_contract.address,
        client=gateway_client,
        proxy_config=True,
    )

    assert all(f in proxy_contract.functions for f in ("put", "get"))


@pytest.mark.asyncio
@pytest.mark.parametrize("compiled_proxy", COMPILED_PROXY_SOURCES, indirect=True)
async def test_contract_from_address_with_2_proxy(
    gateway_client, map_contract, compiled_proxy
):
    proxy1_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[map_contract.address],
        client=gateway_client,
    )
    proxy2_deployment = await Contract.deploy(
        compiled_contract=compiled_proxy,
        constructor_args=[proxy1_deployment.deployed_contract.address],
        client=gateway_client,
    )

    proxy_contract = await Contract.from_address(
        proxy2_deployment.deployed_contract.address,
        client=gateway_client,
        proxy_config=True,
    )

    assert all(f in proxy_contract.functions for f in ("put", "get"))
