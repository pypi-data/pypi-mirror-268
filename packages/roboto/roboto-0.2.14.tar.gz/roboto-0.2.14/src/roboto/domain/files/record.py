import datetime
import enum
import typing
import urllib.parse

import pydantic


class FileStatus(str, enum.Enum):
    Reserved = "reserved"
    Available = "available"
    Deleted = "deleted"


class IngestionStatus(str, enum.Enum):
    NotIngested = "not_ingested"
    Ingested = "ingested"


class FileRecord(pydantic.BaseModel):
    association_id: (
        str  # e.g. dataset_id, collection_id, etc.; GSI PK of "association_id" index.
    )
    file_id: str  # Table PK
    modified: datetime.datetime  # Persisted as ISO 8601 string in UTC
    relative_path: (
        str  # path relative to some common prefix. Used as local path when downloaded.
    )
    size: int  # bytes
    org_id: str
    uri: str  # GSI PK of "uri" index; GSI SK of "association_id" index
    status: FileStatus = FileStatus.Available
    upload_id: str = "NO_ID"  # Defaulted for backwards compatability
    origination: str = ""  # Defaulted for compatibility
    created_by: str = ""
    tags: list[str] = pydantic.Field(default_factory=list)
    metadata: dict[str, typing.Any] = pydantic.Field(default_factory=dict)
    description: typing.Optional[str] = None
    ingestion_status: IngestionStatus = IngestionStatus.NotIngested

    @property
    def bucket(self) -> str:
        parsed_uri = urllib.parse.urlparse(self.uri)
        return parsed_uri.netloc

    @property
    def key(self) -> str:
        parsed_uri = urllib.parse.urlparse(self.uri)
        return parsed_uri.path.lstrip("/")
