"""Everyday Wonder — one sentence that makes a small everyday moment strange.

Writes a single sentence (at most 200 characters) to /output/entry.txt.
Standard library only.
"""

import os

SENTENCE = (
    "My shadow reaches the crosswalk half a step before I do, "
    "already impatient to cross a street I haven't arrived at yet."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(SENTENCE) <= 200):
        raise ValueError(
            f"sentence must be 1-200 characters, got {len(SENTENCE)}"
        )
    if SENTENCE.strip() == "":
        raise ValueError("sentence must not be only whitespace")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
