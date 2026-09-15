# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._commons.utils import map_actions
from digitalhub.entities._mixin.runtime_entity.builder import RuntimeEntityBuilder

from digitalhub_runtime_ray.entities.enums import Actions, EntityKinds

class RuntimeEntityBuilderRay(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_RAY.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_RAY_JOB.value,
                Actions.JOB.value,
            ),
            (
                EntityKinds.TASK_RAY_BUILD.value,
                Actions.BUILD.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_RAY_JOB.value,
                Actions.JOB.value,
            ),
            (
                EntityKinds.RUN_RAY_BUILD.value,
                Actions.BUILD.value,
            ),
        ]
    )