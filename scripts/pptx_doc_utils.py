"""Shared helpers for PPTX → MkDocs documentation."""
from pathlib import Path

EXT_PRIORITY = {".jpg": 0, ".jpeg": 0, ".png": 1}
KE_TOAN_BRANDING_SUFFIXES = ("-01", "-02")


def is_branding_image(name: str, *, skip_suffixes: bool = True) -> bool:
    if not skip_suffixes:
        return False
    stem = Path(name).stem
    return any(stem.endswith(suf) for suf in KE_TOAN_BRANDING_SUFFIXES)


def images_for_slide(
    img_dir: Path,
    num: int,
    *,
    skip_branding: bool = True,
    prefer_sub02: bool = False,
) -> list[str]:
    prefix = f"slide-{num:02d}-"
    candidates = [
        p.name
        for p in img_dir.glob(f"{prefix}*")
        if p.is_file() and not is_branding_image(p.name, skip_suffixes=skip_branding)
    ]
    if prefer_sub02:
        has02 = any("-02." in n for n in candidates)
        if has02:
            candidates = [n for n in candidates if "-01." not in n]
    best: dict[str, str] = {}
    for name in candidates:
        stem = Path(name).stem
        ext = Path(name).suffix.lower()
        prev = best.get(stem)
        if not prev or EXT_PRIORITY.get(ext, 9) < EXT_PRIORITY.get(Path(prev).suffix.lower(), 9):
            best[stem] = name
    return sorted(best.values())


def img_block(
    img_dir: Path,
    img_prefix: str,
    slide: int,
    alt: str | None = None,
    *,
    no_note: bool = False,
    skip_branding: bool = True,
    prefer_sub02: bool = False,
    img_class: str = "doc-screenshot",
) -> list[str]:
    files = images_for_slide(
        img_dir,
        slide,
        skip_branding=skip_branding,
        prefer_sub02=prefer_sub02,
    )
    if not files:
        if no_note:
            return []
        return [
            f'!!! note "Slide {slide}"',
            "    Slide gốc là **sơ đồ / nội dung** trên PowerPoint (không có ảnh chụp Odoo tách riêng).",
            "",
        ]
    lines = []
    for f in files:
        label = alt or f"Slide {slide}"
        lines.append(f"![{label}]({img_prefix}/{f}){{ .{img_class} }}")
        lines.append("")
    return lines


def slide_tag(slide: int | str) -> str:
    return f"*Hình slide {slide}*"
