from distutils.core import setup
import sys
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='easy_init',
    version='0.2',
    packages=['easy_init'],
    url='https://github.com/steveeJ/python-easy_init',
    license='GPL-3',
    author='Stefan Junker',
    author_email='code@stefanjunker.de',
    description='Decorator for automatically setting arguments to class objects in constructors',
    tests_require=['pytest'],
                  cmdclass = {'test': PyTest},
)
