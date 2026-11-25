"""The 3AM Fridge Text — writes one line to /output/entry.txt.

Stdlib only, deterministic: the text is a literal constant, written as
UTF-8 bytes with no trailing newline (a newline would count as a
character against the 1-140 gate and read as a second line).
"""
import os

TEXT = "It's 3am. I counted: you've opened me 6 times tonight and eaten nothing. I'm starting to think you just like the light."

OUTPUT_PATH = "/output/entry.txt"


def main():
    data = TEXT.encode("utf-8")
    # Fail fast instead of silently writing an entry the gate rejects:
    # the sealed scorer requires 1-140 characters, not only whitespace.
    if not 1 <= len(TEXT) <= 140 or not TEXT.strip():
        raise ValueError("TEXT violates the 1-140 character gate")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
