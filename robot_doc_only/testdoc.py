from sys import argv
from distutils.version import StrictVersion
from robot.testdoc import TestDoc

from robot.version import get_version as get_robot_version
robot_version = get_robot_version()

if StrictVersion(robot_version) < StrictVersion('4.0'):
    from .testdoc_322 import TestDocSmall
else:
    from .testdoc_400 import TestDocSmall

def create_testdoc_small():
    rc = TestDocSmall().execute_cli(argv[1:])

def create_testdoc_full():
    rc = TestDoc().execute_cli(argv[1:])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_testdoc_small()
