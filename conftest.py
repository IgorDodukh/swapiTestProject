import pytest

from helpers.api_helper import ApiHelper


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    environment_url = request.config.getoption("env_url")
    ApiHelper(environment_url)


def pytest_addoption(parser):
    parser.addoption("--env_url", default="https://swapi.dev/api")
