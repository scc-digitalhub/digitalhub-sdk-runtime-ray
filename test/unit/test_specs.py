# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from digitalhub.entities._constructors.spec import build_spec
from pydantic import ValidationError

from digitalhub_runtime_ray.entities.function.ray.models import RaySourceValidator
from digitalhub_runtime_ray.entities.function.ray.spec import FunctionSpecRay
from digitalhub_runtime_ray.entities.run.ray_build.spec import RunSpecRayRunBuild
from digitalhub_runtime_ray.entities.run.ray_job.spec import RunSpecRayRunJob
from digitalhub_runtime_ray.entities.task.ray_build.spec import TaskSpecRayBuild
from digitalhub_runtime_ray.entities.task.ray_job.spec import TaskSpecRayJob


def test_ray_function_spec_validates_nested_source_and_runtime_fields():
    spec = build_spec(
        FunctionSpecRay,
        source={"handler": "predict", "code": "def predict(): pass"},
        ray_version="2.40.0",
    )

    assert isinstance(spec.source, RaySourceValidator)
    assert spec.source.handler == "predict"
    assert spec.ray_version == "2.40.0"

    with pytest.raises(TypeError, match="unknown_option"):
        build_spec(FunctionSpecRay, source={"handler": "predict"}, unknown_option=True)


def test_ray_task_specs_validate_action_fields():
    build = build_spec(TaskSpecRayBuild, function="function", instructions=["install ray"])
    job = build_spec(TaskSpecRayJob, function="function", replicas=2, min_replicas=1, max_replicas=4)

    assert build.instructions == ["install ray"]
    assert job.replicas == 2
    assert job.min_replicas == 1
    assert job.max_replicas == 4

    with pytest.raises(ValidationError):
        build_spec(TaskSpecRayBuild, function="function", instructions=["valid", 3])


def test_ray_run_specs_keep_run_fields_separate_from_task_build_fields():
    run = build_spec(
        RunSpecRayRunJob,
        task="ray+job://task",
        local_execution=True,
        inputs={"sample": "value"},
        parameters={"threshold": 0.5},
    )

    assert run.local_execution is True
    assert run.inputs == {"sample": "value"}
    assert run.parameters == {"threshold": 0.5}

    with pytest.raises(TypeError, match="replicas"):
        build_spec(RunSpecRayRunJob, task="ray+job://task", replicas=2)

    with pytest.raises(TypeError, match="service_type"):
        build_spec(RunSpecRayRunJob, task="ray+job://task", service_type="ClusterIP")

    with pytest.raises(TypeError, match="instructions"):
        build_spec(RunSpecRayRunBuild, task="ray+build://task", instructions=["install ray"])
