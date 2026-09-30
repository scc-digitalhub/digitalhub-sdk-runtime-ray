# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator
from digitalhub_runtime_python.entities.function.python.models import PythonVersion

from digitalhub_runtime_ray.entities.function.ray.models import RaySourceValidator


class FunctionSpecRay(FunctionSpec):
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
        super().__init__()

        self.image = image
        self.base_image = base_image
        self.python_version = python_version
        self.requirements = requirements
        self.ray_version = ray_version
        self.source = source


class FunctionValidatorRay(FunctionValidator):
    """
    FunctionValidatorRay validator.
    """

    source: RaySourceValidator
    """Source code validator"""

    python_version: PythonVersion | None = None
    "Python version"

    image: str | None = None
    "Image where the function will be executed"

    base_image: str | None = None
    "Base image used to build the image where the function will be executed"

    requirements: list[str] | str | None = None
    "Requirements list to be installed in the image where the function will be executed"

    ray_version: str | None = None
    "Ray version"
