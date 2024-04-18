from __future__ import annotations

from digitalhub_data.entities.runs.status import ENTITY_FUNC, RunStatusData
from digitalhub_ml.entities.models.crud import get_model_from_key

ENTITY_FUNC["models"] = get_model_from_key


class RunStatusMl(RunStatusData):
    """
    A class representing a run status.
    """
