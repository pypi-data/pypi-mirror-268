# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Module for extracting version information from package metadata.

"""

import json
import pathlib
import re
import sys
from typing import Union

from .exceptions import InvalidVersionError, VersionNotFoundError

if sys.version_info >= (3, 11):
    import tomllib

    MODE = "rb"
else:
    try:
        import toml as tomllib

        MODE = "r"
    except ImportError:
        tomllib = None
        MODE = "r"


def is_valid_semantic_version(v: str) -> bool:
    """
    Returns True if given string represents a valid
    semantic version, False otherwise.

    """
    try:
        # pylint: disable-next=import-outside-toplevel
        from packaging import version

        version.Version(v)
        return True
    except ImportError:
        # Fallback to regex matching if packaging is not installed
        semantic_version_pattern = re.compile(
            r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
            r"(-([0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*))?"
            r"(\+([0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*))?$"
        )
        return bool(semantic_version_pattern.match(v))
    except version.InvalidVersion:
        return False


def _get_version_from_json(package_json_path: Union[str, pathlib.Path]) -> str:
    """Get the version from the package.json file."""
    try:
        with open(package_json_path, "r", encoding="utf-8") as file:
            pkg_json = json.load(file)
            return pkg_json["version"]
    except (FileNotFoundError, KeyError, IOError) as err:
        raise VersionNotFoundError("Unable to find or read package.json") from err


def _simple_toml_version_extractor(file_path: Union[str, pathlib.Path]) -> str:
    """
    Extract the version from a pyproject.toml file using simple string processing.
    This function assumes the version is under [project] and is labeled as version = "x.y.z".
    It is a very basic and fragile implementation and not recommended for general TOML parsing.
    """
    version_pattern = re.compile(r'^version\s*=\s*"([^"]+)"$', re.M)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        match = version_pattern.search(content)
        if match:
            return match.group(1)
        raise ValueError("Version key not found in the TOML content.")
    except FileNotFoundError as err:
        raise VersionNotFoundError("The specified TOML file does not exist.") from err
    except IOError as err:
        raise VersionNotFoundError("An error occurred while reading the TOML file.") from err


def _get_version_from_toml(pyproject_toml_path: Union[str, pathlib.Path]) -> str:
    """Get the version from the pyproject.toml file."""
    if tomllib is None:
        return _simple_toml_version_extractor(pyproject_toml_path)

    try:
        with open(pyproject_toml_path, MODE) as file:
            pyproject_toml = tomllib.load(file)
            return pyproject_toml["project"]["version"]
    except (FileNotFoundError, KeyError, IOError) as err:
        raise VersionNotFoundError("Unable to find or read pyproject.toml") from err


def extract_version(
    file_path: Union[str, pathlib.Path], shorten_prerelease: bool = False, check: bool = False
) -> str:
    """Extract the version from a given package.json or pyproject.toml file.

    Args:
        file_path (Union[str, pathlib.Path]): Path to the package metadata file.
        shorten_prerelease (bool): Whether to shorten the prerelease version.
        check (bool): Whether to check if the version is a valid semantic version.

    Returns:
        str: The version extracted from the file.


    Raises:
        ValueError: If the file type is not supported.
        InvalidVersionError: If the version is not a valid semantic version.
        VersionNotFoundError: If the version is not found in the file.
    """
    file_path = pathlib.Path(file_path)

    if file_path.suffix == ".json":
        version = _get_version_from_json(file_path)
    elif file_path.suffix == ".toml":
        version = _get_version_from_toml(file_path)
    else:
        raise ValueError(
            "Unsupported file type. Only package.json and pyproject.toml are supported."
        )

    if shorten_prerelease:
        version = version.replace("-alpha.", "a").replace("-beta.", "b").replace("-rc.", "rc")

    if check and not is_valid_semantic_version(version):
        raise InvalidVersionError(f"Invalid semantic version: {version}")

    return version
