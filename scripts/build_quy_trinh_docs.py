"""Build quy-trinh-nghiep-vu.md and quy-trinh-hinh-anh.md from slide map (MR UT PPTX).

CANH BAO: Ghi de noi dung da sua tay. Chi chay qua TrichAnhTuPptx.bat.
"""
from pathlib import Path

IMG = "images/quy-trinh"
# slide-NN-01 = logo Edupath, slide-NN-02 = chữ/logo Odoo (ảnh PPTX) — không đưa vào tài liệu
BRANDING_SUFFIXES = ("-01", "-02")
EXT_PRIORITY = {".jpg": 0, ".jpeg": 0, ".png": 1}


def is_branding_image(name: str) -> bool:
    stem = Path(name).stem
    return any(stem.endswith(suf) for suf in BRANDING_SUFFIXES)


def images_for_slide(img_dir: Path, num: int) -> list[str]:
    prefix = f"slide-{num:02d}-"
    candidates = [
        p.name
        for p in img_dir.glob(f"{prefix}*")
        if p.is_file() and not is_branding_image(p.name)
    ]
    # Cùng slide: ưu tiên .jpg đã xử lý, bỏ .png trùng (vd. slide-07-03.jpg + .png)
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
    slide: int,
    alt: str | None = None,
    *,
    no_note: bool = False,
    img_class: str = "doc-screenshot",
) -> list[str]:
    files = images_for_slide(img_dir, slide)
    if not files:
        if no_note:
            return []
        return [
            f"!!! note \"Slide {slide}\"",
            "    Slide gốc là **sơ đồ quy trình** trên PowerPoint (không có ảnh chụp Odoo).",
            "",
        ]
    lines = []
    for f in files:
        label = alt or f"Slide {slide}"
        lines.append(f"![{label}]({IMG}/{f}){{ .{img_class} }}")
        lines.append("")
    return lines


def slide_tag(slide: int) -> str:
    return f"*Hình slide {slide}*"


