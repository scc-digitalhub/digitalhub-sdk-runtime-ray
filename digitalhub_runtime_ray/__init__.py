# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_ray.entities.function.ray.builder import FunctionRayBuilder
from digitalhub_runtime_ray.entities.run.ray_build.builder import RunRayRunBuildBuilder
from digitalhub_runtime_ray.entities.run.ray_job.builder import RunRayRunJobBuilder
from digitalhub_runtime_ray.entities.task.ray_build.builder import TaskRayBuildBuilder
from digitalhub_runtime_ray.entities.task.ray_job.builder import TaskRayJobBuilder

from digitalhub_runtime_ray.entities.enums import EntityKinds

entity_builders = (
    (EntityKinds.FUNCTION_RAY.value, FunctionRayBuilder),
    (EntityKinds.RUN_RAY_JOB.value, RunRayRunJobBuilder),
    (EntityKinds.RUN_RAY_BUILD.value, RunRayRunBuildBuilder),
    (EntityKinds.TASK_RAY_BUILD.value, TaskRayBuildBuilder),
    (EntityKinds.TASK_RAY_JOB.value, TaskRayJobBuilder),
)

try:
    from digitalhub_runtime_ray.runtimes.builder import (
        RuntimeRayBuilder,
    )

    runtime_builders = (
        (EntityKinds.FUNCTION_RAY.value, RuntimeRayBuilder),
        (EntityKinds.RUN_RAY_BUILD.value, RuntimeRayBuilder),
        (EntityKinds.RUN_RAY_JOB.value, RuntimeRayBuilder),
        (EntityKinds.TASK_RAY_BUILD.value, RuntimeRayBuilder),
        (EntityKinds.TASK_RAY_JOB.value, RuntimeRayBuilder),
    )
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    logger = get_logger(__name__)
    logger.debug(f"Error importing runtime builders: {e}")
    runtime_builders = ()
