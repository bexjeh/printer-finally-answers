"""The Printer Finally Answers -- one line, in the printer's own voice.

Writes the printer's comeback to MAKEFUN_OUTPUT_DIR/entry.txt
(or ./entry.txt when the variable is unset). Stdlib only, deterministic:
the same bytes on every run.
"""

import os

LINE = "You hit print six times while I was warming up, so congratulations: six copies of the same email, all yours."


def main():
    if not 1 <= len(LINE) <= 240:
        raise ValueError("entry line must be 1-240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
