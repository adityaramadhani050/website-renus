#!/usr/bin/env python3
"""Gabungkan blok homepage + kalkulator menjadi satu post_content siap kirim.

Pemakaian: python3 scripts/build.py
Hasil:     build/homepage.html
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCKS = ROOT / "blocks"
BUILD = ROOT / "build"
INCLUDE = re.compile(r"<!-- @include ([\w.-]+) -->")


def expand(text: str) -> str:
    def repl(m: re.Match) -> str:
        return (BLOCKS / m.group(1)).read_text(encoding="utf-8").strip()

    return INCLUDE.sub(repl, text)


def main() -> int:
    out = expand((BLOCKS / "homepage.html").read_text(encoding="utf-8"))
    if INCLUDE.search(out):
        print("include bertingkat tidak didukung", file=sys.stderr)
        return 1

    h1 = len(re.findall(r"<h1[\s>]", out))
    if h1 != 1:
        print(f"homepage harus punya tepat satu <h1>, ditemukan {h1}", file=sys.stderr)
        return 1

    BUILD.mkdir(exist_ok=True)
    (BUILD / "homepage.html").write_text(out, encoding="utf-8")
    print(f"build/homepage.html ({len(out.encode('utf-8')):,} byte)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
