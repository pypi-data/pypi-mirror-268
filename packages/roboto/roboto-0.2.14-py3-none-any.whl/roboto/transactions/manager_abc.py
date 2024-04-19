import abc
import typing

from ..domain.datasets.http_resources import (
    BeginManifestTransactionResponse,
)
from .record import (
    TransactionRecord,
    TransactionType,
)


class TransactionManagerABC(abc.ABC):
    @abc.abstractmethod
    def begin_transaction(
        self,
        transaction_type: TransactionType,
        origination: str,
        expected_resource_count: typing.Optional[int] = None,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        raise NotImplementedError("begin_transaction")

    @abc.abstractmethod
    def get_transaction(
        self,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        raise NotImplementedError("get_transaction")

    @abc.abstractmethod
    def is_transaction_complete(
        self,
        transaction_id: str,
        resource_owner_id: str,
    ) -> bool:
        raise NotImplementedError("is_transaction_complete")

    @abc.abstractmethod
    def begin_manifest_transaction(
        self,
        origination: str,
        dataset_id: str,
        resource_manifest: dict[str, int] = {},
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> BeginManifestTransactionResponse:
        raise NotImplementedError("begin_manifest_transaction")

    @abc.abstractmethod
    def on_manifest_item_complete(
        self,
        dataset_id: str,
        transaction_id: str,
        manifest_item_identifier: str,
        future,
        **kwargs,
    ) -> None:
        raise NotImplementedError("on_manifest_item_complete")

    @abc.abstractmethod
    def flush_manifest_item_completions(
        self,
        dataset_id: str,
        transaction_id: str,
        manifest_items: list[str],
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        raise NotImplementedError("flush_manifest_item_completions")

    @abc.abstractmethod
    def complete_manifest_transaction(
        self,
        dataset_id: str,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        raise NotImplementedError("complete_manifest_transaction")
