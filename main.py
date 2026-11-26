#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty entry.

Writes one line in the office printer's own voice to /output/entry.txt: after
41,208 pages printed without complaint, one jam earns it a thump, and the
printer has finally decided to file its own error report — against the human,
who has been thumping it since the first paper jam.
"""

import os

ENTRY = "I have printed 41,208 pages without complaint, and you thump me for one jam? Error 0x41: the human is the malfunction. Please step away from the tray."


def validate(text: str) -> str:
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
