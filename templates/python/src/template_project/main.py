"""Command-line entry point for Template Project.

Replace this module with your project's real logic. Keep functions small and
pure where possible so they are easy to test.
"""

from __future__ import annotations

import argparse


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Template Project")
    parser.add_argument("name", nargs="?", default="world", help="who to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
