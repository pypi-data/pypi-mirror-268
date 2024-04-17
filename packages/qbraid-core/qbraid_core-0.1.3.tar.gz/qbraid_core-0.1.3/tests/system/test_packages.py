# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for qBraid core helper functions related to system site-packages.

"""
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from qbraid_core.exceptions import QbraidException
from qbraid_core.system.exceptions import QbraidSystemError
from qbraid_core.system.packages import (
    get_active_site_packages_path,
    get_latest_package_version,
    get_local_package_path,
    get_local_package_version,
)

# pylint: disable=unused-argument


def test_active_site_pkgs_from_sys_exe():
    """Test the get_active_site_packages_path function for default python system executable."""
    with (
        patch("sys.executable", "/usr/bin/python"),
        patch("qbraid_core.system.executables.subprocess.run", "/usr/bin/python"),
        patch("site.getsitepackages", return_value=["/usr/lib/python3.9/site-packages"]),
    ):

        assert get_active_site_packages_path() == Path(
            "/usr/lib/python3.9/site-packages"
        ), "Should return the global site-packages path"


def test_active_site_pkgs_from_virtual_env():
    """Test the get_active_site_packages_path function when virtual env is active."""
    with (
        patch("sys.executable", "/envs/testenv/bin/python"),
        patch(
            "qbraid_core.system.executables.get_active_python_path",
            return_value=Path("/usr/bin/python"),
        ),
        patch("subprocess.run") as mock_run,
    ):
        mock_run.return_value = MagicMock(stdout="['/envs/testenv/lib/python3.9/site-packages']\n")

        active_site_packages = get_active_site_packages_path()
        expected_site_packages = Path("/envs/testenv/lib/python3.9/site-packages")
        assert str(active_site_packages) == str(
            expected_site_packages
        ), "Should return the virtual env's site-packages path"


def test_active_site_pkgs_raises_for_not_found():
    """Test the get_active_site_packages_path function when the site-packages path is not found."""
    with (
        patch("sys.executable", "/envs/testenv/bin/python"),
        patch(
            "qbraid_core.system.executables.get_active_python_path",
            return_value=Path("/usr/bin/python"),
        ),
        patch("subprocess.run") as mock_run,
    ):
        mock_run.return_value = MagicMock(stdout="[]\n")

        with pytest.raises(QbraidSystemError):
            get_active_site_packages_path()


def test_active_site_pkgs_correct_path_from_multiple():
    """Test the get_active_site_packages_path function when multiple
    site-packages paths are found."""
    with (
        patch("sys.executable", "/usr/envs/testenv/bin/python"),
        patch(
            "qbraid_core.system.executables.get_active_python_path",
            return_value=Path("/usr/envs/testenv/bin/python"),
        ),
        patch("subprocess.run") as mock_run,
    ):
        mock_run.return_value = MagicMock(
            stdout=(
                "['/usr/envs/testenv/lib/python3.9/site-packages', \
                '/usr/.local/lib/python3.9/site-packages']\n"
            )
        )

        active_site_packages = get_active_site_packages_path()
        expected_site_packages = Path("/usr/envs/testenv/lib/python3.9/site-packages")
        assert str(active_site_packages) == str(
            expected_site_packages
        ), "Should return the site-packages path matching the current environment"


@patch(
    "qbraid_core.system.packages.get_active_site_packages_path",
    return_value=Path("/path/to/site-packages"),
)
def test_get_local_package_path_exists(mock_get_active_site_packages_path):
    """Test the get_local_package_path function with an existing package."""
    package_name = "existing_package"
    expected_path = "/path/to/site-packages/existing_package"
    assert get_local_package_path(package_name) == Path(expected_path)


@patch(
    "qbraid_core.system.packages.get_active_site_packages_path",
    side_effect=QbraidException("Failed to find site-packages path."),
)
def test_get_local_package_path_error(mock_get_active_site_packages_path):
    """Test get_local_package_path function raises exception when site-packages not found."""
    package_name = "nonexistent_package"
    with pytest.raises(QbraidException):
        get_local_package_path(package_name)


def test_get_latest_version_raises():
    """Test the _get_latest_version function when an error occurs."""
    with pytest.raises(QbraidException):
        get_latest_package_version("nonexistent_package")


@pytest.mark.parametrize(
    "package,python_path", [("not_a_package", None), ("not_a_package", sys.executable)]
)
def test_get_local_version_raises_for_bad_package(package, python_path):
    """Test the _get_local_version function when an error occurs."""
    with pytest.raises(QbraidException) as exc_info:
        get_local_package_version(package, python_path=python_path)
    assert f"{package} not found in the current environment." in str(exc_info)


def test_get_local_version_raises_for_():
    """Test the _get_local_version function when an error occurs."""
    package = "pytest"  # valid package guaranteed to be installed
    python_path = "/bad/python/path"  # invalid python path
    with pytest.raises(QbraidException) as exc_info:
        get_local_package_version(package, python_path=python_path)
    assert f"Python executable not found at {python_path}." in str(exc_info)


@pytest.mark.parametrize("python_path", [None, Path(sys.executable), sys.executable])
def test_get_local_package_version_alt_python(python_path):
    """Test the get_latest_package_version function with an alternative Python path."""
    python_path = Path(sys.executable)
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="2.31.0\n")
        assert get_local_package_version("requests", python_path=python_path) == "2.31.0"
