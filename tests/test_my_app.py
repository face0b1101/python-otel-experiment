#!/usr/bin/env python


from python_poetry_boilerplate import __version__
from python_poetry_boilerplate.main import something


def test_version():
    assert __version__ == "0.1.0"


def test_something_with_string(str_input):
    assert something(str_input) is True


def test_something_with_input(int_input):
    assert something(int_input) is False
