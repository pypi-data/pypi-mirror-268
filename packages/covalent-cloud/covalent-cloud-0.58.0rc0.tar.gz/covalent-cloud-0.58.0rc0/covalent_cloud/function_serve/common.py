# Copyright 2024 Agnostiq Inc.

import time
from enum import Enum
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from covalent_cloud.function_serve.models import DeploymentInfo

__all__ = [
    "DEPLOY_ELECTRON_PREFIX",
    "SupportedMethods",
    "ServiceStatus",
    "rename",
    "wait_for_deployment_to_be_active",
]


DEPLOY_ELECTRON_PREFIX = "#__deploy_electron__#"

# 120 retries * 30 seconds = 60 minutes
ACTIVE_DEPLOYMENT_RETRIES = 120
ACTIVE_DEPLOYMENT_POLL_INTERVAL = 30


class SupportedMethods(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class ServiceStatus(str, Enum):
    """Possible statuses for a function service."""

    NEW_OBJECT = "NEW_OBJECT"
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ERROR = "ERROR"


def rename(name):
    def decorator(fn):
        fn.__name__ = name
        return fn

    return decorator


def wait_for_deployment_to_be_active(
    deployment_info: "DeploymentInfo", verbose=False
) -> Union[None, "DeploymentInfo"]:
    retries_done = 0
    while (
        deployment_info.status.name
        not in [
            ServiceStatus.ACTIVE.name,
            ServiceStatus.INACTIVE.name,
        ]
        and retries_done < ACTIVE_DEPLOYMENT_RETRIES
    ):
        if verbose:
            print("Deployment info is: ")
            print(deployment_info.model_dump())

        time.sleep(ACTIVE_DEPLOYMENT_POLL_INTERVAL)

        deployment_info.reload()
        retries_done += 1

    if deployment_info.status.name == ServiceStatus.ACTIVE.name:
        return deployment_info

    if deployment_info.status.name == ServiceStatus.INACTIVE.name:
        raise RuntimeError("Deployment is inactive")

    raise RuntimeError(
        f"Timed out after {ACTIVE_DEPLOYMENT_RETRIES * ACTIVE_DEPLOYMENT_POLL_INTERVAL / 60} "
        "minutes while waiting for the deployment to become active"
    )
