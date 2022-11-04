from __future__ import annotations

from typing import Optional, List, Union

from starkware.starknet.definitions.fields import ContractAddressSalt
from starkware.starknet.public.abi import get_selector_from_name

from starknet_py.common import int_from_hex
from starknet_py.constants import DEFAULT_DEPLOYER_ADDRESS
from starknet_py.net import AccountClient
from starknet_py.net.client_models import Hash, InvokeFunction, Call, Event
from starknet_py.net.models import AddressRepresentation
from starknet_py.net.udc_deployer.errors import ContractDeployedEventNotFound
from starknet_py.utils.contructor_args_translator import translate_constructor_args
from starknet_py.utils.data_transformer.universal_deployer_serializer import (
    universal_deployer_serializer,
    deploy_contract_abi,
    deploy_contract_event_abi,
)
from starknet_py.utils.sync import add_sync_methods


@add_sync_methods
class Deployer:
    """
    Deployer used to deploy contracts through Universal Deployer Contract (UDC)
    """

    def __init__(
        self,
        account: AccountClient,
        *,
        deployer_address: Optional[AddressRepresentation] = None,
        unique: bool = True,
    ):
        """
        :param account: AccountClient used to sign and send transactions
        :param deployer_address: Address of the UDC. Must be set when using a custom network
        :param unique: Boolean determining if the salt should be connected with the account's address. Default to True
        """
        deployer_address = deployer_address or DEFAULT_DEPLOYER_ADDRESS

        self.account = account
        self.deployer_address = deployer_address
        self.unique = unique

    async def prepare_contract_deployment(
        self,
        *,
        class_hash: Hash,
        salt: Optional[int] = None,
        abi: Optional[List] = None,
        calldata: Optional[Union[List, dict]] = None,
        max_fee: Optional[int] = None,
        auto_estimate: bool = False,
    ) -> InvokeFunction:
        """
        Prepares deploy invoke transaction

        :param class_hash: The class_hash of the contract to be deployed
        :param salt: The salt for a contract to be deployed. Random value is selected if it is not provided
        :param abi: ABI of the contract to be deployed
        :param calldata: Constructor args of the contract to be deployed
        :param max_fee: Max amount of Wei to be paid when executing transaction
        :param auto_estimate: Use automatic fee estimation, not recommend as it may lead to high costs
        :return: InvokeFunction
        """

        if not abi and calldata:
            raise ValueError("calldata was provided without an abi")

        calldata = translate_constructor_args(abi=abi or [], constructor_args=calldata)

        calldata, _ = universal_deployer_serializer.from_python(
            value_types=deploy_contract_abi["inputs"],
            classHash=int_from_hex(class_hash),
            salt=salt or ContractAddressSalt.get_random_value(),
            unique=int(self.unique),
            calldata=calldata,
        )

        call = Call(
            to_addr=self.deployer_address,
            selector=get_selector_from_name("deployContract"),
            calldata=calldata,
        )

        transaction = await self.account.sign_invoke_transaction(
            calls=call, max_fee=max_fee, auto_estimate=auto_estimate
        )

        return transaction

    async def find_deployed_contract_address(self, transaction_hash: Hash) -> int:
        """
        Returns deployed contract address

        :param transaction_hash: Hash of the already send and accepted deploy invoke transaction
        :returns: An address of the deployed contract
        """
        event = await self._get_deploy_event(transaction_hash=transaction_hash)

        if not event:
            raise ContractDeployedEventNotFound(transaction_hash=transaction_hash)

        event = universal_deployer_serializer.to_python(
            value_types=deploy_contract_event_abi["data"],
            values=event.data,
        )

        # Ignore typing, because event is a NamedTuple
        return event.address  # pyright: ignore

    async def _get_deploy_event(self, transaction_hash: Hash) -> Optional[Event]:
        receipt = await self.account.get_transaction_receipt(tx_hash=transaction_hash)

        for event in receipt.events:
            if get_selector_from_name("ContractDeployed") == event.keys[0]:
                return event
        return None
