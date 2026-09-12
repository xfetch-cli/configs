#!/usr/bin/env python3
"""Validate JSONC/JSON files: strip // and /* */ comments and trailing
commas, then parse. Also rejects broken glyphs (U+FFFD replacement
characters and control characters other than newline/tab) and emoji
codepoints, since configs must only use Nerd Font glyphs and plain text.
Exits non-zero on the first broken file."""
import json
import re
import sys
import unicodedata
from pathlib import Path

# A replacement character means a glyph was mangled by an encoding round trip;
# a control character would corrupt the terminal when rendered.
BROKEN_GLYPHS = ("\ufffd",)

# Codepoints with the Unicode Emoji_Presentation property. Configs must not
# carry emoji; use Nerd Font glyphs (private use area) or plain text instead.
EMOJI_RANGES = (
    (0x231A, 0x231B), (0x23E9, 0x23EC), (0x23F0, 0x23F0), (0x23F3, 0x23F3),
    (0x25FD, 0x25FE), (0x2614, 0x2615), (0x2648, 0x2653), (0x267F, 0x267F),
    (0x2693, 0x2693), (0x26A1, 0x26A1), (0x26AA, 0x26AB), (0x26BD, 0x26BE),
    (0x26C4, 0x26C5), (0x26CE, 0x26CE), (0x26D4, 0x26D4), (0x26EA, 0x26EA),
    (0x26F2, 0x26F3), (0x26F5, 0x26F5), (0x26FA, 0x26FA), (0x26FD, 0x26FD),
    (0x2705, 0x2705), (0x270A, 0x270B), (0x2728, 0x2728), (0x274C, 0x274C),
    (0x274E, 0x274E), (0x2753, 0x2755), (0x2757, 0x2757), (0x2795, 0x2797),
    (0x27B0, 0x27B0), (0x27BF, 0x27BF), (0x2B1B, 0x2B1C), (0x2B50, 0x2B50),
    (0x2B55, 0x2B55), (0x1F000, 0x1FAFF), (0xFE0F, 0xFE0F), (0x20E3, 0x20E3),
)


def is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return any(lo <= cp <= hi for lo, hi in EMOJI_RANGES)


def check_glyphs(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for glyph in BROKEN_GLYPHS:
            if glyph in line:
                issues.append(f"{path}:{lineno}: contains U+FFFD replacement character")
        for ch in line:
            if unicodedata.category(ch) == "Cc" and ch != "\t":
                issues.append(f"{path}:{lineno}: contains control character U+{ord(ch):04X}")
            elif is_emoji(ch):
                issues.append(f"{path}:{lineno}: contains emoji U+{ord(ch):04X}")
    return issues


def strip_jsonc(text: str) -> str:
    out = []
    i = 0
    n = len(text)
    in_string = False
    while i < n:
        c = text[i]
        if in_string:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if c == '"':
                in_string = False
            i += 1
            continue
        if c == '"':
            in_string = True
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def strip_trailing_commas(text: str) -> str:
    return re.sub(r",(\s*[}\]])", r"\1", text)


def main() -> int:
    roots = [Path(p) for p in sys.argv[1:]] or [Path(".")]
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
        else:
            files.extend(root.rglob("*.jsonc"))
            files.extend(root.rglob("*.json"))
    files = sorted(f for f in files if ".git" not in f.parts)
    if not files:
        print("No JSON/JSONC files found.")
        return 1
    ok = True
    for f in files:
        raw = f.read_text(encoding="utf-8")
        try:
            json.loads(strip_trailing_commas(strip_jsonc(raw)))
        except json.JSONDecodeError as e:
            ok = False
            print(f"INVALID {f}: {e}")
            continue
        glyph_issues = check_glyphs(f, raw)
        if glyph_issues:
            ok = False
            for issue in glyph_issues:
                print(f"INVALID GLYPH {issue}")
    if ok:
        print(f"OK: {len(files)} JSON/JSONC files valid (no broken glyphs, no emoji).")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
