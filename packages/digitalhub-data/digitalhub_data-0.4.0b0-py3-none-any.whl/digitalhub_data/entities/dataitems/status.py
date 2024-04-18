"""
DataitemStatus class module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.status import Status


class DataitemStatus(Status):
    """
    Status class for dataitem entities.
    """

    def __init__(self, state: str, message: str | None = None, preview: dict | None = None) -> None:
        """
        Constructor.

        Parameters
        ----------
        preview : dict
            Preview of the data.
        """
        super().__init__(state, message)
        self.preview = preview


class DataitemStatusDataitem(DataitemStatus):
    """
    Status class for dataitem dataitem entities.
    """


class DataitemStatusTable(DataitemStatus):
    """
    Status class for dataitem table entities.
    """


class DataitemStatusIceberg(DataitemStatus):
    """
    Status class for dataitem iceberg entities.
    """
