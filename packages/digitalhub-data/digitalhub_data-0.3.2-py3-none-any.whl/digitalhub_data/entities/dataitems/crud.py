"""
Module for performing operations on Dataitem objects.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.generic_utils import parse_entity_key
from digitalhub_core.utils.io_utils import read_yaml
from digitalhub_data.entities.dataitems.builder import dataitem_from_dict, dataitem_from_parameters

if typing.TYPE_CHECKING:
    from digitalhub_data.entities.dataitems.entity._base import Dataitem


ENTITY_TYPE = "dataitems"


def create_dataitem(**kwargs) -> Dataitem:
    """
    Create a new data item with the provided parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Dataitem
        Object instance.
    """
    return dataitem_from_parameters(**kwargs)


def create_dataitem_from_dict(obj: dict) -> Dataitem:
    """
    Create a new Dataitem instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Dataitem
        Dataitem object.
    """
    check_context(obj.get("project"))
    return dataitem_from_dict(obj)


def new_dataitem(
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
    obj = create_dataitem(
        project=project,
        name=name,
        kind=kind,
        path=path,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        **kwargs,
    )
    obj.save()
    return obj


def get_dataitem(project: str, entity_name: str | None = None, entity_id: str | None = None, **kwargs) -> Dataitem:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_name : str
        Entity name.
    entity_id : str
        Entity ID.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    Dataitem
        Object instance.
    """
    if (entity_id is None) and (entity_name is None):
        raise ValueError("Either entity_name or entity_id must be provided.")

    context = get_context(project)

    if entity_name is not None:
        params = kwargs.get("params", {})
        if params is None or not params:
            kwargs["params"] = {}

        api = api_ctx_list(project, ENTITY_TYPE)
        kwargs["params"]["name"] = entity_name
        obj = context.list_objects(api, **kwargs)[0]
    else:
        api = api_ctx_read(project, ENTITY_TYPE, entity_id)
        obj = context.read_object(api, **kwargs)
    return create_dataitem_from_dict(obj)


def get_dataitem_from_key(key: str) -> Dataitem:
    """
    Get dataitem from key.

    Parameters
    ----------
    key : str
        Key of the dataitem.
        It's format is store://<project>/dataitems/<kind>/<name>:<uuid>.
    """
    project, _, _, _, uuid = parse_entity_key(key)
    return get_dataitem(project, entity_id=uuid)


def import_dataitem(file: str) -> Dataitem:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Dataitem
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_dataitem_from_dict(obj)


def delete_dataitem(
    project: str,
    entity_name: str | None = None,
    entity_id: str | None = None,
    delete_all_versions: bool = False,
    **kwargs,
) -> dict:
    """
    Delete object from backend.

    Parameters
    ----------
    project : str
        Project name.
    entity_name : str
        Entity name.
    entity_id : str
        Entity ID.
    delete_all_versions : bool
        Delete all versions of the named entity. Entity name is required.
    **kwargs : dict
        Parameters to pass to the API call.

    Returns
    -------
    dict
        Response from backend.
    """
    if (entity_id is None) and (entity_name is None):
        raise ValueError("Either entity_name or entity_id must be provided.")

    context = get_context(project)

    params = kwargs.get("params", {})
    if params is None or not params:
        kwargs["params"] = {}

    if entity_id is not None:
        api = api_ctx_delete(project, ENTITY_TYPE, entity_id)
    else:
        kwargs["params"]["name"] = entity_name
        api = api_ctx_list(project, ENTITY_TYPE)
        if delete_all_versions:
            return context.delete_object(api, **kwargs)
        obj = context.list_objects(api, **kwargs)[0]
        entity_id = obj["id"]

    api = api_ctx_delete(project, ENTITY_TYPE, entity_id)
    return context.delete_object(api, **kwargs)


def update_dataitem(entity: Dataitem, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Dataitem
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity_id=entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_dataitems(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of dataitems dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
