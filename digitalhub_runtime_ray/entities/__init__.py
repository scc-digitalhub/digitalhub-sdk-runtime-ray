# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_ray.entities.function.ray.builder import FunctionRayBuilder
from digitalhub_runtime_ray.entities.function.ray.crud import new_function_ray
from digitalhub_runtime_ray.entities.run.ray_build.builder import RunRayRunBuildBuilder
from digitalhub_runtime_ray.entities.run.ray_job.builder import RunRayRunJobBuilder
from digitalhub_runtime_ray.entities.task.ray_build.builder import TaskRayBuildBuilder
from digitalhub_runtime_ray.entities.task.ray_job.builder import TaskRayJobBuilder

function_ray_plugin = EntityPlugin(
    builder=FunctionRayBuilder,
    shortcuts=(CrudPlugin(new_function_ray),),
)

entity_plugins = (
    function_ray_plugin,
    EntityPlugin(builder=TaskRayBuildBuilder),
    EntityPlugin(builder=TaskRayJobBuilder),
    EntityPlugin(builder=RunRayRunBuildBuilder),
    EntityPlugin(builder=RunRayRunJobBuilder),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
