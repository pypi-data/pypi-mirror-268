"""
Model operations module.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_list, api_ctx_read, api_ctx_update
from digitalhub_core.utils.generic_utils import parse_entity_key
from digitalhub_core.utils.io_utils import read_yaml
from digitalhub_ml.entities.models.entity import model_from_dict, model_from_parameters

if typing.TYPE_CHECKING:
    from digitalhub_ml.entities.models.entity import Model


ENTITY_TYPE = "models"


def create_model(**kwargs) -> Model:
    """
    Create a new Model instance with the specified parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Model
        An instance of the created model.
    """
    return model_from_parameters(**kwargs)


def create_model_from_dict(obj: dict) -> Model:
    """
    Create a new Model instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create object from.

    Returns
    -------
    Model
        Model object.
    """
    check_context(obj.get("project"))
    return model_from_dict(obj)


def new_model(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    **kwargs,
) -> Model:
    """
    Create a new Model instance with the specified parameters.

    Parameters
    ----------
    project : str
        A string representing the project associated with this model.
    name : str
        The name of the model.
    kind : str
        Kind of the object.
    uuid : str
        ID of the object in form of UUID.
    description : str
        A description of the model.
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
    Model
        An instance of the created model.
    """
    obj = create_model(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        **kwargs,
    )
    obj.save()
    return obj


def get_model(project: str, entity_name: str | None = None, entity_id: str | None = None, **kwargs) -> Model:
    """
    Retrieves model details from backend.

    Parameters
    ----------

    project : str
        Project name.
    name : str
        The name of the model.
    uuid : str
        ID of the object in form of UUID.

    Returns
    -------
    Model
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
    return create_model_from_dict(obj)


def get_model_from_key(key: str) -> Model:
    """
    Get model from key.

    Parameters
    ----------
    key : str
        Key of the model.
        It's format is store://<project>/models/<kind>/<name>:<uuid>.
    """
    project, _, _, _, uuid = parse_entity_key(key)
    return get_model(project, entity_id=uuid)


def import_model(file: str) -> Model:
    """
    Import an Model object from a file using the specified file path.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Model
        Object instance.
    """
    obj: dict = read_yaml(file)
    return create_model_from_dict(obj)


def delete_model(
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


def update_model(entity: Model, **kwargs) -> dict:
    """
    Update object in backend.

    Parameters
    ----------
    entity : Model
        The object to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(entity.project, ENTITY_TYPE, entity_id=entity.id)
    return get_context(entity.project).update_object(api, entity.to_dict(), **kwargs)


def list_models(project: str, **kwargs) -> list[dict]:
    """
    List all objects from backend.

    Parameters
    ----------
    project : str
        Project name.

    Returns
    -------
    list[dict]
        List of models dict representations.
    """
    api = api_ctx_list(project, ENTITY_TYPE)
    return get_context(project).list_objects(api, **kwargs)
