# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_python.entities.run._base.spec import RunSpecBaseRun, RunValidatorBaseRun


class RunSpecRayRunJob(RunSpecBaseRun):
    """RunSpecRayRunJob specifications."""

    def __init__(
        self,
        task: str,
        function: str | None = None,
        workflow: str | None = None,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        source: dict | None = None,
        image: str | None = None,
        base_image: str | None = None,
        python_version: str | None = None,
        requirements: list | None = None,
        service_type: str | None = None,
        service_name: str | None = None,
        replicas: int | None = None,
        min_replicas: int | None = None,
        max_replicas: int | None = None,
        instructions: dict | None = None,
        inputs: dict | None = None,
        parameters: dict | None = None,
        init_parameters: dict | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            task,
            function,
            workflow,
            volumes,
            resources,
            envs,
            secrets,
            profile,
            source,
            image,
            base_image,
            python_version,
            requirements,
            service_type,
            service_name,
            replicas,
            instructions,
            inputs,
            parameters,
            init_parameters,
            **kwargs,
        )
        self.local_execution = False
        self.replicas = replicas
        self.min_replicas = min_replicas
        self.max_replicas = max_replicas


class RunValidatorRayRunJob(RunValidatorBaseRun):
    """RunValidatorRayRunJob validator."""

    local_execution: bool = False
    """Whether to execute the run locally instead of in the cluster."""

    replicas: int | None = None
    """Number of replicas for the run."""

    min_replicas: int | None = None
    """Minimum number of replicas for the run."""

    max_replicas: int | None = None
    """Maximum number of replicas for the run."""
