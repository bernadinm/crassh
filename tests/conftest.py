import pytest
def pytest_addoption(parser):
    parser.addoption("--cisco", action="store_true", help="run csico IOS tests")