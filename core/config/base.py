"""Abstract class."""

import sys
from abc import ABCMeta, abstractmethod

from six import add_metaclass


@add_metaclass(ABCMeta)
class BaseConfigurator:
    """Abstract configurator class."""

    RESOURCE_TO_CONFIG_PATH_MAP = {}

    def __init__(self):
        """
        Base class init method.

        :return: None
        """
        self._filePath = sys.modules[self.__class__.__module__].__file__
        self._is_configured = False

    @property
    def is_configured(self):
        """Flag to check whether configuration was already done."""
        return self._is_configured

    @abstractmethod
    def configure(self):
        """Perform configuration steps."""
        pass

    @abstractmethod
    def un_configure(self):
        """Perform un-configuration steps."""
        pass
