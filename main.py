"""One Word for Your Wi-Fi — entry: Breadcrumbing.

Writes exactly one word to /output/entry.txt (or $OUTPUT_PATH).
No network, no dependencies, deterministic.
"""

import os

WORD = "Breadcrumbing"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
