"""
Dataitem module.
"""
from __future__ import annotations

import typing

from digitalhub_core.entities._builders.metadata import build_metadata
from digitalhub_core.entities._builders.spec import build_spec
from digitalhub_core.entities._builders.status import build_status
from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.generic_utils import build_uuid

if typing.TYPE_CHECKING:
    from digitalhub_data.entities.dataitems.entity._base import Dataitem

# Manage class mapper
cls_mapper = {}
try:
    from digitalhub_data.entities.dataitems.entity.dataitem import DataitemDataitem

    cls_mapper["dataitem"] = DataitemDataitem
except ImportError:
    ...
try:
    from digitalhub_data.entities.dataitems.entity.table import DataitemTable

    cls_mapper["table"] = DataitemTable
except ImportError:
    ...
try:
    from digitalhub_data.entities.dataitems.entity.iceberg import DataitemIceberg

    cls_mapper["iceberg"] = DataitemIceberg
except ImportError:
    pass


def _choose_dataitem_type(kind: str) -> type[Dataitem]:
    """
    Choose class based on kind.

    Parameters
    ----------
    kind : str
        Kind of the dataitem.

    Returns
    -------
    type[Dataitem]
        Class of the dataitem.
    """
    try:
        return cls_mapper[kind]
    except KeyError:
        raise EntityError(f"Unknown dataitem kind: {kind}")


def dataitem_from_parameters(
    project: str,
    name: str,
    kind: str,
    path: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    **kwargs,
) -> Dataitem:
    """
    Create a new object instance.

    Parameters
    ----------
    project : str
        Project name.
    name : str
        Name that identifies the object.
    kind : str
        Kind of the object.
    path : str
        Path to the dataitem on local file system or remote storage.
    uuid : str
        ID of the object in form of UUID.
    description : str
        Description of the object.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Dataitem
       Object instance.
    """
    uuid = build_uuid(uuid)
    metadata = build_metadata(
        kind,
        project=project,
        name=name,
        version=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
    )

    spec = build_spec(
        kind,
        path=path,
        **kwargs,
    )
    status = build_status(kind)
    cls = _choose_dataitem_type(kind)
    return cls(
        project=project,
        name=name,
        uuid=uuid,
        kind=kind,
        metadata=metadata,
        spec=spec,
        status=status,
    )


def dataitem_from_dict(obj: dict) -> Dataitem:
    """
    Create dataitem from dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Dataitem
        Dataitem object.
    """
    kind = obj.get("kind")
    cls = _choose_dataitem_type(kind)
    return cls.from_dict(obj, validate=False)
