# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.function._base.builder import FunctionBaseBuilder

from digitalhub_runtime_ray.entities._base.runtime_entity.builder import RuntimeEntityBuilderRay
from digitalhub_runtime_ray.entities._commons.enums import EntityKinds
from digitalhub_runtime_ray.entities.function.ray.entity import FunctionRay
from digitalhub_runtime_ray.entities.function.ray.spec import FunctionSpecRay, FunctionValidatorRay
from digitalhub_runtime_ray.entities.function.ray.status import FunctionStatusRay

from digitalhub_runtime_ray.entities.function.ray.utils import source_check

class FunctionRayBuilder(FunctionBaseBuilder, RuntimeEntityBuilderRay):
    """
    Ray Python function builder.
    """

    ENTITY_CLASS = FunctionRay
    ENTITY_SPEC_CLASS = FunctionSpecRay
    ENTITY_SPEC_VALIDATOR = FunctionValidatorRay
    ENTITY_STATUS_CLASS = FunctionStatusRay
    ENTITY_KIND = EntityKinds.FUNCTION_RAY.value

    def _prepare_source(self, source: dict) -> dict:
        return source_check(source=source)["source"]

    def _prepare_kwargs(self, kwargs: dict) -> dict:
        return source_check(**kwargs)
