"""Extract images from Mr Khanh XLHS PPTX into docs/du-an/images/xlhs."""
from pathlib import Path

from extract_pptx_images import extract
from process_quy_trinh_images import process_all


def main():
    root = Path(__file__).resolve().parents[1]
    pptx_dir = root / "Mr Khanh"
    out = root / "docs" / "du-an" / "images" / "xlhs"
    pptx_files = [f for f in pptx_dir.glob("*.pptx") if not f.name.startswith("~$")]
    if not pptx_files:
        raise SystemExit(f"Khong tim thay PPTX trong {pptx_dir}")

    for pptx in pptx_files:
        print("Processing PPTX:", pptx.name)
        extract(pptx, out)

    print("Processing images (crop, resize)...")
    stats = process_all(
        root,
        docs_module="du-an",
        img_dir_name="xlhs",
        skip_branding_suffix=False,
    )
    print("Kept:", stats["kept"], "Removed logos:", stats["removed"])


if __name__ == "__main__":
    main()
