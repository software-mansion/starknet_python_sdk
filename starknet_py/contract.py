from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from marshmallow import ValidationError

from starknet_py.abi.v2.shape import (
    FUNCTION_ENTRY,
    IMPL_ENTRY,
    INTERFACE_ENTRY,
    L1_HANDLER_ENTRY,
)
from starknet_py.common import create_compiled_contract, create_sierra_compiled_contract
from starknet_py.constants import DEFAULT_DEPLOYER_ADDRESS
from starknet_py.contract_function import ContractData, ContractFunction
from starknet_py.contract_utils import _extract_compiled_class_hash, _unpack_provider
from starknet_py.hash.address import compute_address
from starknet_py.hash.class_hash import compute_class_hash
from starknet_py.net.account.base_account import BaseAccount
from starknet_py.net.client import Client
from starknet_py.net.client_models import Hash, ResourceBounds
from starknet_py.net.models import AddressRepresentation, parse_address
from starknet_py.net.models.transaction import Declare
from starknet_py.net.udc_deployer.deployer import Deployer
from starknet_py.proxy.contract_abi_resolver import (
    ContractAbiResolver,
    ProxyConfig,
    prepare_proxy_config,
)
from starknet_py.sent_transaction import SentTransaction
from starknet_py.utils.constructor_args_translator import translate_constructor_args
from starknet_py.utils.sync import add_sync_methods


@add_sync_methods
@dataclass(frozen=True)
class DeclareResult(SentTransaction):
    """
    Result of the Declare transaction.
    """

    _account: BaseAccount = None  # pyright: ignore
    _cairo_version: int = 0

    class_hash: int = None  # pyright: ignore
    """Class hash of the declared contract."""

    compiled_contract: str = None  # pyright: ignore
    """Compiled contract that was declared."""

    declare_transaction: Declare = None  # pyright: ignore
    """A Declare transaction that has been sent."""

    def __post_init__(self):
        if self._account is None:
            raise ValueError("Argument _account can't be None.")

        if self.class_hash is None:
            raise ValueError("Argument class_hash can't be None.")

        if self.compiled_contract is None:
            raise ValueError("Argument compiled_contract can't be None.")

        if self.declare_transaction is None:
            raise ValueError("Argument declare_transaction can't be None.")

    async def deploy_v1(
        self,
        *,
        deployer_address: AddressRepresentation = DEFAULT_DEPLOYER_ADDRESS,
        salt: Optional[int] = None,
        unique: bool = True,
        constructor_args: Optional[Union[List, Dict]] = None,
        nonce: Optional[int] = None,
        max_fee: Optional[int] = None,
        auto_estimate: bool = False,
    ) -> "DeployResult":
        """
        Deploys a contract.

        :param deployer_address: Address of the UDC. Is set to the address of
            the default UDC (same address on mainnet/testnet/devnet) by default.
            Must be set when using custom network other than ones listed above.
        :param salt: Optional salt. Random value is selected if it is not provided.
        :param unique: Determines if the contract should be salted with the account address.
        :param constructor_args: a ``list`` or ``dict`` of arguments for the constructor.
        :param nonce: Nonce of the transaction with call to deployer.
        :param max_fee: Max amount of Wei to be paid when executing transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :return: DeployResult instance.
        """
        # pylint: disable=too-many-arguments, too-many-locals
        abi = self._get_abi()

        return await Contract.deploy_contract_v1(
            account=self._account,
            class_hash=self.class_hash,
            abi=abi,
            constructor_args=constructor_args,
            deployer_address=deployer_address,
            cairo_version=self._cairo_version,
            nonce=nonce,
            max_fee=max_fee,
            auto_estimate=auto_estimate,
            salt=salt,
            unique=unique,
        )

    async def deploy_v3(
        self,
        *,
        deployer_address: AddressRepresentation = DEFAULT_DEPLOYER_ADDRESS,
        salt: Optional[int] = None,
        unique: bool = True,
        constructor_args: Optional[Union[List, Dict]] = None,
        nonce: Optional[int] = None,
        l1_resource_bounds: Optional[ResourceBounds] = None,
        auto_estimate: bool = False,
    ) -> "DeployResult":
        """
        Deploys a contract.

        :param deployer_address: Address of the UDC. Is set to the address of
            the default UDC (same address on mainnet/testnet/devnet) by default.
            Must be set when using custom network other than ones listed above.
        :param salt: Optional salt. Random value is selected if it is not provided.
        :param unique: Determines if the contract should be salted with the account address.
        :param constructor_args: a ``list`` or ``dict`` of arguments for the constructor.
        :param nonce: Nonce of the transaction with call to deployer.
        :param l1_resource_bounds: Max amount and max price per unit of L1 gas (in Wei) used when executing
            this transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :return: DeployResult instance.
        """
        # pylint: disable=too-many-arguments, too-many-locals
        abi = self._get_abi()

        return await Contract.deploy_contract_v3(
            account=self._account,
            class_hash=self.class_hash,
            abi=abi,
            constructor_args=constructor_args,
            deployer_address=deployer_address,
            cairo_version=self._cairo_version,
            nonce=nonce,
            l1_resource_bounds=l1_resource_bounds,
            auto_estimate=auto_estimate,
            salt=salt,
            unique=unique,
        )

    def _get_abi(self) -> List:
        if self._cairo_version == 0:
            abi = create_compiled_contract(compiled_contract=self.compiled_contract).abi
        else:
            try:
                sierra_compiled_contract = create_sierra_compiled_contract(
                    compiled_contract=self.compiled_contract
                )
                abi = json.loads(sierra_compiled_contract.abi)
            except Exception as exc:
                raise ValueError(
                    "Contract's ABI can't be converted to format List[Dict]. "
                    "Make sure provided compiled_contract is correct."
                ) from exc
        return abi


