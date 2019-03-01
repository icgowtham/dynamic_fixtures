"""Configurator for VM environment."""

from core.config.base import BaseConfigurator


class VmConfigurator(BaseConfigurator):
    """Configurator for Cloud class."""

    def __init__(self):
        """Init."""
        super(VmConfigurator, self).__init__()
        self._is_configured = False

    def configure(self):
        """Configure."""
        print('@@@@@ Configuring in VM environment @@@@@')
        self._is_configured = True

    def un_configure(self):
        """Un-configure."""
        if self.is_configured:
            print('@@@@@ Un-configuring in VM environment @@@@@')
        else:
            print('Configuration was not done, nothing to un-configure!')
