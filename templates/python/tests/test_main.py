import pytest

from template_project.main import greet, main


def test_greet_returns_greeting():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_strips_whitespace():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_main_prints_greeting(capsys):
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"
