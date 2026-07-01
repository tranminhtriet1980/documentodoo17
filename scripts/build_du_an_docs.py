"""Build quy-trinh-xlhs.md and phu-luc-hinh-anh.md from Mr Khanh PPTX (XLHS).

CANH BAO: Ghi de toan bo noi dung da sua tay trong 2 file .md tren.
Chi chay qua TrichAnhTuPptxDuAn.bat — KHONG goi trong BuildTaiLieu.bat.
"""
from pathlib import Path

from pptx_doc_utils import img_block, images_for_slide, slide_tag

IMG = "images/xlhs"
SOURCE = "Mr Khanh — *TÀI LIỆU XLHS _ODDO.pptx*"


def subsection(
    img_dir: Path,
    title: str,
    slide_nums: list[int],
    body: list[str],
    alt: str = "",
    img_class: str = "doc-screenshot",
) -> list[str]:
    block = [f"### {title}", ""]
    if slide_nums:
        if len(slide_nums) == 1:
            block.append(slide_tag(slide_nums[0]))
        else:
            block.append(f"*Hình slide {', '.join(str(s) for s in slide_nums)}*")
        block.append("")
    block.extend(body)
    for sn in slide_nums:
        block.extend(
            img_block(
                img_dir,
                IMG,
                sn,
                alt or title,
                no_note=True,
                skip_branding=False,
                prefer_sub02=True,
                img_class=img_class,
            )
        )
    return block


