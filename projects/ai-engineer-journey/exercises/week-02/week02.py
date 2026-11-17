"""Week 2 exercises: values, types, strings and decisions.

Each function is a small piece you'll reuse when building LLM apps:
estimating tokens and cost, cleaning text, validating input.

Run `journey check week-02`. Exercises marked STRETCH use ideas from
week 3 (loops); attempt them last.
"""

from __future__ import annotations


def estimate_tokens(text: str) -> int:
    """Rough token count for English text: about 4 characters per token.

    Return the number of characters divided by 4, rounded UP to a whole number.
    An empty string has 0 tokens.
    Examples: 'abcd' -> 1, 'abcde' -> 2.
    Hint: math.ceil
    """
    raise NotImplementedError


def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
) -> float:
    """Cost in dollars of one LLM call. Prices are per million tokens.

    cost = input_tokens × input_price / 1,000,000 + output_tokens × output_price / 1,000,000
    Round the result to 6 decimal places.
    Raise ValueError if any argument is negative.
    """
    raise NotImplementedError


def truncate(text: str, max_chars: int) -> str:
    """Shorten text to at most max_chars characters, ending with '…' if cut.

    - If text already fits, return it unchanged.
    - Otherwise return the first (max_chars - 1) characters followed by '…'
      (one character), so the result is exactly max_chars long.
    - Raise ValueError if max_chars is less than 1.
    """
    raise NotImplementedError


def normalize_whitespace(text: str) -> str:
    """Collapse every run of spaces, tabs and newlines into one space, and trim both ends.

    '  hello \\n\\t world  ' -> 'hello world'
    Hint: str.split() with no arguments, and str.join().
    """
    raise NotImplementedError


def grade(score: float) -> str:
    """Letter grade for a quiz percentage.

    A: 90 and above · B: 80 to under 90 · C: 70 to under 80 · D: 60 to under 70 · F: below 60
    Raise ValueError if score is below 0 or above 100.
    """
    raise NotImplementedError


def safe_divide(a: float, b: float) -> float | None:
    """Return a / b, or None when b is zero (instead of crashing)."""
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """STRETCH: True if text reads the same backwards, ignoring case, spaces and punctuation.

    Only letters and digits count: 'A man, a plan, a canal: Panama' -> True.
    An empty string counts as a palindrome.
    Hint: str.isalnum(), str.lower(), and slicing with [::-1].
    """
    raise NotImplementedError


def parse_hours(text: str) -> float:
    """STRETCH: Turn a typed duration into hours, the way `journey log` might.

    Accepted forms (case-insensitive, surrounding spaces ignored):
      '2' -> 2.0      '1.5' -> 1.5      '2h' -> 2.0      '90m' -> 1.5
    Raise ValueError for anything else: '', 'abc', '1,5', or a negative amount.
    Hint: float('abc') already raises ValueError for you.
    """
    raise NotImplementedError
