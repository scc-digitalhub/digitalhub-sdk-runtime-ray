# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.spec import Spec


class RayJobSpecMixin(Spec):
    """Scaling fields shared by Ray job tasks and runs."""

    replicas: int | None = None
    min_replicas: int | None = None
    max_replicas: int | None = None