def build_nghiep_vu(img_dir: Path) -> str:
    lines = [
        "# Quy trình xử lý hồ sơ (XLHS) trên Odoo",
        "",
        "!!! info \"Nguồn tài liệu\"",
        f"    {SOURCE}. Áp dụng module **Project (QLHS)** trên **Odoo 17**.",
        "",
        "!!! tip \"Hình ảnh\"",
        "    - Trang này: quy trình + hình theo **thứ tự slide** PowerPoint",
        "    - [Phụ lục hình ảnh](phu-luc-hinh-anh.md) — xem riêng từng mục",
        "    - Cập nhật: `TrichAnhTuPptxDuAn.bat` → `BuildTaiLieu.bat`",
        "",
        "---",
        "",
        "## Chương I — Giới thiệu tổng quan",
        "",
        "### 1. Tổng quan Project (QLHS) — Slide 3",
        "",
        "Phần mềm quản lý **hồ sơ du học – du lịch – định cư** trên Odoo; liên kết **CRM** và **Kế toán**.",
        "",
    ]
    lines.extend(
        img_block(img_dir, IMG, 3, "Tổng quan QLHS", skip_branding=False, prefer_sub02=True)
    )
    lines.extend(
        [
            "### 2. Đăng nhập hệ thống — Slide 4, 5",
            "",
            "- URL: `https://internal.edupath.org.vn`",
            "- **Login with Email — Microsoft 365**",
            "",
        ]
    )
    for sn in (4, 5):
        lines.extend(
            img_block(
                img_dir, IMG, sn, "Đăng nhập",
                skip_branding=False, prefer_sub02=True, img_class="doc-screenshot-sm",
            )
        )

    lines.extend(
        [
            "### 3. Màn hình chính — Slide 6, 7, 8",
            "",
            "- **Trang chủ Project (QLHS):** danh mục hồ sơ theo nhóm (Định cư, Du học, Du lịch, Bảo lãnh…)",
            "- **My Task:** module To-do → My Task — theo hạn (Today, This Week, This Month…)",
            "",
        ]
    )
    for sn in (6, 7, 8):
        lines.extend(img_block(img_dir, IMG, sn, f"Màn hình slide {sn}", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 4. Thanh công cụ — Slide 9, 10",
            "",
            "- **Search** — tìm hồ sơ, task",
            "- **Thông báo** — tin nhắn, task tới due date",
            "",
        ]
    )
    for sn in (9, 10):
        lines.extend(img_block(img_dir, IMG, sn, "Thanh công cụ", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "---",
            "",
            "## Chương II — Quy trình xử lý hồ sơ",
            "",
            "### 1. Quy trình tiếp nhận — Slide 11, 12",
            "",
            "Luồng từ **Sales Order**: tiếp nhận → phê duyệt → khởi tạo dự án/hồ sơ.",
            "",
            "| Bước | Mô tả |",
            "|------|--------|",
            "| Tiếp nhận | Đủ thông tin: chi phí, nhu cầu, chương trình |",
            "| Kế toán | Kiểm tra thông tin khách tham gia chương trình |",
            "| Khởi tạo | Theo **SO** sau duyệt — mẫu dự án theo chương trình (EB3, Du học Mỹ, Canada/Úc, Du lịch…) |",
            "",
            "!!! note \"Slide 12\"",
            "    Sơ đồ quy trình tiếp nhận trên slide 12 (flowchart PowerPoint).",
            "",
        ]
    )
    lines.extend(img_block(img_dir, IMG, 11, "Tiếp nhận", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 2. Vai trò — Slide 14, 15",
            "",
            "| Vai trò | Trách nhiệm |",
            "|---------|-------------|",
            "| **Project Manager** | Chịu trách nhiệm chính; kiểm tra thông tin; khởi tạo; phân công task |",
            "| **Admission, Immigration, Visa, Translate** | Các stage lớn; hoàn thành task; liên hệ bộ phận khác |",
            "",
        ]
    )
    for sn in (14, 15):
        lines.extend(img_block(img_dir, IMG, sn, "Vai trò", skip_branding=False, prefer_sub02=True))

    programs = [
        ("2.1", "Quy trình XLHS EB3", 16),
        ("2.2", "Quy trình XLHS EB3-TT", 17),
        ("2.3", "Quy trình XLHS Du học Mỹ", 18),
        ("2.4", "Quy trình XLHS Du học Canada/Úc", 19),
        ("2.5", "Quy trình XLHS Du lịch Mỹ", 20),
        ("2.6", "Quy trình XLHS Du lịch Canada/Úc", 21),
        ("2.7", "Quy trình XLHS GHLT - CD F1", 22),
        ("2.8", "Quy trình XLHS Bảo lãnh (IN USA)", 23),
        ("2.9", "Quy trình XLHS Bảo lãnh (OUT USA)", 24),
    ]
    for code, title, sn in programs:
        lines.extend(
            [
                f"### {code}. {title} — Slide {sn}",
                "",
                "- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)",
                "- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó",
                "",
            ]
        )
        lines.extend(img_block(img_dir, IMG, sn, title, skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "---",
            "",
            "## Chương III — Thao tác nghiệp vụ xử lý hồ sơ",
            "",
            "### 1. Giới thiệu tính năng — Slide 26",
            "",
            "Module **Project** quản lý danh sách hồ sơ: tình trạng, ngày bắt đầu/kết thúc, tiến độ, công việc…",
            "",
        ]
    )
    lines.extend(img_block(img_dir, IMG, 26, "Tính năng Project", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 2. Tạo mới hồ sơ — Slide 27, 28",
            "",
            "**A. Tạo thủ công:** Module Project → **New** (Sales Admin).",
            "",
            "**B. Tự động từ SO:** Tên hồ sơ theo **Tên KH + Chương trình tư vấn – SO**",
            "(vd: *ĐOÀN VĂN ÚT – EB3 – SO00081*).",
            "",
        ]
    )
    for sn in (27, 28):
        lines.extend(img_block(img_dir, IMG, sn, "Tạo hồ sơ", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 3. Tiếp nhận hồ sơ — Slide 29, 30",
            "",
            "1. Nhận thông báo → menu **⋮** → **Settings**",
            "2. Bổ sung nhân sự (Admission, Leader…)",
            "3. Chuyển trạng thái tiếp nhận → khởi tạo **Task**",
            "",
        ]
    )
    for sn in (29, 30):
        lines.extend(img_block(img_dir, IMG, sn, "Tiếp nhận hồ sơ", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 4. Xử lý Task — Slide 31–39",
            "",
            "- Chọn task từ danh mục hồ sơ",
            "- Chuyển tình trạng: Request, Approved, Done…",
            "- Cập nhật thông tin hồ sơ; **SharePoint** (Create / Open Folder)",
            "- Task phụ — tick hoàn thành",
            "- **Ghi chú**, **Activities** (loại hành động, Due date)",
            "- **Giao** người thực hiện (@ tên)",
            "- Theo dõi trên **My Task**",
            "",
        ]
    )
    for sn in range(31, 40):
        lines.append(f"#### Slide {sn}")
        lines.append("")
        lines.extend(
            img_block(img_dir, IMG, sn, f"Task slide {sn}", skip_branding=False, prefer_sub02=True)
        )

    lines.extend(
        [
            "### 5. Ràng buộc chuyển trạng thái — Slide 40–43",
            "",
            "Chỉ chuyển trạng thái khi đủ điều kiện; thiếu thông tin → thông báo lỗi (vd. thiếu *Ngày nhận hồ sơ Admission*).",
            "",
            "!!! note \"File điều kiện\"",
            "    Chi tiết: *Điều kiện chuyển Status.xlsx* (trên slide 43).",
            "",
        ]
    )
    for sn in (40, 41, 42, 43):
        lines.extend(img_block(img_dir, IMG, sn, "Ràng buộc status", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "### 6. Thông báo tự động — Slide 44–46",
            "",
            "Khi đủ điều kiện tiến trình → email/thông báo tự động cho bộ phận liên quan (Internal).",
            "",
            "!!! note \"Automation\"",
            "    Danh sách mẫu: *Automation.xlsx* (slide 46).",
            "",
        ]
    )
    for sn in (44, 45, 46):
        lines.extend(img_block(img_dir, IMG, sn, "Thông báo tự động", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "---",
            "",
            "## Chương IV — Điều kiện phễu lọc — Slide 47–49",
            "",
            "| Điều kiện | Ý nghĩa |",
            "|-----------|---------|",
            "| **All** | Thoả tất cả điều kiện |",
            "| **Or** | Thoả một trong các điều kiện |",
            "| **=** / **!=** | Bằng / khác |",
            "| **is in** / **is not in** | Thuộc / không thuộc nhóm |",
            "| **is set** / **is not set** | Có giá trị / trống |",
            "",
            "Ví dụ: hồ sơ *Dung Ly*, stage *In Progress*, phụ trách *Thuý Hiên* và *Nguyệt*.",
            "",
        ]
    )
    for sn in (47, 48, 49):
        lines.extend(img_block(img_dir, IMG, sn, "Phễu lọc", skip_branding=False, prefer_sub02=True))

    lines.extend(
        [
            "---",
            "",
            "Xem thêm: [Phụ lục hình ảnh](phu-luc-hinh-anh.md) | [Nhiệm vụ](nhiem-vu.md) | [Timesheet](timesheet.md)",
            "",
        ]
    )
    return "\n".join(lines)


