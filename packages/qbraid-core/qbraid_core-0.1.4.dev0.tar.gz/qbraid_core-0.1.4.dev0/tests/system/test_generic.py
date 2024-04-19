# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the replace_str function in the envs app.

"""

from qbraid_core.system.generic import replace_str


def test_replace_str(tmp_path):
    """Test replacing a string in a file."""
    file_path = tmp_path / "test_file.txt"
    initial_content = "Hello world! Hello everyone!"
    target = "Hello"
    replacement = "Hi"
    file_path.write_text(initial_content, encoding="utf-8")

    replace_str(target, replacement, str(file_path))

    # Verify that the content has been correctly replaced
    updated_content = file_path.read_text(encoding="utf-8")
    expected_content = initial_content.replace(target, replacement)
    assert updated_content == expected_content, "The file's content was not updated as expected."
