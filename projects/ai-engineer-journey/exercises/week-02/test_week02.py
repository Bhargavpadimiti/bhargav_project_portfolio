import pytest
from week02 import (
    estimate_cost,
    estimate_tokens,
    grade,
    is_palindrome,
    normalize_whitespace,
    parse_hours,
    safe_divide,
    truncate,
)

# ── estimate_tokens ───────────────────────────────────────────────────────


def test_tokens_exact_multiple_of_four():
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("a" * 400) == 100


def test_tokens_round_up_edge_case():
    assert estimate_tokens("abcde") == 2
    assert estimate_tokens("a") == 1


def test_tokens_empty_string_edge_case():
    assert estimate_tokens("") == 0


# ── estimate_cost ─────────────────────────────────────────────────────────


def test_cost_example_pricing():
    # 1M input tokens at $0.10/M plus 200k output tokens at $0.50/M
    assert estimate_cost(1_000_000, 200_000, 0.10, 0.50) == pytest.approx(0.2)


def test_cost_small_call():
    assert estimate_cost(1_500, 300, 4.00, 20.00) == pytest.approx(0.012)


def test_cost_zero_tokens_edge_case():
    assert estimate_cost(0, 0, 4.00, 20.00) == 0


def test_cost_is_rounded_to_six_decimals():
    assert estimate_cost(1, 0, 0.10, 0.50) == 0.0  # 0.0000001 rounds to 0.0
    assert estimate_cost(7, 0, 0.10, 0.50) == 0.000001


@pytest.mark.parametrize(
    "args",
    [(-1, 0, 1.0, 1.0), (0, -1, 1.0, 1.0), (0, 0, -1.0, 1.0), (0, 0, 1.0, -0.5)],
)
def test_cost_rejects_negative_values_edge_case(args):
    with pytest.raises(ValueError):
        estimate_cost(*args)


# ── truncate ──────────────────────────────────────────────────────────────


def test_truncate_fits_unchanged():
    assert truncate("hello", 10) == "hello"


def test_truncate_exact_length_unchanged_edge_case():
    assert truncate("hello", 5) == "hello"


def test_truncate_cuts_and_adds_ellipsis():
    result = truncate("hello world", 8)
    assert result == "hello w…"
    assert len(result) == 8


def test_truncate_to_one_character_edge_case():
    assert truncate("hello", 1) == "…"


def test_truncate_empty_text_edge_case():
    assert truncate("", 3) == ""


def test_truncate_rejects_zero_or_negative_edge_case():
    with pytest.raises(ValueError):
        truncate("hello", 0)
    with pytest.raises(ValueError):
        truncate("hello", -3)


# ── normalize_whitespace ──────────────────────────────────────────────────


def test_normalize_collapses_mixed_whitespace():
    assert normalize_whitespace("  hello \n\t world  ") == "hello world"


def test_normalize_already_clean():
    assert normalize_whitespace("a b c") == "a b c"


def test_normalize_empty_and_blank_edge_case():
    assert normalize_whitespace("") == ""
    assert normalize_whitespace(" \n\t ") == ""


# ── grade ─────────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    ("score", "letter"),
    [(95, "A"), (85, "B"), (75, "C"), (65, "D"), (30, "F")],
)
def test_grade_bands(score, letter):
    assert grade(score) == letter


@pytest.mark.parametrize(
    ("score", "letter"),
    [(90, "A"), (89.999, "B"), (80, "B"), (60, "D"), (59.9, "F"), (100, "A"), (0, "F")],
)
def test_grade_boundaries_edge_case(score, letter):
    assert grade(score) == letter


@pytest.mark.parametrize("score", [-0.1, 100.1, -50])
def test_grade_out_of_range_edge_case(score):
    with pytest.raises(ValueError):
        grade(score)


# ── safe_divide ───────────────────────────────────────────────────────────


def test_safe_divide_normal():
    assert safe_divide(10, 4) == 2.5


def test_safe_divide_zero_numerator():
    assert safe_divide(0, 5) == 0


def test_safe_divide_by_zero_edge_case():
    assert safe_divide(1, 0) is None
    assert safe_divide(1, 0.0) is None


# ── is_palindrome (STRETCH) ───────────────────────────────────────────────


@pytest.mark.parametrize(
    "text",
    ["racecar", "Race car", "A man, a plan, a canal: Panama", "No 'x' in Nixon", "12321"],
)
def test_palindromes(text):
    assert is_palindrome(text) is True


@pytest.mark.parametrize("text", ["ab", "hello", "12345"])
def test_not_palindromes(text):
    assert is_palindrome(text) is False


def test_palindrome_empty_and_punctuation_only_edge_case():
    assert is_palindrome("") is True
    assert is_palindrome("!!") is True


# ── parse_hours (STRETCH) ─────────────────────────────────────────────────


@pytest.mark.parametrize(
    ("text", "hours"),
    [
        ("2", 2.0),
        ("1.5", 1.5),
        (" 2.5 ", 2.5),
        ("2h", 2.0),
        ("2H", 2.0),
        ("90m", 1.5),
        ("45m", 0.75),
    ],
)
def test_parse_hours_valid(text, hours):
    assert parse_hours(text) == pytest.approx(hours)


def test_parse_hours_zero_is_allowed_edge_case():
    assert parse_hours("0") == 0


@pytest.mark.parametrize("text", ["", "   ", "abc", "1,5", "-1", "h", "m", "-30m"])
def test_parse_hours_invalid_edge_case(text):
    with pytest.raises(ValueError):
        parse_hours(text)
