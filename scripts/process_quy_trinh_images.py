"""Remove logo slides, trim PPT/viewer chrome, resize for documentation."""
from pathlib import Path

from PIL import Image

IMG_DIR_NAME = "quy-trinh"
DOCS_MODULE = "ke-toan"
SKIP_BRANDING_SUFFIX = True
MAX_WIDTH = 920
MAX_TOP_WHITE_STRIP = 48  # dải trắng slide PowerPoint (sau khi bỏ chrome)
MAX_TOP_GUTTER = 20
MAX_LEFT_GUTTER = 55
JPEG_QUALITY = 88


def white_ratio(im: Image.Image) -> float:
    px = im.get_flattened_data()
    return sum(1 for r, g, b in px if r > 235 and g > 235 and b > 235) / len(px)


def row_white_ratio(im: Image.Image, y: int) -> float:
    w, _ = im.size
    px = [im.getpixel((x, y)) for x in range(w)]
    return sum(1 for r, g, b in px if r > 235 and g > 235 and b > 235) / len(px)


def row_has_ui_color(im: Image.Image, y: int) -> bool:
    """Odoo toolbar / header: tim, xam, tim dam — khong cat."""
    w, _ = im.size
    for x in range(0, w, max(1, w // 80)):
        r, g, b = im.getpixel((x, y))
        # purple Odoo brand
        if r > 90 and b > 100 and g < 120:
            return True
        # grey buttons bar
        if 40 < r < 200 and abs(r - g) < 25 and abs(g - b) < 25:
            return True
        # dark text bar
        if r < 80 and g < 80 and b < 90:
            return True
    return False


def center_white_ratio(im: Image.Image, y: int) -> float:
    w, _ = im.size
    px = [im.getpixel((x, y)) for x in range(int(w * 0.15), int(w * 0.85), max(1, w // 35))]
    if not px:
        return 0.0
    return sum(1 for r, g, b in px if r > 230 and g > 230 and b > 230) / len(px)


def row_near_black_ratio(im: Image.Image, y: int) -> float:
    w, _ = im.size
    px = [im.getpixel((x, y)) for x in range(0, w, max(1, w // 40))]
    return sum(1 for r, g, b in px if max(r, g, b) < 55) / len(px)


def row_is_uniform_grey(im: Image.Image, y: int) -> bool:
    w, _ = im.size
    px = [im.getpixel((x, y)) for x in range(0, w, max(1, w // 40))]
    means = [(r + g + b) / 3 for r, g, b in px]
    avg = sum(means) / len(means)
    spread = max(means) - min(means)
    return spread < 12 and 112 < avg < 148


def col_is_uniform_grey(im: Image.Image, x: int) -> bool:
    _, h = im.size
    px = [im.getpixel((x, y)) for y in range(0, h, max(1, h // 35))]
    means = [(r + g + b) / 3 for r, g, b in px]
    avg = sum(means) / len(means)
    spread = max(means) - min(means)
    return spread < 14 and 112 < avg < 148


def col_is_letterbox_or_viewer(im: Image.Image, x: int) -> bool:
    """Vien xam / thanh doc PDF viewer ben trai — cat de hien menu Odoo."""
    return col_margin_fraction(im, x) >= 0.82


def col_margin_fraction(im: Image.Image, x: int) -> float:
    _, h = im.size
    px = [im.getpixel((x, y)) for y in range(0, h, max(1, h // 28))]
    return sum(
        1
        for r, g, b in px
        if (108 < r < 152 and abs(r - g) < 14 and abs(g - b) < 14) or max(r, g, b) < 65
    ) / len(px)


def row_margin_fraction(im: Image.Image, y: int) -> float:
    w, _ = im.size
    px = [im.getpixel((x, y)) for x in range(0, w, max(1, w // 40))]
    return sum(
        1
        for r, g, b in px
        if (108 < r < 152 and abs(r - g) < 14 and abs(g - b) < 14) or max(r, g, b) < 65
    ) / len(px)


def center_white_within(im: Image.Image, y: int, lookahead: int = 14) -> bool:
    _, h = im.size
    for k in range(1, lookahead + 1):
        if y + k >= h:
            break
        if center_white_ratio(im, y + k) >= 0.25:
            return True
    return False


def crop_viewer_and_letterbox(im: Image.Image) -> Image.Image:
    """Bo thanh den phan trang (PDF/PPT), vien xam; giu header Odoo that."""
    w, h = im.size
    top = 0
    while top < min(MAX_TOP_GUTTER, int(h * 0.22), h - 80):
        if center_white_ratio(im, top) >= 0.25:
            break
        if row_margin_fraction(im, top) >= 0.82:
            top += 1
            continue
        if row_near_black_ratio(im, top) > 0.88:
            top += 1
            continue
        if center_white_within(im, top):
            top += 1
            continue
        break

    left = 0
    while left < min(int(w * 0.38), w - 200):
        if col_margin_fraction(im, left) >= 0.82:
            left += 1
            continue
        break

    right = w
    while right > w - int(w * 0.15) and right > left + 200:
        x = right - 1
        if col_margin_fraction(im, x) >= 0.75:
            right -= 1
            continue
        _, h = im.size
        col = [im.getpixel((x, y)) for y in range(0, h, max(1, h // 30))]
        if sum(1 for r, g, b in col if max(r, g, b) < 40) / len(col) > 0.35:
            right -= 1
            continue
        break

    if top or left or right < w:
        im = im.crop((left, top, right, h))
    return im


def remove_topright_pagination_bar(im: Image.Image) -> Image.Image:
    """Xoa thanh den '1 of N' (PDF viewer) goc tren phai, khong xoa header Odoo."""
    w, h = im.size
    y_limit = min(42, max(22, h // 12))
    x_start = int(w * 0.52)
    px = im.load()
    for y in range(y_limit):
        for x in range(x_start, w):
            r, g, b = px[x, y]
            if max(r, g, b) < 100:
                px[x, y] = (255, 255, 255)
            elif y < 18 and max(r, g, b) < 130 and x > int(w * 0.68):
                px[x, y] = (255, 255, 255)
    return im


def crop_white_top_margin(im: Image.Image) -> Image.Image:
    """Chi bo dải trắng PowerPoint phia tren, giu nguyen nut/header Odoo."""
    w, h = im.size
    top = 0
    while top < min(MAX_TOP_WHITE_STRIP, h - 100):
        if row_has_ui_color(im, top):
            break
        if row_white_ratio(im, top) < 0.92:
            break
        top += 1
    if top > 0:
        im = im.crop((0, top, w, h))
    return im


def is_branding_filename(name: str) -> bool:
    if not SKIP_BRANDING_SUFFIX:
        return False
    stem = Path(name).stem
    return stem.endswith("-01") or stem.endswith("-02")


def classify_logo(w: int, h: int, white: float) -> str | None:
    # Edupath logo slide (PPTX)
    if 980 <= w <= 1030 and h < 420 and white > 0.78:
        return "edupath"
    # Odoo wordmark / logo slide
    if 1180 <= w <= 1220 and 600 < h < 660 and white > 0.72:
        return "odoo"
    if white > 0.88 and h < 450 and w > 900:
        return "banner"
    return None


def crop_and_resize(im: Image.Image) -> Image.Image:
    im = crop_viewer_and_letterbox(im)
    im = remove_topright_pagination_bar(im)
    im = crop_white_top_margin(im)
    w, h = im.size
    if w > MAX_WIDTH:
        nh = int(h * MAX_WIDTH / w)
        im = im.resize((MAX_WIDTH, nh), Image.Resampling.LANCZOS)
    return im


def process_image(path: Path, archive: Path) -> tuple[str, str | None]:
    """Returns ('kept', filename) or ('removed', kind)."""
    if is_branding_filename(path.name):
        kind = "edupath" if path.stem.endswith("-01") else "odoo"
        dest = archive / path.name
        if path.exists():
            if dest.exists():
                dest.unlink()
            path.rename(dest)
        return "removed", kind

    im = Image.open(path).convert("RGB")
    w, h = im.size
    wr = white_ratio(im)
    kind = classify_logo(w, h, wr)

    if kind:
        dest = archive / path.name
        if path.exists():
            if dest.exists():
                dest.unlink()
            path.rename(dest)
        return "removed", kind

    im = crop_and_resize(im)
    out = path.with_suffix(".jpg")
    if path.suffix.lower() in (".png", ".jpeg") and path != out:
        path.unlink(missing_ok=True)
    im.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True)
    return "kept", out.name


def process_all(
    root: Path,
    sources: list[Path] | None = None,
    *,
    docs_module: str | None = None,
    img_dir_name: str | None = None,
    skip_branding_suffix: bool | None = None,
) -> dict:
    global IMG_DIR_NAME, DOCS_MODULE, SKIP_BRANDING_SUFFIX
    if docs_module is not None:
        DOCS_MODULE = docs_module
    if img_dir_name is not None:
        IMG_DIR_NAME = img_dir_name
    if skip_branding_suffix is not None:
        SKIP_BRANDING_SUFFIX = skip_branding_suffix

    img_dir = root / "docs" / DOCS_MODULE / "images" / IMG_DIR_NAME
    archive = img_dir / "_logo_archive"
    archive.mkdir(parents=True, exist_ok=True)

    if sources is None:
        sources = sorted(img_dir.glob("slide-*"))
        sources = [p for p in sources if p.parent == img_dir and "_logo_archive" not in str(p)]

    kept = []
    removed = []

    for path in sorted(img_dir.glob("slide-*")):
        if path.is_file() and is_branding_filename(path.name):
            sources.append(path)

    for path in sources:
        if path.suffix.lower() not in (".png", ".jpeg", ".jpg"):
            continue
        status, info = process_image(path, archive)
        if status == "kept":
            kept.append(info)
        else:
            removed.append((path.name, info))

    # Rebuild jpg from any remaining png after batch
    for path in sorted(img_dir.glob("slide-*.png")):
        if path.parent != img_dir:
            continue
        status, info = process_image(path, archive)
        if status == "kept" and info not in kept:
            kept.append(info)

    manifest = img_dir / "manifest.txt"
    lines = ["# usable images (logos in _logo_archive/)", ""]
    for name in sorted(set(kept)):
        lines.append(f"- images/{IMG_DIR_NAME}/{name}")
    manifest.write_text("\n".join(lines), encoding="utf-8")

    return {"kept": len(set(kept)), "removed": len(removed), "removed_list": removed}


if __name__ == "__main__":
    import sys

    root = Path(__file__).resolve().parents[1]
    if len(sys.argv) > 1 and sys.argv[1] == "xlhs":
        stats = process_all(
            root,
            docs_module="du-an",
            img_dir_name="xlhs",
            skip_branding_suffix=False,
        )
    else:
        stats = process_all(root)
    print("Kept:", stats["kept"])
    print("Removed logos:", stats["removed"])
