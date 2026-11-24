#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (1-200 UTF-8 characters) to
/output/entry.txt. The line is a fixed, deliberately crafted string:
a doorbell camera records the narrator leaving for work, while the
narrator has not left the house in three days. The dread is earned
by the contradiction, not announced, and the final words land it.
"""

ENTRY = "My doorbell camera caught me leaving for work this morning, but I haven't left the house in three days."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
