#!/usr/bin/env python


import pytest


@pytest.fixture
def str_input():
    return "Hello World!"


@pytest.fixture
def int_input():
    return 23
