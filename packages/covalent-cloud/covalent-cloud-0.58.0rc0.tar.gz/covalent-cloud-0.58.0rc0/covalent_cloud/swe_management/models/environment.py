# Copyright 2024 Agnostiq Inc.

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseImageConfig(BaseModel):
    """
    Represents the base Docker image configuration for an environment.

    Attributes:
        base_image: The base Docker image for the environment, formatted as `<registry>/<image>:<tag>`,
                    where `:tag` is optional. This should point to a publicly accessible or private image.

        username_credentials_reference_id: Optional(str); The ID of the username secret uploaded to the Covalent Cloud via
                                            the `store_secret` function, if the Docker image is stored in a private.

        password_credentials_reference_id: Optional(str); The ID of the password uploaded to the Covalent Cloud via the
                                        `store_secret` function, if the Docker image is stored in a private registry.
    """
    base_image: str
    username_credentials_reference_id: Optional[str] = None
    password_credentials_reference_id: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class PackageProvider(Enum):
    """
    Enum representing the package provider for runtime packages to be installed in the environment.

    Values:
        SYSTEM: the OS default package manager (e.g., APT for Ubuntu, yum for CentOS, etc.).
        WGET: wget to download packages from a given URL.
        GIT: git to clone repositories as packages.
    """
    SYSTEM = "SYSTEM"
    WGET = "WGET"
    GIT = "GIT"


class RuntimePackage(BaseModel):
    """
    Defines a runtime package to be installed in the environment.

    Attributes:
        name: The name of the package. For SYSTEM providers, this is the package name. For WGET and GIT,
              this should be the URL of the artifact or repository to fetch.
        provider Optional(PackageProvider): The provider for this package. Defaults to SYSTEM if not specified.
    """
    name: str
    provider: Optional[PackageProvider] = PackageProvider.SYSTEM
    model_config = ConfigDict(from_attributes=True)


class EnvironmentRuntimeConfig(BaseModel):
    """
    Configuration for the runtime environment, including the base image and any additional packages.

    Attributes:
        image: Optional(BaseImageConfig); Configuration for the base Docker image of the environment.
    """
    image: Optional[BaseImageConfig] = None
    model_config = ConfigDict(from_attributes=True)
