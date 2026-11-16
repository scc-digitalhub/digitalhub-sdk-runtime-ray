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

try:
    from digitalhub_runtime_ray.runtimes.builder import RuntimeRayBuilder
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    get_logger(__name__).debug(f"Error importing runtime builder: {e}")
    RuntimeRayBuilder = None

function_ray_plugin = EntityPlugin(
    builder=FunctionRayBuilder,
    shortcuts=(CrudPlugin(new_function_ray),),
    runtime_builder=RuntimeRayBuilder,
)

entity_plugins = (
    function_ray_plugin,
    EntityPlugin(builder=TaskRayBuildBuilder, runtime_builder=RuntimeRayBuilder),
    EntityPlugin(builder=TaskRayJobBuilder, runtime_builder=RuntimeRayBuilder),
    EntityPlugin(builder=RunRayRunBuildBuilder, runtime_builder=RuntimeRayBuilder),
    EntityPlugin(builder=RunRayRunJobBuilder, runtime_builder=RuntimeRayBuilder),
)  # SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
