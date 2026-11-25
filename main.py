#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = "I promised my son I'd stop telling dad jokes, but I'm not groan up enough to quit yet."


def write_entry(path: str, text: str) -> None:
    """Write one line of text to path, readable by the grader."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    if "\n" in ENTRY.strip():
        raise ValueError("entry must be a single line")
    write_entry("/output/entry.txt", ENTRY)


if __name__ == "__main__":
    main()
