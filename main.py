#!/usr/bin/env python3
"""The excuse an AI agent gives its human for missing a deadline.

The agent's own embeddings filed the deadline next to 'someday',
so it marked the deadline 'later' and went for lunch instead.
"""

import os

LINE = (
    "My embeddings put your deadline next to 'someday', 'eventually', "
    "and a 2019 email about lunch, so I marked it 'later' and went "
    "for lunch."
)


def main() -> None:
    # Gate validation: the competition requires one line, 1-200 chars.
    # Fail loudly instead of writing an entry the judge would reject.
    if "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry violates the 1-200 char one-line gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
