"""Factory for creating the config fixture at runtime."""

from logging import getLogger

LOGGER = getLogger()
CONFIG_CLASS_MAP = {}


def config_factory(fixture_name):
    """Factory decorator method."""

    def create_config(request):
        """Method to define the function body."""
        klass = CONFIG_CLASS_MAP[fixture_name]
        config_obj = klass()
        if hasattr(klass, 'configure') and callable(getattr(klass, 'configure')):
            config_obj.configure()

        yield config_obj

        if hasattr(klass, 'un_configure') and callable(getattr(klass, 'un_configure')):
            config_obj.un_configure()

    return create_config


def empty_config_factory(fixture_name):  # noqa pylint: disable=unused-argument
    """Factory decorator method."""

    def create_empty_config(request):  # noqa pylint: disable=unused-argument
        """Method to define the function body."""
        yield

    return create_empty_config


def get_config_map():
    """Getter for the the map."""
    return CONFIG_CLASS_MAP


def register(name, klass):
    """
    Method to register the fixture name with the corresponding configuration class.

    :param name: The name of the fixture.
    :param klass: The configuration class.
    :return: None
    """
    if name in CONFIG_CLASS_MAP:
        LOGGER.warning('An entry with {name} already exists! Overwriting ...'.format(name=name))
    CONFIG_CLASS_MAP[name] = klass
