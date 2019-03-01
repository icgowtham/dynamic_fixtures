"""Sample."""

from core.config.factory import register
from sample_testcase.environments.cloud.config import CloudConfigurator
from sample_testcase.environments.hw.config import HwConfigurator
from sample_testcase.environments.vm.config import VmConfigurator

# NOTE: Register cannot be done inside the test case folder.
# The reason for that is that when 'pytest_configure' gets called, it will not
# be aware of the test case since it executes at the very beginning. Since
# conftest.py gets executed, placing this here ensures that module
# is loaded.
register('cloud_fixture', CloudConfigurator)
register('hw_fixture', HwConfigurator)
register('vm_fixture', VmConfigurator)
