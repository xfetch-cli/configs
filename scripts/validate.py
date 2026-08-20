#!/usr/bin/env python3
"""Validate JSONC/JSON files: strip // and /* */ comments and trailing
commas, then parse. Exits non-zero on the first broken file."""
import json
import re
import sys
from pathlib import Path


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
    if ok:
        print(f"OK: {len(files)} JSON/JSONC files valid.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
