"""Directory level plugin for Eureka tests."""

from __future__ import (
    absolute_import,
    division,
    print_function)
from termcolor import colored

import pytest
import os
import sys

import core.cli.my_env_cli as my_env_cli
from core.cli.my_env_cli import get_my_env_config_from_cli
from core.config.factory import get_config_map, config_factory

sys.path.insert(0, (os.path.dirname(__file__)))


def pytest_addoption(parser):
    """
    Add command line options.

    Create a logical group called 'MyGroup' and add CLI options underneath.

    :param parser: Object of _pytest.config.Parser that allows adding custom CLI options.
    :return: None
    """
    my_cli_group = parser.getgroup(
        colored('MyGroup', color='green', attrs=['bold', 'underline']))
    my_env_cli.add_cli(cli_group=my_cli_group)


def pytest_sessionstart(session):
    """
    Pytest hook function called at session startup.

    :param session: Instance of _pytest.main.Session.
        This is supplied by the pytest framework.
    :return: None
    """
    print('Session started.')


def pytest_collectreport(report):
    """
    Pytest hook called after testcase collection.

    :param report:pytest collection report
    :return: None
    """
    pass


def pytest_collection_finish(session):
    """
    Pytest hook function called after collecting all test cases.

    :param session: Instance of _pytest.main.Session
    :return: None
    """
    if not len(session.items):
        pytest.exit('No test case(s) to process!')


def pytest_collection_modifyitems(session, config, items):
    """
    Pytest hook function called for modification of collcted test cases.

    :param session: Instance of _pytest.main.Session
    :param config: Instances of _pytest.config.Config
    :param items: List of instances of _pytest.python.Function
        Each instance represents an object of the test case.
    :return: None
    """
    pass


def pytest_runtest_setup(item):
    """
    Pytest hook function called before setup of each test case.

    :param item: Instance of _pytest.python.Function representing current test case.
    :return: None
    """
    print('Starting Testcase : "{testcase}"'.format(testcase=item.name))


def pytest_runtest_teardown(item, nextitem):
    """
    Pytest hook function called before teardown of each test case.

    :param item: Instance of _pytest.python.Function representing current test case.
    :param nextitem: Instance of _pytest.python.Function representing next test case
                    to be executed.
    :return: None
    """
    print('Ending Testcase : "{testcase}"'.format(testcase=item.name))


def pytest_configure(config):
    """
    Pytest hook function called before test process is started.

    :param config: Instances of _pytest.config.Config
    :return: None
    """
    global ENV_CONFIG
    ENV_CONFIG = get_my_env_config_from_cli(cli_options=config.option)
    config_map = get_config_map()
    # Get the current environment
    current_env = ENV_CONFIG['type']
    tc_path_components = config.option.file_or_dir[0].split('/')
    tc_env_path = tc_path_components[-2] + '.' + \
        'environments' + '.' + current_env
    for fixture_name in config_map:
        if tc_env_path in str(config_map[fixture_name]):
            if ENV_CONFIG['configure']:
                fn = pytest.fixture(scope='module', autouse=True, name=fixture_name)(
                    config_factory(fixture_name))
                setattr(sys.modules[__name__], '{}_func'.format(fixture_name), fn)


def pytest_unconfigure(config):
    """
    Pytest hook function called before test process is exited.

    :param config: Instances of _pytest.config.Config
    :return: None
    """
    pass
