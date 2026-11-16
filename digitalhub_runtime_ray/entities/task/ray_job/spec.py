# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.spec import TaskSpecFunction


class TaskSpecRayJob(TaskSpecFunction):
    """
    TaskSpecRayJob specifications.
    """

    replicas: int | None = None
    min_replicas: int | None = None
    max_replicas: int | None = None


class TaskValidatorRayJob(TaskSpecRayJob):
    """Compatibility name for the typed Ray job-task spec."""