def build_phu_luc(img_dir: Path) -> str:
    lines = [
        "# Phụ lục — Hình ảnh XLHS (Project / QLHS)",
        "",
        f"Theo file {SOURCE}, **từ trên xuống** (theo phụ lục slide 2).",
        "",
        "[← Quy trình XLHS (đầy đủ)](quy-trinh-xlhs.md)",
        "",
        "---",
        "",
        "## Chương I — Giới thiệu tổng quan {#chuong-i}",
        "",
    ]

    ch1 = [
        ("1. Tổng quan Project (QLHS)", [3], []),
        ("2. Đăng nhập hệ thống", [4, 5], ["- Microsoft 365 / Email", ""], "", "doc-screenshot-sm"),
        (
            "3. Màn hình — Trang chủ & My Task",
            [6, 7, 8],
            ["- Danh mục: Định cư, Du học, Du lịch, Bảo lãnh", ""],
        ),
        ("4. Thanh công cụ — Search & Thông báo", [9, 10], []),
    ]
    for item in ch1:
        title, slides, body = item[0], item[1], item[2]
        alt = item[3] if len(item) > 3 else ""
        img_class = item[4] if len(item) > 4 else "doc-screenshot"
        lines.extend(subsection(img_dir, title, slides, body, alt, img_class))

    lines.extend(["---", "", "## Chương II — Quy trình XLHS {#chuong-ii}", ""])
    lines.extend(
        subsection(
            img_dir,
            "1. Quy trình tiếp nhận hồ sơ",
            [11],
            [
                "SO → Phê duyệt → Khởi tạo hồ sơ theo template chương trình.",
                "",
                "!!! note \"Slide 12\"",
                "    Sơ đồ flowchart trên PowerPoint (không tách ảnh).",
                "",
            ],
        )
    )
    lines.extend(
        subsection(
            img_dir,
            "Vai trò PM & Admission / Visa / Immigration",
            [14, 15],
            [],
        )
    )

    for code, title, sn in [
        ("2.1", "EB3", 16),
        ("2.2", "EB3-TT", 17),
        ("2.3", "Du học Mỹ", 18),
        ("2.4", "Du học Canada/Úc", 19),
        ("2.5", "Du lịch Mỹ", 20),
        ("2.6", "Du lịch Canada/Úc", 21),
        ("2.7", "GHLT - CD F1", 22),
        ("2.8", "Bảo lãnh IN USA", 23),
        ("2.9", "Bảo lãnh OUT USA", 24),
    ]:
        lines.extend(
            subsection(
                img_dir,
                f"{code}. Quy trình {title}",
                [sn],
                ["Stage trái → phải; Task trên → dưới.", ""],
            )
        )

    lines.extend(["---", "", "## Chương III — Thao tác nghiệp vụ {#chuong-iii}", ""])
    ch3_sections = [
        ("1. Giới thiệu tính năng Project", [26], []),
        ("2. Tạo mới hồ sơ (thủ công & từ SO)", [27, 28], []),
        ("3. Tiếp nhận hồ sơ", [29, 30], []),
        ("4.1–4.2 Chọn task & cập nhật", [31, 32], []),
        ("4.3 Trạng thái task & thông tin hồ sơ", [33], []),
        ("4.4 SharePoint folder", [34], []),
        ("4.5 Task phụ", [35], []),
        ("4.6 Ghi chú", [36], []),
        ("4.7 Activities", [37], []),
        ("4.8 Giao người thực hiện", [38], []),
        ("4.9 My Task", [39], []),
        ("5. Ràng buộc chuyển trạng thái", [40, 41, 42, 43], []),
        ("6. Thông báo tự động", [44, 45, 46], []),
    ]
    for title, slides, body in ch3_sections:
        lines.extend(subsection(img_dir, title, slides, body))

    lines.extend(["---", "", "## Chương IV — Phễu lọc {#chuong-iv}", ""])
    lines.extend(subsection(img_dir, "Điều kiện lọc cơ bản", [47, 48, 49], []))

    lines.append("---")
    lines.append("")
    lines.append("[← Quy trình XLHS](quy-trinh-xlhs.md)")
    lines.append("")
    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parents[1]
    img_dir = root / "docs" / "du-an" / "images" / "xlhs"
    if not img_dir.exists():
        raise SystemExit(f"Chua co anh: {img_dir}. Chay TrichAnhTuPptxDuAn.bat")

    out_nv = root / "docs" / "du-an" / "quy-trinh-xlhs.md"
    out_pl = root / "docs" / "du-an" / "phu-luc-hinh-anh.md"
    out_nv.write_text(build_nghiep_vu(img_dir), encoding="utf-8")
    out_pl.write_text(build_phu_luc(img_dir), encoding="utf-8")
    print("Wrote", out_nv)
    print("Wrote", out_pl)


if __name__ == "__main__":
    main()
