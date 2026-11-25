"""The 3 AM Excuse — make.fun entry.

Writes one line (1-200 chars): the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM. Deterministic.

The joke: the wallet is the responsible adult in the room — it will not
let your 3 AM self make a decision your 9 AM self will regret. The hour
is the joke; at 3 PM this line makes no sense at all.
"""

import os

ENTRY = (
    "It is 3 AM. I refuse to sign anything your 9 AM self will regret — "
    "sleep on it, and if you still want it in daylight, I will be here."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
