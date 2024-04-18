"""Tests for interactors.retrieve module."""
import pytest
from bacore.domain import settings
from bacore.interactors import retrieve


@pytest.fixture
def fixture_test_system_information():
    """Fixture for system_information_os."""
    return "Darwin"


def test_system_information_os(fixture_test_system_information):
    """Test system_information_os."""
    information = retrieve.system_information_os(func_os=fixture_test_system_information)
    assert isinstance(information, settings.System)
    assert information.os == "Darwin"
