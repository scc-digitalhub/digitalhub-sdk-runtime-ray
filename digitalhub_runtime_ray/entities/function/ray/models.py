# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import ClassVar

from digitalhub.entities._mixin.source.models import HandlerSourceCode
from digitalhub_runtime_python.entities.function._base.models import Lang
from pydantic import Field


class RaySourceCode(HandlerSourceCode):
    """Source code model for Ray functions."""

    DEFAULT_LANG: ClassVar[str | None] = "python"
    lang: Lang = Field(default=Lang.PYTHON.value)


RaySourceValidator = RaySourceCode
