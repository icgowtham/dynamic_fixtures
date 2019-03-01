"""Configurator for HW environment."""

from core.config.base import BaseConfigurator


class HwConfigurator(BaseConfigurator):
    """Configurator for HW class."""

    def __init__(self):
        """Init."""
        super(HwConfigurator, self).__init__()
        self._is_configured = False

    def configure(self):
        """Configure."""
        print('***** Configuring in HW environment *****')
        self._is_configured = True

    def un_configure(self):
        """Un-configure."""
        if self.is_configured:
            print('***** Unconfiguring in HW environment *****')
        else:
            print('Configuration was not done, nothing to unconfigure!')
