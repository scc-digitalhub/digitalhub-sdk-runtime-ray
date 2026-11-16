# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecFunction


class TaskSpecRayBuild(TaskSpecFunction):
    """TaskSpecRayBuild specifications."""

    instructions: list[str] | None = None


class TaskValidatorRayBuild(TaskSpecRayBuild):
    """Compatibility name for the typed Ray build-task spec."""
