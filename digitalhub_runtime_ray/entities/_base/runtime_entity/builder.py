# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RuntimeEntityBuilder, map_actions

from digitalhub_runtime_ray.entities._commons.enums import Actions, EntityKinds


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
