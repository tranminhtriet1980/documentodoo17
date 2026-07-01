"""Extract images from PPTX per slide into docs folder."""
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def get_relationships(z, part_path):
    rels_path = part_path.replace("slides/", "slides/_rels/").replace(".xml", ".xml.rels")
    if rels_path not in z.namelist():
        return {}
    root = ET.fromstring(z.read(rels_path))
    return {
        el.get("Id"): el.get("Target")
        for el in root.findall("rel:Relationship", NS)
    }


def resolve_target(base_part, target):
    base = Path(base_part).parent
    return str((base / target).as_posix()).replace("\\", "/")


def extract(pptx_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []

    with zipfile.ZipFile(pptx_path) as z:
        slide_files = sorted(
            n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)
        )

        for slide_path in slide_files:
            slide_num = int(re.search(r"slide(\d+)", slide_path).group(1))
            rels = get_relationships(z, slide_path)
            root = ET.fromstring(z.read(slide_path))

            img_idx = 0
            for blip in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}blip"):
                embed = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                if not embed or embed not in rels:
                    continue
                target = rels[embed]
                media_path = resolve_target(slide_path, target)
                if media_path not in z.namelist():
                    # sometimes target is ../media/image1.png
                    media_path = "ppt/" + target.lstrip("../").lstrip("/")
                if media_path not in z.namelist():
                    continue

                img_idx += 1
                ext = Path(media_path).suffix or ".png"
                out_name = f"slide-{slide_num:02d}-{img_idx:02d}{ext}"
                out_path = out_dir / out_name
                out_path.write_bytes(z.read(media_path))
                manifest.append((slide_num, img_idx, out_name))
                print(f"Slide {slide_num}: {out_name}")

    # Write manifest for markdown
    manifest_path = out_dir / "manifest.txt"
    lines = ["# slide_num | file | use in markdown", ""]
    for slide_num, img_idx, name in manifest:
        lines.append(f"{slide_num} | {name} | ![Slide {slide_num}](images/quy-trinh/{name})")
    manifest_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nTotal images: {len(manifest)}")
    print(f"Output: {out_dir}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    pptx_dir = root / "MR UT"
    out = root / "docs" / "ke-toan" / "images" / "quy-trinh"
    for f in pptx_dir.glob("*.pptx"):
        if f.name.startswith("~$"):
            continue
        print("Processing PPTX...")
        extract(f, out)

    print("Processing images (remove logos, crop, resize)...")
    from process_quy_trinh_images import process_all

    process_all(root)
