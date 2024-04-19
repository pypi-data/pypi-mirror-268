import threading
import typing

from ..domain.datasets.http_resources import (
    BeginManifestTransactionRequest,
    BeginManifestTransactionResponse,
    BeginSingleFileUploadRequest,
    BeginSingleFileUploadResponse,
    ReportTransactionProgressRequest,
)
from ..exceptions import (
    RobotoHttpExceptionParse,
    RobotoNotFoundException,
)
from ..http import HttpClient, roboto_headers
from ..logging import default_logger
from .http_resources import (
    BeginTransactionRequest,
    TransactionCompletionResponse,
)
from .manager_abc import TransactionManagerABC
from .record import (
    TransactionRecord,
    TransactionType,
)

logger = default_logger()


class TransactionManager(TransactionManagerABC):
    __http_client: HttpClient
    __roboto_service_base_url: str
    __transaction_manifests: dict[str, set[str]]
    __transaction_completed_unreported_items: dict[str, set[str]]
    __manifests_lock: threading.RLock
    __manifest_items_lock: threading.RLock
    __manifest_reporting_increments: int = 10
    __manifest_reporting_min_batch_size: int = 10

    def __init__(self, roboto_service_base_url: str, http_client: HttpClient) -> None:
        self.__http_client = http_client
        self.__roboto_service_base_url = roboto_service_base_url
        self.__transaction_manifests = {}
        self.__transaction_completed_unreported_items = {}
        self.__manifests_lock = threading.RLock()
        self.__manifest_items_lock = threading.RLock()

    def begin_transaction(
        self,
        transaction_type: TransactionType,
        origination: str,
        expected_resource_count: typing.Optional[int] = None,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        url = f"{self.__roboto_service_base_url}/v2/transactions/begin"
        request_body = BeginTransactionRequest(
            transaction_type=transaction_type,
            origination=origination,
            expected_resource_count=expected_resource_count,
        )

        with RobotoHttpExceptionParse():
            response = self.__http_client.post(
                url,
                data=request_body.model_dump_json(exclude_none=True),
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        return TransactionRecord.model_validate(response.from_json(json_path=["data"]))

    def get_transaction(
        self,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        url = f"{self.__roboto_service_base_url}/v2/transactions/id/{transaction_id}"
        with RobotoHttpExceptionParse():
            response = self.__http_client.get(
                url,
                headers=roboto_headers(
                    org_id=org_id,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        return TransactionRecord.model_validate(response.from_json(json_path=["data"]))

    def is_transaction_complete(
        self,
        transaction_id: str,
        resource_owner_id: str,
    ) -> bool:
        url = f"{self.__roboto_service_base_url}/v2/transactions/id/{transaction_id}/completion"
        with RobotoHttpExceptionParse():
            response = self.__http_client.get(
                url,
                headers=roboto_headers(
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        return TransactionCompletionResponse.model_validate(
            response.from_json(json_path=["data"])
        ).is_complete

    def begin_manifest_transaction(
        self,
        origination: str,
        dataset_id: str,
        resource_manifest: dict[str, int] = {},
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> BeginManifestTransactionResponse:
        url = f"{self.__roboto_service_base_url}/v2/datasets/{dataset_id}/batch_uploads"
        request_body = BeginManifestTransactionRequest(
            origination=origination,
            resource_manifest=resource_manifest,
        )

        with RobotoHttpExceptionParse():
            response = self.__http_client.post(
                url,
                data=request_body.model_dump_json(exclude_none=True),
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        result = BeginManifestTransactionResponse.model_validate(
            response.from_json(json_path=["data"])
        )
        record = result.record
        with self.__manifests_lock:
            self.__transaction_manifests[record.transaction_id] = set(
                result.upload_mappings.values()
            )

        return result

    def on_manifest_item_complete(
        self,
        dataset_id: str,
        transaction_id: str,
        manifest_item_identifier: str,
        future,
        **kwargs,
    ) -> None:
        logger.debug(
            "START on_manifest_item_complete: %s, %s, %s, %s",
            dataset_id,
            transaction_id,
            manifest_item_identifier,
            future,
        )
        with self.__manifest_items_lock:
            if transaction_id not in self.__transaction_manifests:
                raise RobotoNotFoundException(
                    f"Transaction {transaction_id} does not have a manifest"
                )

            if transaction_id not in self.__transaction_completed_unreported_items:
                self.__transaction_completed_unreported_items[transaction_id] = set()

            self.__transaction_completed_unreported_items[transaction_id].add(
                manifest_item_identifier
            )

            if self.__unreported_manifest_items_batch_ready_to_report(transaction_id):
                self.flush_manifest_item_completions(
                    dataset_id=dataset_id,
                    transaction_id=transaction_id,
                    manifest_items=list(
                        self.__transaction_completed_unreported_items[transaction_id]
                    ),
                )
                self.__transaction_completed_unreported_items[transaction_id] = set()
                logger.debug("Flushed items!")

        logger.debug("No items flushed")

    def __unreported_manifest_items_batch_ready_to_report(self, transaction_id):
        return (
            len(self.__transaction_completed_unreported_items[transaction_id])
            >= (
                len(self.__transaction_manifests[transaction_id])
                / self.__manifest_reporting_increments
            )
            and len(self.__transaction_completed_unreported_items[transaction_id])
            >= self.__manifest_reporting_min_batch_size
        )

    def flush_manifest_item_completions(
        self,
        dataset_id: str,
        transaction_id: str,
        manifest_items: list[str],
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        url = f"{self.__roboto_service_base_url}/v2/datasets/{dataset_id}/batch_uploads/{transaction_id}/progress"
        request_body = ReportTransactionProgressRequest(
            manifest_items=manifest_items,
        )

        with RobotoHttpExceptionParse():
            self.__http_client.put(
                url,
                data=request_body.model_dump_json(exclude_none=True),
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

    def complete_manifest_transaction(
        self,
        dataset_id: str,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        """
        Marks a transaction as 'completed', which allows the Roboto Platform to evaluate triggers
        for automatic action on incoming data. This also aids reporting on partial upload failure cases.
        """
        url = f"{self.__roboto_service_base_url}/v2/datasets/{dataset_id}/batch_uploads/{transaction_id}/complete"

        with RobotoHttpExceptionParse():
            self.__http_client.put(
                url=url,
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

    def create_single_file_upload(
        self,
        dataset_id: str,
        file_path: str,
        file_size: int,
        origination: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> typing.Tuple[str, str]:
        url = f"{self.__roboto_service_base_url}/v2/datasets/{dataset_id}/uploads"
        request_body = BeginSingleFileUploadRequest(
            origination=origination,
            file_path=file_path,
            file_size=file_size,
        )

        with RobotoHttpExceptionParse():
            response = self.__http_client.post(
                url,
                data=request_body.model_dump_json(exclude_none=True),
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        parsed_response = BeginSingleFileUploadResponse.model_validate(
            response.from_json(json_path=["data"])
        )
        return parsed_response.upload_id, parsed_response.upload_url

    def complete_single_file_upload(
        self,
        dataset_id: str,
        upload_id: str,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        url = f"{self.__roboto_service_base_url}/v2/datasets/{dataset_id}/uploads/{upload_id}/complete"

        with RobotoHttpExceptionParse():
            self.__http_client.put(
                url=url,
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )
