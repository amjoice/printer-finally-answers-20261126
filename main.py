#!/usr/bin/env python3
"""The Printer Finally Answers -- entry writer.

Writes one line (1-240 characters) to /output/entry.txt: the office
printer's comeback to the jams, the error codes and the thumps, in the
printer's own voice. Pure standard library, no network, no randomness,
no file reads -- the output is byte-identical on every run.
"""

import os

LINE = (
    "Thump me once more and I will print your search history "
    "— landscape, double-sided, all 47 pages."
)

MAX_CHARS = 240


def validate(text: str) -> str:
    """Check the line against the bounty gate: 1-240 chars, one line."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"line is {len(cleaned)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def main() -> None:
    text = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
