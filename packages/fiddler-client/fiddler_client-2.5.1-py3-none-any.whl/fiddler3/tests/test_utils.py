import os
from pathlib import Path

import pytest

from fiddler3.schemas.server_info import Version
from fiddler3.utils.validations import validate_artifact_dir
from fiddler3.utils.version import match_semver


def test_match_semvar_version() -> None:
    assert match_semver(None, '>=22.9.0') is False
    assert match_semver(Version.parse('22.9.0'), '>=22.10.0') is False
    assert match_semver(Version.parse('22.10.0'), '>=22.10.0') is True
    assert match_semver(Version.parse('22.10.0'), '>22.10.0') is False
    assert match_semver(Version.parse('22.11.0'), '>=22.10.0') is True
    assert match_semver(Version.parse('22.11.0'), '>22.10.0') is True
    assert match_semver(Version.parse('22.10.0'), '<=22.10.0') is True
    assert match_semver(Version.parse('22.10.0'), '<22.10.0') is False
    assert match_semver(Version.parse('22.9.0'), '<22.10.0') is True
    assert match_semver(Version.parse('22.11.0-RC1'), '>=22.11.0') is True


def test_validate_artifact_dir(tmp_path) -> None:
    artifact_dir = os.path.join(Path(__file__).resolve().parent, 'artifact_test_dir')
    assert validate_artifact_dir(Path(artifact_dir)) is None
    # Test for artifact_dir not valid directory
    with pytest.raises(ValueError):
        validate_artifact_dir(Path('test'))
    # Test for package.py file not found
    mock_dir = tmp_path / 'test'
    mock_dir.mkdir()
    with pytest.raises(ValueError):
        validate_artifact_dir(Path(mock_dir))
