"""Environment CLI."""

import ast

from core.environment import SUPPORTED_ENVIRONMENTS
from termcolor import colored


def add_cli(cli_group):
    """
    Add CLI options.

    :param cli_group: Object of _pytest.config.OptionGroup
    :return: None
    """
    env_defaults = (
            '{' +
            '"type": "hw", ' +
            '"configure": "True" ' +
            '}'
    )

    cli_group.addoption(
        '--myEnv',
        default=env_defaults,
        help=colored(
            "Environment specification.\n" +
            "\nSupported environment types: {tp}.".format(tp=', '.join(SUPPORTED_ENVIRONMENTS)) +
            "\ne.g., --myEnv '{env_defaults}'".format(env_defaults=env_defaults),
            color='yellow'
        )
    )


def is_env_specified_in_cli(cli_options):
    """
    Check if environment is specified in CLI.

    :param cli_options: Object of _pytest.config.CmdOptions
        This object is part of standard pytest objects:
        request.config.option
        OR
        session.config.option
    :return: boolean
        True, if environment is specified in CLI, False, otherwise
    """
    my_env_cli_options = [
        cli_options.myEnv
    ]
    if not any(my_env_cli_options):
        return False
    else:
        return True


def _sanitize_cli(cli_options):
    """
    Sanitize the CLI for environment options.

    An environment may be specified in the command line via:
    - 'myEnv'
    This function sanitizes the CLI (for environment options).

    :param cli_options: Object of _pytest.config.CmdOptions
        This object is part of standard pytest objects:
        request.config.option
        OR
        session.config.option
    :return: None
    """
    my_env_cli_options = [
        cli_options.myEnv
    ]

    my_env_usage_str = (
            '\nUsage:' +
            '\n  --myEnv \'{"type": "hw", "configure": True}\''
    )

    if not is_env_specified_in_cli(cli_options):
        raise Exception(
            'No environment is provided.' +
            '\nAn environment can be specified in the CLI as:' +
            my_env_usage_str
        )

    try:
        my_env_config = ast.literal_eval(cli_options.myEnv)
        if not isinstance(my_env_config, dict):
            raise Exception(
                'Environment config is not in valid format.' +
                my_env_usage_str
            )

        if 'type' not in my_env_config:
            raise Exception(
                '"type" is required. Environment config is not in valid format.' +
                my_env_usage_str
            )

        if my_env_config['type'] not in SUPPORTED_ENVIRONMENTS:
            raise Exception(
                'Environment config is not in valid format.' +
                my_env_usage_str
            )

        if not isinstance(my_env_config['configure'], bool):
            raise Exception(
                'Environment config is not in valid format.' +
                my_env_usage_str
            )

        # Use the defaults.
        if 'configure' not in my_env_config and \
                (my_env_config['type'] == 'hw'):
            my_env_config['configure'] = True

        return my_env_config
    except Exception:
        # ast.literal_eval will throw an exception if unable to parse
        raise Exception(
            'Environment config is not in valid format.' +
            my_env_usage_str
        )


def get_my_env_config_from_cli(cli_options):
    """
    Return the my_env_config dictionary from CLI.

    :param cli_options: Object of _pytest.config.CmdOptions
        This object is part of standard pytest objects:
        request.config.option
        OR
        session.config.option
    :return: dictionary
        A my_env_config dictionary.
    """
    return _sanitize_cli(cli_options)
