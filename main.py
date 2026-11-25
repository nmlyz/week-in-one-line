#!/usr/bin/env python3
"""Week in One Line -- submission generator.

Writes one line summing up a week to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``). The line is 92 characters, inside the 100 limit
(93 with the trailing newline the file carries, still inside the limit).
The output is deterministic: running the script twice produces
byte-identical files.
"""

import os
from pathlib import Path

LINE = "My train app listed a station that doesn't exist; my chess engine reached a final that does."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 100


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-100 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    # The gate reads the file as UTF-8 text, so prove it encodes cleanly.
    line.encode("utf-8")
    # The gate counts the whole file, trailing newline included, so the
    # written bytes must stay inside the limit too.
    if len((line + "\n").encode("utf-8")) > MAX_LINE_LENGTH:
        raise ValueError("line plus trailing newline exceeds 100 characters")


def main() -> None:
    os.umask(0o022)
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)

    # Read the file back and prove what was written is exactly the line
    # plus one newline, inside the limit: the gate reads this file.
    written = entry_path.read_bytes()
    if written != (LINE + "\n").encode("utf-8"):
        raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