def build_nghiep_vu(img_dir: Path) -> str:
    lines = [
        "# Quy trình xử lý nghiệp vụ kế toán",
        "",
        "!!! info \"Nguồn tài liệu\"",
        "    MR UT — *01. Quy trình xử lý nghiệp vụ kế toán - odoo 18*. Áp dụng tương tự **Odoo 17**.",
        "",
        "!!! tip \"Hình ảnh\"",
        "    - Trang này: quy trình + hình theo **đúng thứ tự slide** PowerPoint",
        "    - [Phụ lục hình ảnh](quy-trinh-hinh-anh.md) — xem riêng từng slide",
        "    - Cập nhật: `TrichAnhTuPptx.bat` → `BuildTaiLieu.bat`",
        "",
        "---",
        "",
        "## I. Khai báo hệ thống tài khoản (Slide 2)",
        "",
        "Cấu hình trước khi vận hành (chi tiết: file quản lý hệ thống tài khoản & Cost Center):",
        "",
        "| STT | Hạng mục |",
        "|-----|----------|",
        "| 1 | **Tài khoản** kế toán |",
        "| 2 | **Tài khoản ngân hàng** |",
        "| 3 | **Sổ nhật ký** kế toán |",
        "| 4 | **Cost Center** |",
        "",
    ]
    lines.extend(img_block(img_dir, 2, "Hệ thống tài khoản", img_class="doc-screenshot-sm"))
    lines.extend(
        [
            "---",
            "",
            "## II. Ghi nhận doanh thu — Thu tiền khách hàng",
            "",
            "### 1. Quy trình — tổng quan (Slide 3)",
            "",
            "| Level | Vai trò | Mô tả |",
            "|-------|---------|--------|",
            "| **0** | TVV | Lên đơn hàng, **Confirm** khi đã thống nhất dịch vụ, sản phẩm, giá với khách |",
            "| **1** | Kế toán | Kiểm tra SO đủ thông tin |",
            "| **2** | Kế toán | Tạo **Invoice** (doanh thu, phí thu hộ). Sai TK sau Payment → **hủy Payment**, sửa Invoice |",
            "| **3** | Kế toán | **Thu tiền** khách theo điều khoản hợp đồng |",
            "",
            "```mermaid",
            "flowchart LR",
            "    SO[SO] --> K{KT kiểm tra}",
            "    K -->|OK| INV[Invoice]",
            "    INV --> PAY[Payment]",
            "```",
            "",
            "### 2. Quy trình — chi tiết (Slide 4)",
            "",
            "Luồng: **SO → Kiểm tra thông tin SO → Invoice → Payment** (có nhánh hủy/điều chỉnh nếu sai).",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 4, "Quy trình doanh thu"))
    lines.extend(
        [
            "### 3. Tạo Invoice (Slide 4)",
            "",
            "Tạo hóa đơn ghi nhận doanh thu từ đơn bán.",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 4, "Tạo Invoice"))
    lines.extend(
        [
            "### 4. Tạo Invoice & hợp đồng (Slide 6)",
            "",
            "**Kiểm tra thông tin đơn hàng:**",
            "",
            "| Trường hợp | Thứ tự |",
            "|------------|--------|",
            "| **Có hợp đồng** | (2) → (3) → (1) → (4) |",
            "| **Không cần hợp đồng** | (2) → (3), sau đó (1) → (4) |",
            "",
            "!!! note \"Cờ hợp đồng trên SO\"",
            "    - Đơn **có** hợp đồng: **bật màu xanh** ở bước (2)",
            "    - Đơn **không** hợp đồng: **tắt** bước (2), tạo hợp đồng ở bước (3)",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 6, "Invoice và hợp đồng"))
    lines.extend(
        [
            "### 5. Chi tiết tạo Invoice — xác nhận (Slide 7)",
            "",
            "Kiểm tra hóa đơn đã ghi nhận đúng:",
            "",
            "- **Sổ nhật ký**, **tài khoản** doanh thu / thu hộ, **giá tiền**",
            "- Đúng → chọn **Xác nhận** (Post/Confirm)",
            "",
            "!!! note \"Tỷ giá manual\"",
            "    Bật **Use manual Exchange Rate** để nhập tỷ giá; không chọn → hệ thống lấy tỷ giá mặc định.",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 7, "Chi tiết Invoice"))
    lines.extend(
        [
            "### 6. Tạo Payment — thu tiền khách (Slide 8, 9, 10)",
            "",
            "- **Slide 8:** Tạo **Payment** thu tiền theo hợp đồng/đơn (đủ một lần hoặc nhiều đợt)",
            "- **Slide 9–10:** Xem và **in phiếu thu** cho khách ký",
            "    - CN Việt Nam: mẫu **01-TT / 02-TT**",
            "    - CN Mỹ: phiếu thu/chi theo mẫu chi nhánh",
            "",
        ]
    )
    for sn in (8, 9, 10):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn))

    lines.extend(
        [
            "---",
            "",
            "## III. Các bút toán chi tiền (Slide 11)",
            "",
            "| Nghiệp vụ | Bút toán (tóm tắt) |",
            "|-----------|-------------------|",
            "| Hoàn phí chương trình | Nợ 3388 (chi tiết ĐT) / Có 112, 111 |",
            "| Hoàn phí ký quỹ | Nợ 344 (chi tiết ĐT) / Có 112, 111 |",
            "| TT đối tác nước ngoài | TT: Nợ 331 / Có 112,111 — Kết chuyển: Nợ 3388 / Có 331 |",
            "| TT NCC trong nước | Nợ CP 641,642 (Cost Center) / Có 331 → TT: Nợ 331 / Có 112,111 |",
            "| Lương, BHXH, thuế… | TT: Nợ 3341, 3335… / Có 112,111 — Kết chuyển: Nợ 6425 / Có 3341, 3335 |",
            "",
            "---",
            "",
            "## IV. Ghi nhận chi phí / mua hàng — Thanh toán NCC",
            "",
            "### 1. Quy trình (Slide 12)",
            "",
            "| Level | Vai trò | Mô tả |",
            "|-------|---------|--------|",
            "| **0** | User | Đề xuất mua hàng **đã duyệt**, đủ chứng từ (HĐ, chứng từ CP…) |",
            "| **1** | User / KT | Tạo **Bill**. Sau duyệt đề nghị → KT **Xác nhận** Bill |",
            "| **2** | User | Tạo **đề nghị thanh toán** theo Bill — chọn **loại thanh toán** đúng → [Mục V](#v-de-xuat-thanh-toan) |",
            "| **3** | Kế toán | **Chi tiền** theo Bill + đề nghị đã duyệt |",
            "",
            "```mermaid",
            "flowchart LR",
            "    PO[PO / Mua hàng] --> BILL[Bill]",
            "    BILL --> DNTT[Đề nghị TT]",
            "    DNTT --> PAY[Payment]",
            "    PAY --> PRINT[In phiếu chi]",
            "```",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 12, "Quy trình NCC"))
    lines.extend(
        [
            "### 2. Tạo Bill — ghi nhận hóa đơn mua (Slide 13, 14)",
            "",
            "**Kế toán › Nhà cung cấp › Hóa đơn** (hoặc PO → Create Bill):",
            "",
            "- Chọn **nhà cung cấp** (chưa có → tạo mới)",
            "- **Loại thanh toán**, **sổ nhật ký**, **tiền tệ** (VND/USD)",
            "- Chi tiết: sản phẩm/dịch vụ, **TK chi phí**, số lượng, số tiền",
            "- Ghi nhận CP theo **Cost Center** (TK 641, 642…)",
            "",
        ]
    )
    for sn in (13, 14):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn))

    lines.extend(
        [
            "### 3. Tạo Payment thanh toán NCC (Slide 15, 16)",
            "",
            "1. **Xác nhận** Bill (sau khi đề nghị được duyệt — Mục V)",
            "2. **Register Payment** — chọn ngân hàng/tiền mặt, số tiền, nội dung",
            "",
        ]
    )
    for sn in (15, 16):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn))

    lines.extend(
        [
            "### 4. In phiếu chi (Slide 17)",
            "",
            "In phiếu chi sau khi thanh toán (mẫu theo chi nhánh).",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 17, "In phiếu chi"))

    lines.extend(
        [
            "---",
            "",
            "## V. Đề xuất thanh toán (DNTT) {#v-de-xuat-thanh-toan}",
            "",
            "### 1. Quy trình phê duyệt (Slide 18)",
            "",
            "| Level | Vai trò | Mô tả |",
            "|-------|---------|--------|",
            "| **0** | Người lập ĐNTT | Lập yêu cầu; thu thập chứng từ theo **danh mục** KT |",
            "| **1** | QLBP / TCN | Kiểm tra → Duyệt/Từ chối (ghi lý do). Áp dụng khi loại TT cần QLBP |",
            "| **2** | Kế toán / HR | Kiểm tra + **Checklist** chứng từ → Duyệt/Từ chối. Sau BOD → thanh toán |",
            "| **3** | BOD | Duyệt / Từ chối |",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 18, "Quy trình DNTT"))
    lines.extend(
        [
            "### 2. Tạo đề xuất thanh toán (Slide 19, 20, 21)",
            "",
            "**Thông tin chung:** Chi nhánh, phòng ban, người phê duyệt cuối, loại yêu cầu, danh mục thanh toán.",
            "",
            "**Thông tin chi tiết:** Loại tiền, hình thức TT, số tiền, nội dung ĐNTT, STK (nếu CK/Sec), thông tin HĐ (nếu có).",
            "",
            "**QLBP/TCN:** Thêm người duyệt nếu loại thanh toán đi qua QLBP/TCN.",
            "",
            "**Checklist:** Đủ chứng từ, HĐ theo từng loại thanh toán.",
            "",
        ]
    )
    for sn in (19, 20, 21):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn))

    lines.extend(
        [
            "### 3. View đề nghị thanh toán trên Bill (Slide 22)",
            "",
            "1. Lưu đề nghị thanh toán",
            "2. Trên **Bill** → nút **View DNTT**",
            "3. Chọn **View DNTT** → đính kèm hồ sơ → **Xác nhận** yêu cầu thanh toán",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 22, "View DNTT"))
    lines.extend(
        [
            "### 4. Xem trạng thái & thanh toán sau duyệt (Slide 23)",
            "",
            "Sau khi **phê duyệt** → quay lại Bill → **Xác nhận** → tạo **Payment** NCC.",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 23, "Trạng thái thanh toán"))

    lines.extend(
        [
            "---",
            "",
            "## VI. Bút toán tổng hợp — Không có hóa đơn",
            "",
            "### 1. Tạo bút toán thu hộ / chi hộ (Slide 24, 25, 26)",
            "",
            "- Chọn loại thanh toán, **sổ nhật ký**, loại tiền, Account, hạng mục, số tiền",
            "- Chọn **SO** (đối tượng chi hộ); nhiều đối tượng → thêm nhiều dòng SO",
            "- **Nợ:** đối tượng **chi hộ** | **Có:** đối tượng **thu hộ**",
            "- Nhập số tiền, TK ngân hàng/tiền mặt chi ra",
            "- Sau khi tạo bút toán → **Tạo đề nghị thanh toán** (giống Mục V)",
            "",
        ]
    )
    for sn in (24, 25, 26):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn))

    lines.extend(
        [
            "### 2. Đề nghị thanh toán & vào sổ (Slide 27)",
            "",
            "Tạo đề nghị thanh toán giống **Mục V**. Sau khi ĐNTT **được duyệt** → quay lại bút toán → **Post (Vào sổ)**.",
            "",
            "!!! note",
            "    Đề nghị thanh toán tạo **giống** đề nghị thanh toán NCC.",
            "",
            "---",
            "",
            "Xem thêm: [Phụ lục hình ảnh](quy-trinh-hinh-anh.md) | [Hóa đơn](hoa-don.md) | [Thanh toán](thanh-toan.md) | [Sổ cái](so-cai.md)",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 27, "Bút toán tổng hợp"))

    return "\n".join(lines)


