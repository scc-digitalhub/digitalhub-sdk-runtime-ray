# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.function._base.spec import FunctionBaseSpec, FunctionBaseValidator

from digitalhub_runtime_ray.entities.function.ray.models import RaySourceValidator


class FunctionSpecRay(FunctionBaseSpec):
    """
    FunctionSpecRay specifications.
    """

    def __init__(
        self,
        source: dict | None = None,
        image: str | None = None,
        base_image: str | None = None,
        python_version: str | None = None,
        requirements: list | None = None,
        ray_version: str | None = None,
    ) -> None:
        super().__init__(
            source=source,
            image=image,
            base_image=base_image,
            python_version=python_version,
            requirements=requirements,
        )
        self.ray_version = ray_version


class FunctionValidatorRay(FunctionBaseValidator[RaySourceValidator]):
    """
    FunctionValidatorRay validator.
    """

    source: RaySourceValidator
    """Source code validator"""

    ray_version: str | None = None
    "Ray version"
