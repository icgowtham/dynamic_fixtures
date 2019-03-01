"""Configurator for Cloud environment."""

from core.config.base import BaseConfigurator


class CloudConfigurator(BaseConfigurator):
    """Configurator for Cloud class."""

    def __init__(self):
        """Init."""
        super(CloudConfigurator, self).__init__()
        self._is_configured = False

    def configure(self):
        """Configure."""
        print('$$$$$ Configuring in Cloud environment $$$$$')
        self._is_configured = True

    def un_configure(self):
        """Un-configure."""
        if self.is_configured:
            print('$$$$$ Unconfiguring in Cloud environment $$$$$')
        else:
            print('Configuration was not done, nothing to unconfigure!')
