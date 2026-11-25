# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from digitalhub.plugins import build_spec
from pydantic import ValidationError

from digitalhub_runtime_ray.entities._mixin.execution.spec import RayJobSpecMixin
from digitalhub_runtime_ray.entities.function.ray.builder import FunctionRayBuilder
from digitalhub_runtime_ray.entities.function.ray.models import RaySourceCode
from digitalhub_runtime_ray.entities.function.ray.spec import FunctionSpecRay
from digitalhub_runtime_ray.entities.run.ray_build.spec import RunSpecRayRunBuild
from digitalhub_runtime_ray.entities.run.ray_job.spec import RunSpecRayRunJob
from digitalhub_runtime_ray.entities.task.ray_build.spec import TaskSpecRayBuild
from digitalhub_runtime_ray.entities.task.ray_job.spec import TaskSpecRayJob


def test_ray_function_spec_validates_nested_source_and_runtime_fields():
    spec = build_spec(
        FunctionSpecRay,
        source={"handler": "predict", "code": "def predict(): pass"},
        init_function="initialize",
        ray_version="2.40.0",
    )

    assert isinstance(spec.source, RaySourceCode)
    assert spec.source.handler == "predict"
    assert spec.init_function == "initialize"
    assert spec.ray_version == "2.40.0"

    with pytest.raises(TypeError, match="unknown_option"):
        build_spec(FunctionSpecRay, source={"handler": "predict"}, unknown_option=True)


def test_ray_builder_preserves_init_function_on_outer_spec():
    builder = FunctionRayBuilder()

    function = builder.build(
        kind=builder.ENTITY_KIND,
        project="project",
        name="function",
        code="def predict(): pass",
        handler="predict",
        init_function="initialize",
    )

    assert function.spec.source.base64 == "ZGVmIHByZWRpY3QoKTogcGFzcw=="
    assert function.spec.init_function == "initialize"


def test_ray_task_specs_validate_action_fields():
    build = build_spec(TaskSpecRayBuild, function="function", instructions=["install ray"])
    job = build_spec(TaskSpecRayJob, function="function", replicas=2, min_replicas=1, max_replicas=4)

    assert build.instructions == ["install ray"]
    assert job.replicas == 2
    assert job.min_replicas == 1
    assert job.max_replicas == 4

    with pytest.raises(ValidationError):
        build_spec(TaskSpecRayBuild, function="function", instructions=["valid", 3])


def test_ray_job_spec_mixin_has_one_runtime_owner():
    assert RayJobSpecMixin in TaskSpecRayJob.__mro__
    assert RayJobSpecMixin in RunSpecRayRunJob.__mro__


def test_ray_run_specs_keep_run_fields_separate_from_task_build_fields():
    run = build_spec(
        RunSpecRayRunJob,
        function="function",
        task="ray+job://task",
        local_execution=True,
        inputs={"sample": "value"},
        parameters={"threshold": 0.5},
        replicas=2,
        min_replicas=1,
        max_replicas=4,
    )

    assert run.local_execution is True
    assert run.inputs == {"sample": "value"}
    assert run.parameters == {"threshold": 0.5}
    assert run.replicas == 2
    assert run.min_replicas == 1
    assert run.max_replicas == 4

    with pytest.raises(TypeError, match="service_type"):
        build_spec(RunSpecRayRunJob, function="function", task="ray+job://task", service_type="ClusterIP")

    with pytest.raises(TypeError, match="instructions"):
        build_spec(RunSpecRayRunJob, function="function", task="ray+job://task", instructions=["install ray"])

    build = build_spec(
        RunSpecRayRunBuild,
        function="function",
        task="ray+build://task",
        instructions=["install ray"],
    )
    assert build.instructions == ["install ray"]

    with pytest.raises(TypeError, match="replicas"):
        build_spec(RunSpecRayRunBuild, function="function", task="ray+build://task", replicas=2)
