# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.run._base.spec import RunSpecPython


class RunSpecRayRunJob(RunSpecPython):
    """RunSpecRayRunJob specifications."""

    local_execution: bool = False


class RunValidatorRayRunJob(RunSpecRayRunJob):
    """Compatibility name for the typed Ray job-run spec."""
