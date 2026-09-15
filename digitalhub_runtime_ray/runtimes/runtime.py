# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.runtimes.runtime import RuntimePython
from digitalhub.utils.logger.logger import get_logger

logger = get_logger(__file__)


class RuntimeRay(RuntimePython):
    """
    Runtime Ray class.
    """
