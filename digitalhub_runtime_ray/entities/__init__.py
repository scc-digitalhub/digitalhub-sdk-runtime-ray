# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_ray.entities.function.ray.builder import FunctionRayBuilder
from digitalhub_runtime_ray.entities.function.ray.crud import new_function_ray
from digitalhub_runtime_ray.entities.run.ray_build.builder import RunRayRunBuildBuilder
from digitalhub_runtime_ray.entities.run.ray_job.builder import RunRayRunJobBuilder
from digitalhub_runtime_ray.entities.task.ray_build.builder import TaskRayBuildBuilder
from digitalhub_runtime_ray.entities.task.ray_job.builder import TaskRayJobBuilder

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_RAY_BUILDER = "digitalhub_runtime_ray.runtimes.builder:RuntimeRayBuilder"

function_ray_plugin = EntityPlugin(
    builder=FunctionRayBuilder,
    shortcuts=(CrudPlugin(new_function_ray),),
    runtime_builder=RUNTIME_RAY_BUILDER,
)

entity_plugins = (
    function_ray_plugin,
    EntityPlugin(builder=TaskRayBuildBuilder, runtime_builder=RUNTIME_RAY_BUILDER),
    EntityPlugin(builder=TaskRayJobBuilder, runtime_builder=RUNTIME_RAY_BUILDER),
    EntityPlugin(builder=RunRayRunBuildBuilder, runtime_builder=RUNTIME_RAY_BUILDER),
    EntityPlugin(builder=RunRayRunJobBuilder, runtime_builder=RUNTIME_RAY_BUILDER),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
