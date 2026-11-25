# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder
from digitalhub_runtime_python.entities.run._base.status import RunStatusBaseRun

from digitalhub_runtime_ray.entities._base.runtime_entity.builder import RuntimeEntityBuilderRay
from digitalhub_runtime_ray.entities._commons.enums import EntityKinds
from digitalhub_runtime_ray.entities.run.ray_build.entity import RunRayRunBuild
from digitalhub_runtime_ray.entities.run.ray_build.spec import RunSpecRayRunBuild


class RunRayRunBuildBuilder(RunBuilder, RuntimeEntityBuilderRay):
    """
    RunRayRunBuildBuilder runner.
    """

    ENTITY_CLASS = RunRayRunBuild
    ENTITY_SPEC_CLASS = RunSpecRayRunBuild
    ENTITY_STATUS_CLASS = RunStatusBaseRun
    ENTITY_KIND = EntityKinds.RUN_RAY_BUILD.value
