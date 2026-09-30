# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing
from pathlib import Path

from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.generic_utils import encode_string

from digitalhub_runtime_python.entities.function.python.models import Lang

def source_check(**kwargs) -> dict:
    """
    Check source code.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    dict
        Checked source.
    """
    source: dict = kwargs.pop("source", None)
    code_src = kwargs.pop("code_src", None)
    code = kwargs.pop("code", None)
    base64 = kwargs.pop("base64", None)
    handler = kwargs.pop("handler", None)
    init_function = kwargs.pop("init_function", None)
    lang = kwargs.pop("lang", None)

    if source is not None:
        source = source.copy()
        code_src = source.pop("source", None)
        code = source.pop("code", None)
        base64 = source.pop("base64", None)
        handler = source.pop("handler", None)
        lang = source.pop("lang", None)

    kwargs["source"] = _check_params(
        code_src=code_src,
        code=code,
        base64=base64,
        handler=handler,
        lang=lang,
    )
    return kwargs


def _check_params(
    code_src: str | None = None,
    code: str | None = None,
    base64: str | None = None,
    handler: str | None = None,
    lang: str | None = None,
) -> dict:
    """
    Check source.

    Parameters
    ----------
    code_src : str
        Source code source.
    code : str
        Source code.
    base64 : str
        Source code base64.
    handler : str
        Function handler.
    lang : str
        Source code language.

    Returns
    -------
    dict
        Checked source.
    """
    source = {}

    source["handler"] = handler

    source["lang"] = lang if lang is not None else Lang.PYTHON.value

    if code_src is None and code is None and base64 is None:
        raise EntityError("Source must be provided.")

    if code_src is not None:
        source["source"] = code_src

    if base64 is not None:
        source["base64"] = base64

    if code is not None:
        source["base64"] = encode_string(code)

    return source