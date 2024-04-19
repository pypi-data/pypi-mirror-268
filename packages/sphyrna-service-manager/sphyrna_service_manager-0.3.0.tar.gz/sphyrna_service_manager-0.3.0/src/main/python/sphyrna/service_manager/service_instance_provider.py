"""
This module defines types and functions related to a service instance provider, 
which is used to create an instance of a service class
"""

from abc import ABC, abstractmethod

from sphyrna.service_manager.service import ServiceT


# mypy does not yet support PEP 695 generics
class ServiceInstanceProvider[ServiceT](ABC):  # type: ignore[valid-type]
    """
    A ServiceInstanceProvider creates a single instance of a service.
    """

    @abstractmethod
    def create_service_instance(self) -> ServiceT:
        """
        Create a Service instance
        """


# pylint isn't handling generics in the way I'm specifing them
# pylint: disable=E1136,unused-variable
class DefaultServiceInstanceProviderImpl(ServiceInstanceProvider[ServiceT]):
    """
    DefaultServiceInstanceProviderImpl is a service provider that simply invokes the provided service constructor to
    create the service instance
    """

    def __init__(self, service_class: type):
        self.service_class = service_class

    def create_service_instance(self) -> ServiceT:
        """
        Create an instance of the service class
        """
        return self.service_class()
