"""Re-extract PPTX and reprocess images (fix header crop)."""
from pathlib import Path
import shutil

from extract_pptx_images import extract
from process_quy_trinh_images import process_all


def main():
    root = Path(__file__).resolve().parents[1]
    img_dir = root / "docs" / "ke-toan" / "images" / "quy-trinh"
    pptx_dir = root / "MR UT"

    # Xoa anh da xu ly (giu logo archive)
    for p in img_dir.glob("slide-*"):
        if p.is_file() and "_logo_archive" not in str(p):
            p.unlink()

    for f in pptx_dir.glob("*.pptx"):
        if f.name.startswith("~$"):
            continue
        print("Extracting from PPTX...")
        extract(f, img_dir)

    print("Processing (giu header/nut Odoo)...")
    stats = process_all(root)
    print("Done. Kept:", stats["kept"], "Removed logos:", stats["removed"])


if __name__ == "__main__":
    main()
