"""
Run base specification module.
"""
from __future__ import annotations

from digitalhub_data.entities.runs.spec import ENTITY_FUNC, RunParamsData, RunSpecData
from digitalhub_ml.entities.models.crud import get_model_from_key

ENTITY_FUNC["models"] = get_model_from_key


class RunSpecMl(RunSpecData):
    """Run specification."""


class RunParamsMl(RunParamsData):
    """
    Run parameters.
    """
