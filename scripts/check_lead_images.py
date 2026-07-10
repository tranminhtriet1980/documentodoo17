#!/usr/bin/env python3
"""Kiem tra anh Chương II Leads theo manifest.txt."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "docs" / "ban-hang" / "crm" / "images" / "lead-process"
MANIFEST = IMG_DIR / "manifest.txt"


def main() -> None:
    if not MANIFEST.is_file():
        raise SystemExit(f"Khong tim thay {MANIFEST}")

    expected = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- "):
            expected.append(line[2:].strip())

    missing = [name for name in expected if not (IMG_DIR / name).is_file()]
    extra = [
        p.name
        for p in IMG_DIR.iterdir()
        if p.is_file() and p.name != "manifest.txt" and p.name not in expected
    ]

    print("Thu muc: docs/ban-hang/crm/images/lead-process/")
    print(f"Can co: {len(expected)} file")
    print(f"Da co:  {len(expected) - len(missing)} file")
    if missing:
        print("\nTHIEU:")
        for name in missing:
            print(f"  - {name}")
    else:
        print("\nOK: Du tat ca anh trong manifest.")

    if extra:
        print("\nFile thua (khong trong manifest):")
        for name in extra:
            print(f"  - {name}")

    raise SystemExit(1 if missing else 0)


if __name__ == "__main__":
    main()
