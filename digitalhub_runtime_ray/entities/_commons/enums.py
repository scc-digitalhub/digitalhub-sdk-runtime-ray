# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_RAY = "ray"
    TASK_RAY_BUILD = "ray+build"
    TASK_RAY_JOB = "ray+job"
    RUN_RAY_BUILD = "ray+build:run"
    RUN_RAY_JOB = "ray+job:run"


class Actions(Enum):
    """
    Task actions.
    """

    BUILD = "build"
    JOB = "job"
