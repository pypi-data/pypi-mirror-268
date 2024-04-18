"""
Dataitem metadata module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.metadata import Metadata


class DataitemMetadata(Metadata):
    """
    A class representing Dataitem metadata.
    """


class DataitemMetadataDataitem(DataitemMetadata):
    """
    A class representing Dataitem dataitem metadata.
    """


class DataitemMetadataTable(DataitemMetadata):
    """
    A class representing Dataitem table metadata.
    """


class DataitemMetadataIceberg(DataitemMetadata):
    """
    A class representing Dataitem iceberg metadata.
    """
