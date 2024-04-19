from __future__ import annotations

from digitalhub_core.registry.registry import registry

root = "digitalhub_core.entities"

# Projects
project_kind = "project"
entity_type = "projects"
project_info = {
    "entity_type": entity_type,
    "spec": {
        "module": f"{root}.{entity_type}.spec",
        "class_name": "ProjectSpec",
        "parameters_validator": "ProjectParams",
    },
    "status": {
        "module": f"{root}.{entity_type}.status",
        "class_name": "ProjectStatus",
    },
    "metadata": {
        "module": f"{root}.{entity_type}.metadata",
        "class_name": "ProjectMetadata",
    },
}
registry.register(project_kind, project_info)


# Secrets
secret_kind = "secret"
entity_type = "secrets"
secret_info = {
    "entity_type": entity_type,
    "spec": {
        "module": f"{root}.{entity_type}.spec",
        "class_name": "SecretSpec",
        "parameters_validator": "SecretParams",
    },
    "status": {
        "module": f"{root}.{entity_type}.status",
        "class_name": "SecretStatus",
    },
    "metadata": {
        "module": f"{root}.{entity_type}.metadata",
        "class_name": "SecretMetadata",
    },
}
registry.register(secret_kind, secret_info)


# Artifacts
entity_type = "artifacts"
for i in ["artifact"]:
    artifact_kind = i
    artifact_info = {
        "entity_type": entity_type,
        "spec": {
            "module": f"{root}.{entity_type}.spec",
            "class_name": f"ArtifactSpec{i.title()}",
            "parameters_validator": f"ArtifactParams{i.title()}",
        },
        "status": {
            "module": f"{root}.{entity_type}.status",
            "class_name": f"ArtifactStatus{i.title()}",
        },
        "metadata": {
            "module": f"{root}.{entity_type}.metadata",
            "class_name": f"ArtifactMetadata{i.title()}",
        },
    }
    registry.register(artifact_kind, artifact_info)
