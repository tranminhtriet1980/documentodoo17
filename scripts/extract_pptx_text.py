"""Extract text from each slide in the accounting PPTX."""
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def slide_text(z, slide_path: str) -> str:
    root = ET.fromstring(z.read(slide_path))
    parts = []
    for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t"):
        if t.text:
            parts.append(t.text.strip())
        if t.tail:
            parts.append(t.tail.strip())
    return "\n".join(p for p in parts if p)


def main():
    root = Path(__file__).resolve().parents[1]
    pptx = root / "MR UT" / "01. Quy trình xử lý nghiệp vụ kế toán - odoo 18.pptx"
    out = root / "scripts" / "_pptx_slides_text.txt"

    lines = []
    with zipfile.ZipFile(pptx) as z:
        slides = sorted(
            n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)
        )
        for sp in slides:
            num = int(re.search(r"slide(\d+)", sp).group(1))
            text = slide_text(z, sp)
            lines.append(f"=== SLIDE {num} ===")
            lines.append(text or "(no text)")
            lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", out)


if __name__ == "__main__":
    main()
