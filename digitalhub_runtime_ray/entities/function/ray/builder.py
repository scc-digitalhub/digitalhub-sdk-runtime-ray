# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status
from digitalhub_runtime_python.entities.function._base.builder import FunctionBaseBuilder

from digitalhub_runtime_ray.entities._base.runtime_entity.builder import RuntimeEntityBuilderRay
from digitalhub_runtime_ray.entities._commons.enums import EntityKinds
from digitalhub_runtime_ray.entities.function.ray.entity import FunctionRay
from digitalhub_runtime_ray.entities.function.ray.spec import FunctionSpecRay


class FunctionRayBuilder(FunctionBaseBuilder, RuntimeEntityBuilderRay):
    """
    Ray Python function builder.
    """

    ENTITY_CLASS = FunctionRay
    ENTITY_SPEC_CLASS = FunctionSpecRay
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_RAY.value
