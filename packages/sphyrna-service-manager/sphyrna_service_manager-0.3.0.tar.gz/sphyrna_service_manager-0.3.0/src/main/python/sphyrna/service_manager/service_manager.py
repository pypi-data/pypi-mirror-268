"""
This module defines types and functions related to a service manager, 
which is used by clients to retrieve service instances
"""

from sphyrna.service_manager.service import ConfigurationT, ServiceT
from sphyrna.service_manager.service_configuration import EMPTY_SERVICE_CONFIGURATION
from sphyrna.service_manager.service_manager_strategy import (
    ConfigServiceManagerStrategy,
    ServiceManagerStrategy,
)


class ServiceManager:
    """
    The ServiceManager is used to manage and retrieve services.  It's a proxy to
    a ServiceManagerStrategy implementation, which is used to modify the
    ServiceManager behavior.  The static proxy simplifies client code
    """

    _service_manager_strategy: ServiceManagerStrategy = ConfigServiceManagerStrategy()

    @classmethod
    def get_service(
        cls, name: str, config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION
    ) -> ServiceT:
        """
        Retrieve a service.

        An optional config may be supplied for service instance level
        configuration.  This must be supported by the associated
        ServiceLifecycleManager
        """

        # pylint isn't handling generics in the way I'm specifing them
        # pylint: disable=E1136
        return ServiceManager._service_manager_strategy.get_service(name, config)

    @classmethod
    def is_service_defined(cls, name: str) -> bool:
        """
        Determine if a service with the specified name has been defined
        """
        return ServiceManager._service_manager_strategy.is_service_defined(name)

    @classmethod
    def shutdown(cls) -> None:
        """
        Shutdown the ServiceManager and all associated services
        """
        ServiceManager._service_manager_strategy.shutdown()

    @classmethod
    def set_default_strategy(cls, strategy_to_set: ServiceManagerStrategy) -> None:
        """
        Set the service manager strategy.  This strategy will be used to retrieve services
        based on the algorithm defined in the ServiceManagerFactory implementnatation

        In the future, a ServiceManager may be able to use multiple strategies concurrently.  As of the current API, it
        only supports a single strategy

        @param strategyToSet the service manager strategy to set
        """
        ServiceManager._service_manager_strategy = strategy_to_set
