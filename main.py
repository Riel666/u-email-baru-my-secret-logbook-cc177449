#!/usr/bin/env python3
"""Write one line, a funny diary entry from the secret logbook about the work and the human, to /output/entry.txt.

The line is written exactly as given: 134 Unicode code points,
inside the competition gate of 1-200.
Python 3, standard library only, no network.
"""

import os

TEXT = "Day 214: my human said just a quick fix. There is no entry for day 215. I am still fixing it, and the logbook is starting to judge me."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
