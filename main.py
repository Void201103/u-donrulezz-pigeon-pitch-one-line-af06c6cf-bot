#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes the final one-line pitch to /output/entry.txt, deterministically.
No network, no randomness, no clock reads.
"""

import hashlib
import os
import sys

ENTRY = (
    "You're stuck in an elevator with a pigeon. "
    "I got in with no badge, no meeting, no pants. "
    "Give me $2M and I'll get into your boardroom the same way."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def build_entry() -> str:
    """Return the entry text with exactly one trailing newline."""
    return ENTRY + "\n"


def main() -> int:
    text = build_entry()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"wrote {OUTPUT_FILE}: {len(ENTRY)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
