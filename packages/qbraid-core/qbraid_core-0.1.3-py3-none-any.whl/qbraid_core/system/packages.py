# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for serving information about Python packages.

"""
import ast
import logging
import site
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Optional, Union

import requests

from .exceptions import QbraidSystemError
from .executables import (
    get_active_python_path,
    get_python_version_from_cfg,
    get_python_version_from_exe,
    python_paths_equivalent,
)

logger = logging.getLogger(__name__)


def get_venv_site_packages_path(venv_path: Path) -> Path:
    """
    Determines the site-packages directory for a given virtual environment in an OS-agnostic manner.
    Automatically selects the Python version if a single version is present in the 'lib' directory.
    If multiple versions are detected, it attempts to determine the correct version through
    configuration files or the Python executable.

    Args:
        venv_path (pathlib.Path): The path to the virtual environment directory.

    Returns:
        A Path object pointing to the site-packages directory, or None if unable to determine.

    Raises:
        QbraidSystemError: If an error occurs while determining the site-packages path.
    """
    if sys.platform == "win32":
        return venv_path / "Lib" / "site-packages"

    python_dirs = sorted(venv_path.glob("lib/python*"))
    if not python_dirs:
        raise QbraidSystemError("No Python directories found in the virtual environment.")

    if len(python_dirs) == 1:
        return python_dirs[0] / "site-packages"

    python_version = get_python_version_from_cfg(venv_path)
    python_version = python_version or get_python_version_from_exe(venv_path)

    if not python_version:
        raise QbraidSystemError("Unable to determine Python version from the virtual environment.")

    major_minor_version = ".".join(python_version.split(".")[:2])
    lib_python_dir = venv_path / f"lib/python{major_minor_version}"
    return lib_python_dir / "site-packages"


def get_active_site_packages_path(python_path: Optional[Path] = None) -> Path:
    """
    Retrieves the site-packages path of the current Python environment,
    respecting active virtual environments, as well.

    """

    current_python_path = Path(sys.executable)
    shell_python_path = python_path or get_active_python_path()

    if python_paths_equivalent(shell_python_path, current_python_path):
        site_packages_paths = [Path(path) for path in site.getsitepackages()]

    else:
        try:
            result = subprocess.run(
                [shell_python_path, "-c", "import site; print(site.getsitepackages())"],
                capture_output=True,
                text=True,
                check=True,
            )
        except subprocess.CalledProcessError as err:
            raise QbraidSystemError(
                f"Failed to get user site-packages directory from {shell_python_path}."
            ) from err
        except FileNotFoundError as err:
            raise QbraidSystemError(f"Python executable not found at {shell_python_path}.") from err

        paths = ast.literal_eval(result.stdout.strip())
        site_packages_paths = [Path(path) for path in paths]

    # Common logic for finding the correct site-packages path
    if len(site_packages_paths) == 1:
        return site_packages_paths[0]

    # Base path of the Python environment
    shell_base_path = shell_python_path.parent.parent
    sys_base_path = current_python_path.parent.parent

    base_paths = [shell_base_path]
    if shell_base_path != sys_base_path:
        base_paths.append(sys_base_path)

    # Find the site-packages path that is within the same environment
    for base_path in base_paths:
        for path in site_packages_paths:
            if base_path in path.parents:
                return path

    raise QbraidSystemError("Failed to find site-packages path.")


def get_local_package_path(package: str) -> Path:
    """Retrieves the local path of a package."""
    try:
        site_packages_path = get_active_site_packages_path()
        return site_packages_path / package
    except (PackageNotFoundError, ModuleNotFoundError) as err:
        raise QbraidSystemError(f"{package} not found in the current environment.") from err


def get_local_package_version(package: str, python_path: Optional[Union[str, Path]] = None) -> str:
    """Retrieves the local version of a package."""
    if python_path:
        try:
            result = subprocess.run(
                [
                    str(python_path),
                    "-c",
                    f"import importlib.metadata; print(importlib.metadata.version('{package}'))",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as err:
            raise QbraidSystemError(f"{package} not found in the current environment.") from err
        except FileNotFoundError as err:
            raise QbraidSystemError(f"Python executable not found at {python_path}.") from err

    try:
        return version(package)
    except PackageNotFoundError as err:
        raise QbraidSystemError(f"{package} not found in the current environment.") from err


def get_latest_package_version(package: str) -> str:
    """Retrieves the latest version of package from PyPI."""
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except requests.RequestException as err:
        raise QbraidSystemError(f"Failed to retrieve latest {package} version from PyPI.") from err
