"""
This module defines types and functions related to a service manager strategy, 
which is used to specify a concrete service manager strategy
"""

from abc import ABC, abstractmethod
from typing import Dict

from sphyrna.service_manager.service import ConfigurationT, ServiceException, ServiceT
from sphyrna.service_manager.service_configuration import (
    EMPTY_SERVICE_CONFIGURATION,
    ServiceConfiguration,
)
from sphyrna.service_manager.service_instance_provider import (
    DefaultServiceInstanceProviderImpl,
    ServiceInstanceProvider,
)
from sphyrna.service_manager.service_lifecycle_controller import (
    KnownServiceLifecycleControllers,
    ServiceLifecycleController,
)


class ServiceManagerStrategy(ABC):
    """
    Defines a Service Manager Strategy that controls the behavior of the ServiceManager
    """

    @abstractmethod
    def get_service(
        self, name: str, config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION
    ) -> ServiceT:
        """
        Retrieve a service.

        An Optional config may be supplied for service instance level
        configuration.  This must be supported by the associated
        ServiceLifecycleManager
        """

    @abstractmethod
    def is_service_defined(self, name: str) -> bool:
        """
        Determine if a service with the specified name has been defined
        """

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shutdown the ServiceManager and all associated services
        """


# mypy does not yet support PEP 695 generics
class ServiceDefinition[ServiceT]:  # type: ignore[valid-type]
    """
    Internal class
    """

    # pylint isn't handling generics in the way I'm specifing them
    # pylint: disable=E1136
    def __init__(
        self,
        service_lifecycle_controller: ServiceLifecycleController[
            ServiceT, ConfigurationT
        ],
        service_instance_provider: ServiceInstanceProvider[ServiceT] = None,
        config: ServiceConfiguration = EMPTY_SERVICE_CONFIGURATION,
    ):
        self.service_lifecycle_controller = service_lifecycle_controller
        self._service_instance_provider = service_instance_provider
        self.service_configuration = config

    def has_service_instance_provider(self) -> bool:
        """
        Check if the instance provider has been defined for this ServiceDefinition
        """
        return (hasattr(self, "_service_instance_provider")) and (
            self._service_instance_provider is not None
        )

    def get_service_instance_provider(self) -> ServiceInstanceProvider[ServiceT]:
        """
        Retrieve the service instance provider for this ServiceDefinition
        FIXME - Check Python Property support
        """
        if not self.has_service_instance_provider():
            raise ServiceException(
                "get serviceInstanceProvider called when one doesn't exist"
            )

        return self._service_instance_provider


class DefaultServiceManagerStrategyImpl(ServiceManagerStrategy):
    """
    This is the default service manager strategy.
    It's used by clients to programmetically register/define services
    """

    def __init__(self):
        self._controllers_for_active_services: Dict[
            str, ServiceLifecycleController[ServiceT, ConfigurationT]
        ] = {}
        self._service_definitions: Dict[str, ServiceDefinition[ServiceT]] = {}

    def register_service_by_controller_only(
        self,
        name: str,
        service_lifecycle_controller: ServiceLifecycleController[
            ServiceT, ConfigurationT
        ],
        override: bool = False,
    ) -> None:
        """
        Register a service.  This is the minimal number of inputs needed to register a new service.

        IMPORTANT NOTE: If registering a lifecycle controller through this method, the init(serviceInstanceProvider:
        ServiceInstanceProvider[T], config: C) method will NOT be called.  If it must be called, it should be invoked by
        the client before registering the service

        @param name
                    the name of the defined service
        @param serviceLifecycleController
                    controls the service lifeycle. For known controllers,
        see {@KnownServiceLifecycleControllers}
        @param override
                    An optional bool indicating whether or not to override an
        existing defintion with the same name. If self is false and a service
        definition already exists, an error will be thrown
        """
        if name in self._service_definitions:
            self._handle_service_override(name, override)

        service_definition: ServiceDefinition[ServiceT] = ServiceDefinition(
            service_lifecycle_controller
        )
        self._service_definitions[name] = service_definition

    def register_service(
        self,
        name: str,
        service_instance_provider: ServiceInstanceProvider[ServiceT],
        service_lifecycle_controller: ServiceLifecycleController[
            ServiceT, ConfigurationT
        ],
        config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION,
        override: bool = False,
    ) -> bool:
        """
        Register a service, providing the service name, instance provider, lifecycle controller and
        optional configuration
        """
        if name in self._service_definitions:
            self._handle_service_override(name, override)

        service_definition: ServiceDefinition[ServiceT] = ServiceDefinition(
            service_lifecycle_controller, service_instance_provider, config
        )
        self._service_definitions[name] = service_definition

    # FIXME - type as it's used here isn't strong enough.
    def register_service_by_class(
        self,
        name: str,
        service_class: type,
        service_lifecycle_controller_class: type,
        config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION,
        override: bool = False,
    ) -> None:
        """
        Register a service providing a contructor method for a service class and service lifecycle controller class

        @param name
                    the name of the defined service
        @param serviceClass
                    the class that implements the service
        @param serviceLifecycleControllerClass
                    the class that controls the service lifeycle. For known controllers,
        see {@KnownServiceLifecycleControllers}
        @param config
                    An Optional config may be supplied for service definition level
        configuration.
        @param override
                    An optional bool indicating whether or not to override an
        existing defintion with the same name. If self is false and a service
        definition already exists, an error will be thrown
        """

        service_provider = DefaultServiceInstanceProviderImpl(service_class)
        service_lifecycle_controller = service_lifecycle_controller_class()
        self.register_service(
            name, service_provider, service_lifecycle_controller, config, override
        )

    def register_singleton_service(
        self,
        name: str,
        service_class: type,
        config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION,
        override: bool = False,
    ) -> None:
        """
        Register a service that has a singleton lifecycle (only one instance exists)

        @param name
                    the name of the defined service
        @param serviceClass
                    the class that implements the service
        @param config
                    An Optional config may be supplied for service definition level
        configuration.
        @param override
                    An optional bool indicating whether or not to override an
        existing defintion with the same name. If self is false and a service
        definition already exists, an error will be thrown
        """
        self.register_service_by_class(
            name,
            service_class,
            KnownServiceLifecycleControllers.SINGLETON,
            config,
            override,
        )

    def get_service(
        self, name: str, config: ConfigurationT = EMPTY_SERVICE_CONFIGURATION
    ) -> ServiceT:

        service_lifecycle_controller: ServiceLifecycleController[ServiceT]

        if name not in self._service_definitions:
            raise ServiceException("Service not defined: " + name)

        # Check if the service lifecycle controller has already been initialized
        if name in self._controllers_for_active_services:
            service_lifecycle_controller = self._controllers_for_active_services[name]
        else:
            service_definition: ServiceDefinition[ServiceT] = self._service_definitions[
                name
            ]
            service_lifecycle_controller = (
                service_definition.service_lifecycle_controller
            )

            if service_definition.has_service_instance_provider():
                service_lifecycle_controller.init(
                    service_definition.get_service_instance_provider(),
                    service_definition.service_configuration,
                )

            self._controllers_for_active_services[name] = service_lifecycle_controller

        return service_lifecycle_controller.get_service()

    def is_service_defined(self, name: str) -> bool:
        return name in self._service_definitions

    def shutdown(self) -> None:
        for next_service_controller in self._controllers_for_active_services.values():
            next_service_controller.shutdown()

        self._controllers_for_active_services.clear()
        self._service_definitions.clear()

    def _handle_service_override(self, name: str, override: bool) -> None:
        if override:
            # Remove defintions.  Shutdown lifecycle controller
            del self._service_definitions[name]
            if name in self._controllers_for_active_services:
                controller_to_remove = self._controllers_for_active_services[name]
                controller_to_remove.shutdown()
                del self._controllers_for_active_services[name]
        else:
            raise ServiceException(
                "Service with name, :"
                + name
                + ", is already defined.  Specify override=true if it should be replaced"
            )


# Placeholder - TBD
# pylint: disable=unused-variable
class ConfigServiceManagerStrategy(DefaultServiceManagerStrategyImpl):
    """
    A strategy that reads service configuration from serviceConfig.json.  FIXME - To Be Implemented
    """
