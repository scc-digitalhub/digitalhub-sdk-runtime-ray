# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    ExecutableActions,
    FunctionBuilder,
    RunBuilder,
    SourceBuilderMixin,
    Status,
    Task,
    TaskBuilder,
)
from digitalhub_runtime_python.entities.function.python.entity import FunctionPython
from digitalhub_runtime_python.entities.run._base.entity import RunBaseBuildRun
from digitalhub_runtime_python.entities.run._base.status import RunStatusBaseRun
from digitalhub_runtime_python.entities.run.python_job.entity import RunPythonRunJob

from digitalhub_runtime_ray.entities._commons.enums import Actions, EntityKinds
from digitalhub_runtime_ray.entities.function.ray.crud import new_function_ray
from digitalhub_runtime_ray.entities.function.ray.spec import FunctionSpecRay
from digitalhub_runtime_ray.entities.run.ray_build.spec import RunSpecRayRunBuild
from digitalhub_runtime_ray.entities.run.ray_job.spec import RunSpecRayRunJob
from digitalhub_runtime_ray.entities.task.ray_build.spec import TaskSpecRayBuild
from digitalhub_runtime_ray.entities.task.ray_job.spec import TaskSpecRayJob

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_RAY_BUILDER = "digitalhub_runtime_ray.runtimes.builder:RuntimeRayBuilder"

ray = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_RAY,
        FunctionPython,
        FunctionSpecRay,
        Status,
        base=FunctionBuilder,
        mixins=(SourceBuilderMixin,),
        shortcuts=(CrudPlugin(new_function_ray),),
    ),
    actions={
        Actions.JOB: Action(
            task=BuilderDef(EntityKinds.TASK_RAY_JOB, Task, TaskSpecRayJob, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_RAY_JOB, RunPythonRunJob, RunSpecRayRunJob, RunStatusBaseRun, base=RunBuilder
            ),
        ),
        ExecutableActions.BUILD: Action(
            task=BuilderDef(EntityKinds.TASK_RAY_BUILD, Task, TaskSpecRayBuild, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_RAY_BUILD, RunBaseBuildRun, RunSpecRayRunBuild, RunStatusBaseRun, base=RunBuilder
            ),
        ),
    },
    runtime_builder=RUNTIME_RAY_BUILDER,
)

entity_plugins = (*ray.plugins(),)
