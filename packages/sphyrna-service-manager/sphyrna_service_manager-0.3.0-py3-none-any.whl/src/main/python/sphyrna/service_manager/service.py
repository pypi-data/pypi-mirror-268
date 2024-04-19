"""
    service module defines a Service class/interface
"""

from typing import TypeVar
from abc import ABC, abstractmethod

# pylint is reporting this as unused, but it's used as a bound in the TypeVar defintion below
# pylint: disable=unused-variable,unused-import
from sphyrna.service_manager.service_configuration import ServiceConfiguration

# pylint is reporting this as unused, but it's imported by other files
# pylint: disable=unused-variable
ServiceT = TypeVar("ServiceT", bound="Service")
ConfigurationT = TypeVar("ConfigurationT", bound="ServiceConfiguration")


# mypy does not yet support PEP 695 generics
class Service[ConfigurationT](ABC):  # type: ignore[valid-type]
    """A Service is a predefined component of functionality with a lifecycle managed by the ServiceManger."""

    @abstractmethod
    def init(self, configuration: ConfigurationT) -> None:
        """Initialize the service instance

        Args:
            configuration (C): Service level configuration"""

    @abstractmethod
    def start(self) -> None:
        """Start the service instances"""

    @abstractmethod
    def stop(self) -> None:
        """Stop the service instance"""

    @abstractmethod
    def destroy(self) -> None:
        """Destroy the service instance.  Can be used to clean up memory or other resources"""


# mypy does not yet support PEP 695 generics
# pylint is reporting this as unused, because it's used by clients
# pylint: disable=unused-variable
class BaseService[ConfigurationT](Service):  # type: ignore[valid-type]
    """
    Base instance of a Service which is a noop for all methods.  Extend to create a new service and
    implement the methods that are required
    """

    def init(self, configuration: ConfigurationT) -> None:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def destroy(self) -> None:
        pass


# pylint is reporting this as unused, even thought it is imported elsewhere
# pylint: disable=unused-variable
class ServiceException(Exception):
    """
    Service API Exception
    """
