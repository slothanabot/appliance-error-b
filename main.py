#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the funniest
honest error message an appliance could show.

The line: a washing machine reporting a genuinely plausible fault — an
unbalanced load — in its own flat, put-upon voice. The laugh comes from the
truth of the fault, not a bolted-on pun: a real washer really does refuse to
spin when the drum is off balance, and here it names the exact culprits —
one sock versus a wet towel — then refuses like a fed-up worker rather than
trying to be funny.
"""

import os

# One line, at most 200 characters (93 chars). Single line, UTF-8.
ENTRY = "Error: load unbalanced. One sock versus a wet towel. I refuse to spin under these conditions."


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 cap"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
