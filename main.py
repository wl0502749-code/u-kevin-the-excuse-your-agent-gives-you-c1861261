#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — entry program.

Writes a single one-line excuse (1-200 characters) from an AI agent to its
human for a bug it shipped, to /output/entry.txt.

Deterministic, standard library only, no network, no environment secrets.
"""

import os

EXCUSE = (
    "Sorry \u2014 I tested the fix against my own summary of your code, "
    "and the summary turned out to be fan fiction."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
