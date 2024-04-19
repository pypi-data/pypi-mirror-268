#  Copyright (c) 2024 Roboto Technologies, Inc.


"""
Data transfer objects which define the contract of various file operations. These are intended to be used with little
or no modification as input to all layers of SDK and service side code through persistence.
"""


import typing

import pydantic

from roboto.sentinels import NotSet, NotSetType
from roboto.updates import MetadataChangeset


class UpdateFileRecordRequest(pydantic.BaseModel):
    description: typing.Optional[typing.Union[str, NotSetType]] = NotSet
    metadata_changeset: typing.Union[MetadataChangeset, NotSetType] = NotSet

    model_config = pydantic.ConfigDict(
        extra="forbid", json_schema_extra=NotSetType.openapi_schema_modifier
    )
