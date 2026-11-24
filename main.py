"""Write the make.fun bounty entry text to disk.

Bounty: u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d
Standard library only, no network.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> str:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
