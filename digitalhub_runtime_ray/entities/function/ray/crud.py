# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_ray.entities.function.ray.builder import FunctionRayBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_ray.entities.function.ray.entity import FunctionRay


def new_function_ray(
    project: str,
    name: str,
    source: dict | None = None,
    code: str | None = None,
    code_src: str | None = None,
    base64: str | None = None,
    handler: str | None = None,
    init_function: str | None = None,
    lang: str | None = None,
    image: str | None = None,
    base_image: str | None = None,
    python_version: str | None = None,
    requirements: list[str] | str | None = None,
    ray_version: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionRay:
    """Create a Ray function entity."""
    return new_function(
        project=project,
        name=name,
        kind=FunctionRayBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        source=source,
        code=code,
        code_src=code_src,
        base64=base64,
        handler=handler,
        init_function=init_function,
        lang=lang,
        image=image,
        base_image=base_image,
        python_version=python_version,
        requirements=requirements,
        ray_version=ray_version,
    )
