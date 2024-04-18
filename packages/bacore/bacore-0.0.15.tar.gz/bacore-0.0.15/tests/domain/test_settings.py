"""Tests for domain.files module."""
import pytest
from bacore.domain import settings

pytestmark = pytest.mark.domain


@pytest.fixture
def fixture_project_root_dir(fixture_pyproject_file):
    return fixture_pyproject_file.parent


class TestCredential:
    """Tests for Credential entity."""

    credential = settings.Credential(username="username", password="passw0rd")

    def test_username(self):
        """Test username."""
        assert self.credential.username == "username"

    def test_username_must_not_contain_spaces(self):
        """Test username must not contain spaces."""
        with pytest.raises(ValueError):
            settings.Credential(username="user name")

    def test_password(self):
        """Test password."""
        assert self.credential.password.get_secret_value() == "passw0rd"

    def test_password_must_be_secret(self):
        """Test password must be of type pydantic.SecretStr."""
        assert isinstance(self.credential.password, settings.SecretStr)


class TestProject:
    """Tests for ProjectInfo entity."""

    def test_name(self):
        """Test name."""
        p = settings.Project(name="bacore")
        assert p.name == "bacore"

    def test_name_must_not_contain_spaces(self):
        """Test name_must_not_contain_spaces."""
        with pytest.raises(ValueError):
            settings.Project(name="ba core")


class TestProjectSettings:
    """Tests for ProjectSettings entity."""

    def test_path_must_be_directory(self, fixture_project_root_dir):
        """Test path_must_be_directory."""
        with pytest.raises(ValueError):
            settings.ProjectSettings(project_root_dir=fixture_project_root_dir / "wrong_path")

    def test_project_settings(self, fixture_project_root_dir):
        """Test ProjectSettings."""
        project_settings = settings.ProjectSettings(project_root_dir=fixture_project_root_dir)
        assert project_settings.name == "bacore"
        assert project_settings.version == "1.0.0"
        assert project_settings.description == "BACore is a framework for business analysis and test automation."


class TestSystem:
    """Test for SystemInfo."""

    def test_os(self):
        """Test os. (Darwin is macOS.)"""
        system_info = settings.System(os="Darwin")
        assert system_info.os in ["Darwin", "Linux", "Windows"]

    def test_os_must_be_supported(self):
        """Test os_must_be_supported."""
        with pytest.raises(ValueError):
            settings.System(os="AS/400")
