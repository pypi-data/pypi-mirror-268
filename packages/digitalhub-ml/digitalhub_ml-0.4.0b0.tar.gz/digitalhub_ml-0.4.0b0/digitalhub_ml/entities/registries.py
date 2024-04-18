from __future__ import annotations

from digitalhub_core.registry.registry import registry

root = "digitalhub_ml.entities"

# Projects
entity_type = "projects"
registry.project.spec.module = f"{root}.{entity_type}.spec"
registry.project.spec.class_name = "ProjectSpecMl"
registry.project.spec.parameters_validator = "ProjectParamsMl"

# Models
entity_type = "models"
for i in ["model"]:
    model_kind = i
    model_info = {
        "entity_type": entity_type,
        "spec": {
            "module": f"{root}.{entity_type}.spec",
            "class_name": f"ModelSpec{i.title()}",
            "parameters_validator": f"ModelParams{i.title()}",
        },
        "status": {
            "module": f"{root}.{entity_type}.status",
            "class_name": f"ModelStatus{i.title()}",
        },
        "metadata": {
            "module": f"{root}.{entity_type}.metadata",
            "class_name": f"ModelMetadata{i.title()}",
        },
    }
    registry.register(model_kind, model_info)
