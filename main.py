#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one original joke, a single line of plain text, about a meeting
that should have been an email, to /output/entry.txt. Deterministic:
the same line every run.
"""
import os

# One fixed line, no randomness and no network: the output is identical
# on every run, so the two sandbox runs match byte for byte.
ENTRY = (
    "This meeting could have been an email. Instead, twelve people "
    "nodded at a slide nobody read for an hour, then agreed to meet again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
