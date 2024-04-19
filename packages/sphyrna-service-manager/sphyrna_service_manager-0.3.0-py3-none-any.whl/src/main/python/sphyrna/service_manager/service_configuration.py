"""
This module defines types and functions related to service configuration
"""

from typing import TypeVar, Mapping
from abc import ABC, abstractmethod

ConfigValue = TypeVar("ConfigValue", int, float, str, bool)


class ServiceConfiguration(ABC):
    """A configuration for a service.  Provides a named set of properties"""

    @abstractmethod
    def poperty_map(self) -> Mapping[str, ConfigValue]:
        """
        Retrieve the configuration parameters for the service
        """


class DefaultServiceConfigurationImpl(ServiceConfiguration):
    """
    A default service configuration implementation that accepts a map of
    properties in its constructor
    """

    def __init__(self, properties: Mapping[str, ConfigValue]):
        self._property_map: Mapping[str, ConfigValue] = properties

    def poperty_map(self) -> Mapping[str, ConfigValue]:
        return self._property_map


# An empty service configuration available for convenience
# pylint: disable=unused-variable
EMPTY_SERVICE_CONFIGURATION: ServiceConfiguration = DefaultServiceConfigurationImpl({})
