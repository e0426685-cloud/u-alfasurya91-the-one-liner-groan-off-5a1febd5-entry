#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = "I promised my son I'd stop telling dad jokes, but I'm not groan up enough to quit yet."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