def build_hinh_anh(img_dir: Path) -> str:
    """Phụ lục: đúng cấu trúc mục I–VI và tiêu đề con như file PowerPoint."""

    def subsection(title: str, slide_nums: list[int], body: list[str], alt: str = "") -> list[str]:
        block = [f"### {title}", ""]
        if slide_nums:
            if len(slide_nums) == 1:
                block.append(slide_tag(slide_nums[0]))
            else:
                block.append(f"*Hình slide {', '.join(str(s) for s in slide_nums)}*")
            block.append("")
        block.extend(body)
        for sn in slide_nums:
            block.extend(img_block(img_dir, sn, alt or title, no_note=True))
        return block

    lines = [
        "# Phụ lục — Hình ảnh quy trình kế toán",
        "",
        "Theo file *01. Quy trình xử lý nghiệp vụ kế toán - odoo 18* (MR UT), **từ trên xuống**.",
        "",
        "[← Quy trình nghiệp vụ (đầy đủ)](quy-trinh-nghiep-vu.md)",
        "",
        "---",
        "",
        "## I. Khai báo hệ thống tài khoản {#i-he-thong}",
        "",
        slide_tag("2"),
        "",
        "Hệ thống **tài khoản kế toán**, **tài khoản ngân hàng**, **sổ nhật ký** và **Cost Center**",
        "(chi tiết: file quản lý hệ thống tài khoản).",
        "",
        "1. Tài khoản",
        "2. Cost Center",
        "",
    ]
    lines.extend(img_block(img_dir, 2, "Hệ thống tài khoản", img_class="doc-screenshot-sm"))

    lines.extend(
        [
            "---",
            "",
            "## II. Ghi nhận doanh thu — Thu tiền khách hàng {#ii-doanh-thu}",
            "",
        ]
    )

    lines.extend(
        subsection(
            "1. Quy trình — hình slide 3 (chung)",
            [3],
            [
                "| Level | Vai trò | Mô tả |",
                "|-------|---------|--------|",
                "| **0** | TVV | Lên đơn hàng, **Confirm** khi đã thống nhất dịch vụ, sản phẩm, giá |",
                "| **1** | Kế toán | Kiểm tra SO đủ thông tin |",
                "| **2** | Kế toán | Tạo **Invoice** (doanh thu, phí thu hộ). Sai TK khi đã Payment → hủy Payment, sửa Invoice |",
                "| **3** | Kế toán | **Thu tiền** khách theo điều khoản hợp đồng |",
                "",
                "Luồng: **SO → Kiểm tra SO → Invoice → Payment**.",
                "",
            ],
        )
    )

    lines.extend(
        subsection(
            "2. Quy trình — hình slide 4 (chi tiết)",
            [4],
            [
                "Sơ đồ chi tiết: kiểm tra SO → Invoice → Payment (nhánh hủy/điều chỉnh nếu cần).",
                "",
            ],
            "Quy trình chi tiết",
        )
    )

    lines.extend(
        subsection(
            "3. Tạo Invoice — hình slide 4",
            [4],
            ["Tạo **Invoice** ghi nhận doanh thu từ đơn bán.", ""],
            "Tạo Invoice",
        )
    )

    lines.extend(
        subsection(
            "4. Tạo Invoice, hợp đồng — hình slide 6",
            [6],
            [
                "**Kiểm tra thông tin đơn hàng:**",
                "",
                "- Đơn **có hợp đồng**: thực hiện **(2) → (3) → (1) → (4)**",
                "- Đơn **không cần hợp đồng**: **(2) → (3)**, xong thực hiện **(1) → (4)**",
                "",
                "!!! note \"Ghi chú hợp đồng\"",
                "    - Đơn **có** hợp đồng: **bật màu xanh** ở bước (2)",
                "    - Đơn **không** hợp đồng: **tắt** bước (2), **tạo hợp đồng** ở bước (3)",
                "",
            ],
            "Invoice và hợp đồng",
        )
    )

    lines.extend(
        subsection(
            "5. Chi tiết tạo Invoice — hình slide 7",
            [7],
            [
                "Hóa đơn đã tạo — kiểm tra đã ghi nhận đúng:",
                "",
                "- **Sổ nhật ký**, **tài khoản** doanh thu / thu hộ, **giá tiền**",
                "- Đúng → chọn **Xác nhận**",
                "",
                "!!! note \"Tỷ giá manual\"",
                "    Chọn **Use manual Exchange Rate** để nhập tỷ giá; không chọn → hệ thống lấy tỷ giá mặc định.",
                "",
            ],
            "Chi tiết Invoice",
        )
    )

    lines.extend(["### 6. Tạo Payment — hình slide 8, 9, 10", "", slide_tag("8, 9, 10"), ""])
    lines.extend(
        [
            "- **Slide 8:** Tạo **Payment** thu tiền khách theo hợp đồng/đơn (đủ một lần hoặc nhiều đợt)",
            "- **Slide 9–10:** Xem và **in phiếu thu** cho khách ký",
            "    - CN Việt Nam: **01-TT / 02-TT**",
            "    - CN Mỹ: phiếu thu/chi theo mẫu chi nhánh",
            "",
        ]
    )
    for sn, cap in [(8, "Tạo Payment"), (9, "Phiếu thu"), (10, "In phiếu thu")]:
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn, cap, no_note=True))

    lines.extend(
        [
            "---",
            "",
            "## III. Các bút toán chi tiền {#iii-but-toan-chi}",
            "",
            slide_tag("11"),
            "",
            "| Nghiệp vụ | Bút toán (tóm tắt) |",
            "|-----------|-------------------|",
            "| Hoàn phí chương trình | Nợ 3388 (chi tiết ĐT) / Có 112, 111 |",
            "| Hoàn phí ký quỹ | Nợ 344 (chi tiết ĐT) / Có 112, 111 |",
            "| TT đối tác nước ngoài | TT: Nợ 331 / Có 112,111 — Kết chuyển: Nợ 3388 / Có 331 |",
            "| TT NCC trong nước | Nợ CP 641,642 (Cost Center) / Có 331 → TT: Nợ 331 / Có 112,111 |",
            "| Lương, BHXH, thuế… | TT: Nợ 3341, 3335… / Có 112,111 — Kết chuyển: Nợ 6425 / Có 3341, 3335 |",
            "",
        ]
    )
    lines.extend(img_block(img_dir, 11, "Bút toán chi tiền"))

    lines.extend(
        [
            "---",
            "",
            "## IV. Ghi nhận chi phí / mua hàng — Thanh toán NCC {#iv-ncc}",
            "",
        ]
    )

    lines.extend(
        subsection(
            "Quy trình — hình slide 12",
            [12],
            [
                "| Level | Vai trò | Mô tả |",
                "|-------|---------|--------|",
                "| **0** | User | Đề xuất mua hàng **đã duyệt**, đủ chứng từ |",
                "| **1** | User / KT | Tạo **Bill** → sau duyệt KT **Xác nhận** |",
                "| **2** | User | Tạo **đề nghị thanh toán** — loại TT đúng → Mục V |",
                "| **3** | Kế toán | **Chi tiền** theo Bill + đề nghị đã duyệt |",
                "",
                "**PO → Bill → Đề nghị thanh toán → Payment**",
                "",
            ],
            "Quy trình NCC",
        )
    )

    lines.extend(
        [
            "### Tạo Bill — hình slide 13; nội dung & hình slide 14",
            "",
            slide_tag("13, 14"),
            "",
            "- Chọn **nhà cung cấp** (chưa có → tạo mới)",
            "- **Loại thanh toán**, **sổ nhật ký**, **tiền tệ** (VND/USD)",
            "- Sản phẩm/dịch vụ, **TK chi phí**, số lượng, số tiền",
            "",
        ]
    )
    for sn in (13, 14):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn, "Tạo Bill", no_note=True))

    lines.extend(
        [
            "### Tạo Payment thanh toán — hình slide 15, 16",
            "",
            slide_tag("15, 16"),
            "",
            "1. **Xác nhận** Bill (sau khi đề nghị được duyệt)",
            "2. **Register Payment** — ngân hàng/tiền mặt, số tiền, nội dung",
            "",
        ]
    )
    for sn in (15, 16):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn, "Payment NCC", no_note=True))

    lines.extend(
        subsection(
            "In phiếu — hình slide 17",
            [17],
            ["In **phiếu chi** sau khi thanh toán.", ""],
            "In phiếu chi",
        )
    )

    lines.extend(
        [
            "---",
            "",
            "## V. Đề xuất thanh toán {#v-dntt}",
            "",
        ]
    )

    lines.extend(
        subsection(
            "Quy trình — hình slide 18",
            [18],
            [
                "| Level | Vai trò | Mô tả |",
                "|-------|---------|--------|",
                "| **0** | Người lập ĐNTT | Lập yêu cầu; thu thập chứng từ theo danh mục KT |",
                "| **1** | QLBP / TCN | Duyệt / Từ chối (ghi lý do) |",
                "| **2** | Kế toán / HR | Checklist chứng từ → Duyệt; sau BOD → thanh toán |",
                "| **3** | BOD | Duyệt / Từ chối |",
                "",
            ],
            "Quy trình DNTT",
        )
    )

    lines.extend(
        [
            "### Tạo đề xuất thanh toán — hình slide 19, 20, 21",
            "",
            slide_tag("19, 20, 21"),
            "",
            "**Thông tin chung:** Chi nhánh, phòng ban, phê duyệt cuối, loại yêu cầu, danh mục thanh toán.",
            "",
            "**Thông tin chi tiết:** Loại tiền, hình thức TT, số tiền, nội dung ĐNTT, STK (CK/Sec), thông tin HĐ.",
            "",
            "**QLBP/TCN** và **Checklist** chứng từ theo loại thanh toán.",
            "",
        ]
    )
    for sn in (19, 20, 21):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn, "Tạo đề xuất TT", no_note=True))

    lines.extend(
        subsection(
            "View đề nghị thanh toán — hình & nội dung slide 22",
            [22],
            [
                "Sau khi lưu ĐNTT → trên **Bill** hiển thị **View DNTT** → đính kèm hồ sơ → **Xác nhận** yêu cầu.",
                "",
            ],
            "View DNTT",
        )
    )

    lines.extend(
        subsection(
            "Xem trạng thái thanh toán — nội dung & hình slide 23",
            [23],
            [
                "Sau **phê duyệt** → quay lại Bill → **Xác nhận** → tạo **Payment** NCC.",
                "",
            ],
            "Trạng thái thanh toán",
        )
    )

    lines.extend(
        [
            "---",
            "",
            "## VI. Bút toán tổng hợp {#vi-but-toan-th}",
            "",
        ]
    )

    lines.extend(
        [
            "### Tạo bút toán (thu hộ / chi hộ theo đối tượng) — hình & nội dung slide 24, 25, 26",
            "",
            slide_tag("24, 25, 26"),
            "",
            "- Loại thanh toán, **sổ nhật ký**, loại tiền, Account, hạng mục, số tiền",
            "- Chọn **SO** (đối tượng chi hộ); nhiều đối tượng → thêm nhiều dòng SO",
            "- **Nợ:** chi hộ | **Có:** thu hộ — nhập số tiền, TK ngân hàng/tiền mặt",
            "- Sau tạo bút toán → **Tạo đề nghị thanh toán** (giống Mục V)",
            "",
        ]
    )
    for sn in (24, 25, 26):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(img_block(img_dir, sn, "Bút toán thu chi hộ", no_note=True))

    lines.extend(
        subsection(
            "Bút toán tổng hợp — slide 27",
            [27],
            [
                "Tạo đề nghị thanh toán giống **Mục V** → sau khi duyệt → quay lại bút toán → **Post (Vào sổ)**.",
                "",
                "!!! note",
                "    Đề nghị thanh toán tạo **giống** đề nghị thanh toán NCC.",
                "",
            ],
            "Post bút toán",
        )
    )

    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parents[1]
    img_dir = root / "docs" / "ke-toan" / "images" / "quy-trinh"
    nghiep = root / "docs" / "ke-toan" / "quy-trinh-nghiep-vu.md"
    hinh = root / "docs" / "ke-toan" / "quy-trinh-hinh-anh.md"

    nghiep.write_text(build_nghiep_vu(img_dir), encoding="utf-8")
    hinh.write_text(build_hinh_anh(img_dir), encoding="utf-8")
    print("Wrote", nghiep)
    print("Wrote", hinh)


if __name__ == "__main__":
    main()
