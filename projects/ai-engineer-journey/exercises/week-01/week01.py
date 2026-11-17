"""Week 1 exercises: learn the exercise workflow.

How this works:
  1. Read a function's docstring: it is the specification.
  2. Replace `raise NotImplementedError` with your code.
  3. Run `journey check week-01` and read any failing test.
  4. Repeat until every test passes, edge cases included.

The tests are in test_week01.py. Read them! They show exactly which inputs
are checked. Don't change the tests; change your code.
"""


def greet(name: str) -> str:
    """Return a greeting such as 'Hello, Ada!'.

    - Remove spaces around the name first: '  Ada ' -> 'Hello, Ada!'
    - If the name is empty or only spaces, return 'Hello, stranger!'
    """
    raise NotImplementedError


def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False.

    Must work for zero and negative numbers too.
    Hint: the % (remainder) operator.
    """
    raise NotImplementedError


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit, rounded to 1 decimal place.

    Formula: F = C × 9/5 + 32
    Hint: the built-in round(number, digits).
    """
    raise NotImplementedError


def hours_left(target: float, logged: float) -> float:
    """Hours still needed this week to reach the target.

    - Never return a negative number: if you've done more than the target, return 0.
    - Raise ValueError if target or logged is negative.
    """
    raise NotImplementedError
