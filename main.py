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

# Pinned digest of the entry text (with its one trailing newline).
# Any accidental change to the pitch changes this digest and the run
# must fail instead of silently submitting a different line.
EXPECTED_SHA256 = "4da27c0f4c3be8d86189982ff93e2148eed287b47b0c1e71025b1ba2933788c5"


def build_entry() -> str:
    """Return the entry text with exactly one trailing newline."""
    return ENTRY + "\n"


def main() -> int:
    text = build_entry()
    # The entry must stay one line: a newline inside ENTRY would split
    # the pitch and break the one-line rule, so fail loudly instead.
    assert "\n" not in ENTRY, "ENTRY must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read the file back and prove the disk content is exactly what
    # we intended to write; a partial write must never pass silently.
    with open(OUTPUT_FILE, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "written entry does not match"
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    assert digest == EXPECTED_SHA256, "entry text changed unexpectedly"
    print(f"wrote {OUTPUT_FILE}: {len(ENTRY)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
