from __future__ import annotations

from digitalhub_core.entities._base.metadata import MetadataRegistry
from digitalhub_core.entities._base.spec import SpecRegistry
from digitalhub_core.entities._base.status import StatusRegistry

metadata_registry = MetadataRegistry()
spec_registry = SpecRegistry()
status_registry = StatusRegistry()

spec_registry.register("project", "digitalhub_data.entities.projects.spec", "ProjectSpecData", "ProjectParamsData")

for i in ["dataitem", "table", "iceberg"]:
    root = "digitalhub_data.entities.dataitems"
    metadata_registry.register(i, f"{root}.metadata", f"DataitemMetadata{i.title()}")
    spec_registry.register(i, f"{root}.spec", f"DataitemSpec{i.title()}", f"DataitemParams{i.title()}")
    status_registry.register(i, f"{root}.status", f"DataitemStatus{i.title()}")
