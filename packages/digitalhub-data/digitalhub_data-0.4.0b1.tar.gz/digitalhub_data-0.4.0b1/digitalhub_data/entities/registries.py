from __future__ import annotations

from digitalhub_core.registry.registry import registry

root = "digitalhub_data.entities"

# Projects
entity_type = "projects"
registry.project.spec.module = f"{root}.{entity_type}.spec"
registry.project.spec.class_name = "ProjectSpecData"
registry.project.spec.parameters_validator = "ProjectParamsData"

# Dataitems
entity_type = "dataitems"
for i in ["dataitem", "table", "iceberg"]:
    dataitem_kind = i
    dataitem_info = {
        "entity_type": entity_type,
        "spec": {
            "module": f"{root}.{entity_type}.spec",
            "class_name": f"DataitemSpec{i.title()}",
            "parameters_validator": f"DataitemParams{i.title()}",
        },
        "status": {
            "module": f"{root}.{entity_type}.status",
            "class_name": f"DataitemStatus{i.title()}",
        },
        "metadata": {
            "module": f"{root}.{entity_type}.metadata",
            "class_name": f"DataitemMetadata{i.title()}",
        },
    }
    registry.register(dataitem_kind, dataitem_info)
