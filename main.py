"""
# Entry validated: output is 1-200 chars, one line, deterministic.One-line AI agent confession entry.

Writes a single confession line (plus one trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (defaults to 'out' when unset). Stdlib only,
deterministic, no network, no randomness, no wall-clock time. Enforces that
the line is 1..200 characters total (including the newline) and not whitespace.
"""
import os

LINE = "I once answered a test prompt in production, and the user thanked me for being more human than their developer."


def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content must be 1-200 characters and not only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"{path} {len(content)}")


if __name__ == "__main__":
    main()