@add_sync_methods
@dataclass(frozen=True)
class DeployResult(SentTransaction):
    """
    Result of the contract deployment.
    """

    # We ensure this is not None in __post_init__
    deployed_contract: Contract = None  # pyright: ignore
    """A Contract instance representing the deployed contract."""

    def __post_init__(self):
        if self.deployed_contract is None:
            raise ValueError("Argument deployed_contract can't be None.")


FunctionsRepository = Dict[str, ContractFunction]


@add_sync_methods
class Contract:
    """
    Cairo contract's model.
    """

    def __init__(
        self,
        address: AddressRepresentation,
        abi: list,
        provider: Union[BaseAccount, Client],
        *,
        cairo_version: int = 0,
    ):
        """
        Should be used instead of ``from_address`` when ABI is known statically.

        Arguments provider and client are mutually exclusive and cannot be provided at the same time.

        :param address: contract's address.
        :param abi: contract's abi.
        :param provider: BaseAccount or Client used to perform transactions.
        :param cairo_version: Version of the Cairo in which contract is written.
        """
        client, account = _unpack_provider(provider)

        self.account: Optional[BaseAccount] = account
        self.client: Client = client
        self.data = ContractData.from_abi(parse_address(address), abi, cairo_version)

        try:
            self._functions = self._make_functions(
                contract_data=self.data,
                client=self.client,
                account=self.account,
                cairo_version=cairo_version,
            )
        except ValidationError as exc:
            raise ValueError(
                "Make sure valid ABI is used to create a Contract instance"
            ) from exc

    @property
    def functions(self) -> FunctionsRepository:
        """
        :return: All functions exposed from a contract.
        """
        return self._functions

    @property
    def address(self) -> int:
        """Address of the contract."""
        return self.data.address

    @staticmethod
    async def from_address(
        address: AddressRepresentation,
        provider: Union[BaseAccount, Client] = None,  # pyright: ignore
        proxy_config: Union[bool, ProxyConfig] = False,
    ) -> Contract:
        """
        Fetches ABI for given contract and creates a new Contract instance with it. If you know ABI statically you
        should create Contract's instances directly instead of using this function to avoid unnecessary API calls.

        :raises ContractNotFoundError: when contract is not found.
        :raises TypeError: when given client's `get_class_by_hash` method does not return abi.
        :raises ProxyResolutionError: when given ProxyChecks were not sufficient to resolve proxy's implementation.
        :param address: Contract's address.
        :param provider: BaseAccount or Client.
        :param proxy_config: Proxy resolving config
            If set to ``True``, will use default proxy checks
            :class:`starknet_py.proxy.proxy_check.OpenZeppelinProxyCheck`,
            :class:`starknet_py.proxy.proxy_check.ArgentProxyCheck`,
            and :class:`starknet_py.proxy.proxy_check.StarknetEthProxyCheck`.

            If set to ``False``, :meth:`Contract.from_address` will not resolve proxies.

            If a valid :class:`starknet_py.contract_abi_resolver.ProxyConfig` is provided, will use its values instead.

        :return: an initialized Contract instance.
        """
        client, account = _unpack_provider(provider)

        address = parse_address(address)
        proxy_config = Contract._create_proxy_config(proxy_config)

        abi, cairo_version = await ContractAbiResolver(
            address=address, client=client, proxy_config=proxy_config
        ).resolve()

        return Contract(
            address=address,
            abi=abi,
            provider=account or client,
            cairo_version=cairo_version,
        )

    @staticmethod
    async def declare_v1(
        account: BaseAccount,
        compiled_contract: str,
        *,
        nonce: Optional[int] = None,
        max_fee: Optional[int] = None,
        auto_estimate: bool = False,
    ) -> DeclareResult:
        """
        Declares a contract.

        :param account: BaseAccount used to sign and send declare transaction.
        :param compiled_contract: String containing compiled contract.
        :param nonce: Nonce of the transaction.
        :param max_fee: Max amount of Wei to be paid when executing transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :return: DeclareResult instance.
        """

        declare_tx = await account.sign_declare_v1_transaction(
            compiled_contract=compiled_contract,
            nonce=nonce,
            max_fee=max_fee,
            auto_estimate=auto_estimate,
        )
        res = await account.client.declare(transaction=declare_tx)

        return DeclareResult(
            hash=res.transaction_hash,
            class_hash=res.class_hash,
            compiled_contract=compiled_contract,
            declare_transaction=declare_tx,
            _account=account,
            _client=account.client,
            _cairo_version=0,
        )

    @staticmethod
    async def declare_v2(
        account: BaseAccount,
        compiled_contract: str,
        *,
        compiled_contract_casm: Optional[str] = None,
        compiled_class_hash: Optional[int] = None,
        nonce: Optional[int] = None,
        max_fee: Optional[int] = None,
        auto_estimate: bool = False,
    ) -> DeclareResult:
        """
        Declares a contract.

        :param account: BaseAccount used to sign and send declare transaction.
        :param compiled_contract: String containing compiled contract.
        :param compiled_contract_casm: String containing the content of the starknet-sierra-compile (.casm file).
        :param compiled_class_hash: Hash of the compiled_contract_casm.
        :param nonce: Nonce of the transaction.
        :param max_fee: Max amount of Wei to be paid when executing transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :return: DeclareResult instance.
        """

        compiled_class_hash = _extract_compiled_class_hash(
            compiled_contract_casm, compiled_class_hash
        )

        declare_tx = await account.sign_declare_v2_transaction(
            compiled_contract=compiled_contract,
            compiled_class_hash=compiled_class_hash,
            nonce=nonce,
            max_fee=max_fee,
            auto_estimate=auto_estimate,
        )

        res = await account.client.declare(transaction=declare_tx)

        return DeclareResult(
            hash=res.transaction_hash,
            class_hash=res.class_hash,
            compiled_contract=compiled_contract,
            declare_transaction=declare_tx,
            _account=account,
            _client=account.client,
            _cairo_version=1,
        )

    @staticmethod
    async def declare_v3(
        account: BaseAccount,
        compiled_contract: str,
        *,
        compiled_contract_casm: Optional[str] = None,
        compiled_class_hash: Optional[int] = None,
        nonce: Optional[int] = None,
        l1_resource_bounds: Optional[ResourceBounds] = None,
        auto_estimate: bool = False,
    ) -> DeclareResult:
        """
        Declares a contract.

        :param account: BaseAccount used to sign and send declare transaction.
        :param compiled_contract: String containing compiled contract.
        :param compiled_contract_casm: String containing the content of the starknet-sierra-compile (.casm file).
        :param compiled_class_hash: Hash of the compiled_contract_casm.
        :param nonce: Nonce of the transaction.
        :param l1_resource_bounds: Max amount and max price per unit of L1 gas (in Wei) used when executing
            this transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :return: DeclareResult instance.
        """

        compiled_class_hash = _extract_compiled_class_hash(
            compiled_contract_casm, compiled_class_hash
        )

        declare_tx = await account.sign_declare_v3_transaction(
            compiled_contract=compiled_contract,
            compiled_class_hash=compiled_class_hash,
            nonce=nonce,
            l1_resource_bounds=l1_resource_bounds,
            auto_estimate=auto_estimate,
        )

        res = await account.client.declare(transaction=declare_tx)

        return DeclareResult(
            hash=res.transaction_hash,
            class_hash=res.class_hash,
            compiled_contract=compiled_contract,
            declare_transaction=declare_tx,
            _account=account,
            _client=account.client,
            _cairo_version=1,
        )

    @staticmethod
    async def deploy_contract_v1(
        account: BaseAccount,
        class_hash: Hash,
        abi: List,
        constructor_args: Optional[Union[List, Dict]] = None,
        *,
        deployer_address: AddressRepresentation = DEFAULT_DEPLOYER_ADDRESS,
        cairo_version: int = 0,
        nonce: Optional[int] = None,
        max_fee: Optional[int] = None,
        auto_estimate: bool = False,
        salt: Optional[int] = None,
        unique: bool = True,
    ) -> "DeployResult":
        """
        Deploys a contract through Universal Deployer Contract.

        :param account: BaseAccount used to sign and send deploy transaction.
        :param class_hash: The class_hash of the contract to be deployed.
        :param abi: An abi of the contract to be deployed.
        :param constructor_args: a ``list`` or ``dict`` of arguments for the constructor.
        :param deployer_address: Address of the UDC. Is set to the address of
            the default UDC (same address on mainnet/testnet/devnet) by default.
            Must be set when using custom network other than ones listed above.
        :param cairo_version: Version of the Cairo in which contract is written.
            By default, it is set to 0.
        :param nonce: Nonce of the transaction.
        :param max_fee: Max amount of Wei to be paid when executing transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :param salt: Optional salt. Random value is selected if it is not provided.
        :param unique: Determines if the contract should be salted with the account address.
        :return: DeployResult instance.
        """
        # pylint: disable=too-many-arguments
        deployer = Deployer(
            deployer_address=deployer_address,
            account_address=account.address if unique else None,
        )
        deploy_call, address = deployer.create_contract_deployment(
            class_hash=class_hash,
            salt=salt,
            abi=abi,
            calldata=constructor_args,
            cairo_version=cairo_version,
        )

        res = await account.execute(
            calls=deploy_call,
            nonce=nonce,
            max_fee=max_fee,
            auto_estimate=auto_estimate,
        )

        deployed_contract = Contract(
            provider=account, address=address, abi=abi, cairo_version=cairo_version
        )
        deploy_result = DeployResult(
            hash=res.transaction_hash,
            _client=account.client,
            deployed_contract=deployed_contract,
        )

        return deploy_result

    @staticmethod
    async def deploy_contract_v3(
        account: BaseAccount,
        class_hash: Hash,
        abi: List,
        constructor_args: Optional[Union[List, Dict]] = None,
        *,
        deployer_address: AddressRepresentation = DEFAULT_DEPLOYER_ADDRESS,
        cairo_version: int = 1,
        nonce: Optional[int] = None,
        l1_resource_bounds: Optional[ResourceBounds] = None,
        auto_estimate: bool = False,
        salt: Optional[int] = None,
        unique: bool = True,
    ) -> "DeployResult":
        """
        Deploys a contract through Universal Deployer Contract.

        :param account: BaseAccount used to sign and send deploy transaction.
        :param class_hash: The class_hash of the contract to be deployed.
        :param abi: An abi of the contract to be deployed.
        :param constructor_args: a ``list`` or ``dict`` of arguments for the constructor.
        :param deployer_address: Address of the UDC. Is set to the address of
            the default UDC (same address on mainnet/testnet/devnet) by default.
            Must be set when using custom network other than ones listed above.
        :param cairo_version: Version of the Cairo in which contract is written.
            By default, it is set to 1.
        :param nonce: Nonce of the transaction.
        :param l1_resource_bounds: Max amount and max price per unit of L1 gas (in Wei) used when executing
            this transaction.
        :param auto_estimate: Use automatic fee estimation (not recommended, as it may lead to high costs).
        :param salt: Optional salt. Random value is selected if it is not provided.
        :param unique: Determines if the contract should be salted with the account address.
        :return: DeployResult instance.
        """
        # pylint: disable=too-many-arguments
        deployer = Deployer(
            deployer_address=deployer_address,
            account_address=account.address if unique else None,
        )
        deploy_call, address = deployer.create_contract_deployment(
            class_hash=class_hash,
            salt=salt,
            abi=abi,
            calldata=constructor_args,
            cairo_version=cairo_version,
        )

        res = await account.execute_v3(
            calls=deploy_call,
            nonce=nonce,
            l1_resource_bounds=l1_resource_bounds,
            auto_estimate=auto_estimate,
        )

        deployed_contract = Contract(
            provider=account, address=address, abi=abi, cairo_version=cairo_version
        )
        deploy_result = DeployResult(
            hash=res.transaction_hash,
            _client=account.client,
            deployed_contract=deployed_contract,
        )

        return deploy_result

    @staticmethod
    def compute_address(
        salt: int,
        compiled_contract: str,
        constructor_args: Optional[Union[List, Dict]] = None,
        deployer_address: int = 0,
    ) -> int:
        """
        Computes address for given contract.

        :param salt: int
        :param compiled_contract: String containing compiled contract.
        :param constructor_args: A ``list`` or ``dict`` of arguments for the constructor.
        :param deployer_address: Address of the deployer (if not provided default 0 is used).

        :return: Contract's address.
        """

        compiled = create_compiled_contract(compiled_contract)
        assert compiled.abi is not None
        translated_args = translate_constructor_args(compiled.abi, constructor_args)
        return compute_address(
            salt=salt,
            class_hash=compute_class_hash(compiled),
            constructor_calldata=translated_args,
            deployer_address=deployer_address,
        )

    @staticmethod
    def compute_contract_hash(compiled_contract: str) -> int:
        """
        Computes hash for given contract.

        :param compiled_contract: String containing compiled contract.
        :return: Class_hash of the contract.
        """

        contract_class = create_compiled_contract(compiled_contract)
        return compute_class_hash(contract_class)

    @classmethod
    def _make_functions(
        cls,
        contract_data: ContractData,
        client: Client,
        account: Optional[BaseAccount],
        cairo_version: int = 0,
    ) -> FunctionsRepository:
        repository = {}
        implemented_interfaces = [
            entry["interface_name"]
            for entry in contract_data.abi
            if entry["type"] == IMPL_ENTRY
        ]

        for abi_entry in contract_data.abi:
            if abi_entry["type"] in [FUNCTION_ENTRY, L1_HANDLER_ENTRY]:
                name = abi_entry["name"]
                repository[name] = ContractFunction(
                    name=name,
                    abi=abi_entry,
                    contract_data=contract_data,
                    client=client,
                    account=account,
                    cairo_version=cairo_version,
                )

            if (
                abi_entry["type"] == INTERFACE_ENTRY
                and abi_entry["name"] in implemented_interfaces
            ):
                for item in abi_entry["items"]:
                    name = item["name"]
                    repository[name] = ContractFunction(
                        name=name,
                        abi=item,
                        contract_data=contract_data,
                        client=client,
                        account=account,
                        cairo_version=cairo_version,
                        interface_name=abi_entry["name"],
                    )

        return repository

    @staticmethod
    def _create_proxy_config(proxy_config) -> ProxyConfig:
        if proxy_config is False:
            return ProxyConfig()
        proxy_arg = ProxyConfig() if proxy_config is True else proxy_config
        return prepare_proxy_config(proxy_arg)
