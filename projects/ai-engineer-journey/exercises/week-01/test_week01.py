import pytest
from week01 import celsius_to_fahrenheit, greet, hours_left, is_even

# ── greet ─────────────────────────────────────────────────────────────────


def test_greet_simple_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_strips_surrounding_spaces():
    assert greet("  Ada ") == "Hello, Ada!"


def test_greet_empty_name_edge_case():
    assert greet("") == "Hello, stranger!"


def test_greet_only_spaces_edge_case():
    assert greet("    ") == "Hello, stranger!"


# ── is_even ───────────────────────────────────────────────────────────────


def test_is_even_positive():
    assert is_even(4) is True
    assert is_even(7) is False


def test_is_even_zero_edge_case():
    assert is_even(0) is True


def test_is_even_negative_numbers_edge_case():
    assert is_even(-2) is True
    assert is_even(-3) is False


# ── celsius_to_fahrenheit ─────────────────────────────────────────────────


def test_freezing_and_boiling_points():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0


def test_minus_forty_is_the_same_in_both_scales_edge_case():
    assert celsius_to_fahrenheit(-40) == -40.0


def test_rounds_to_one_decimal():
    assert celsius_to_fahrenheit(36.6) == 97.9


# ── hours_left ────────────────────────────────────────────────────────────


def test_hours_left_normal():
    assert hours_left(10, 4) == 6


def test_hours_left_with_decimals():
    assert hours_left(10, 2.5) == 7.5


def test_hours_left_exactly_on_target_edge_case():
    assert hours_left(10, 10) == 0


def test_hours_left_never_negative_edge_case():
    assert hours_left(10, 12) == 0


def test_hours_left_rejects_negative_input_edge_case():
    with pytest.raises(ValueError):
        hours_left(10, -1)
    with pytest.raises(ValueError):
        hours_left(-5, 1)
