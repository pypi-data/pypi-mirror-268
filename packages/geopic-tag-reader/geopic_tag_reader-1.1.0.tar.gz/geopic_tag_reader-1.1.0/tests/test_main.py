import pytest
from typer.testing import CliRunner
from geopic_tag_reader import main

runner = CliRunner()


def test_read_broken_makernotes():
    with pytest.raises(RuntimeError) as e:
        result = runner.invoke(main.app, ["read", "--image", "tests/fixtures/broken_makernotes.jpg"], catch_exceptions=False)
    assert "entries considered invalid; not read" in str(e)


def test_read_ignore_broken_makernotes():
    result = runner.invoke(main.app, ["read", "--image", "tests/fixtures/broken_makernotes.jpg", "--ignore-exiv2-errors"])
    assert result.exit_code == 0
    assert "Latitude" in result.stdout
