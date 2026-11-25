# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, TaskBuilder

from digitalhub_runtime_ray.entities._base.runtime_entity.builder import RuntimeEntityBuilderRay
from digitalhub_runtime_ray.entities._commons.enums import EntityKinds
from digitalhub_runtime_ray.entities.task.ray_build.entity import TaskRayBuild
from digitalhub_runtime_ray.entities.task.ray_build.spec import TaskSpecRayBuild


class TaskRayBuildBuilder(TaskBuilder, RuntimeEntityBuilderRay):
    """
    TaskRayBuild builder.
    """

    ENTITY_CLASS = TaskRayBuild
    ENTITY_SPEC_CLASS = TaskSpecRayBuild
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_RAY_BUILD.value
