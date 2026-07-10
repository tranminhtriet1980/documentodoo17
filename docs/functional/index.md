# Chức năng — Đặc tả chức năng

!!! info "Đối tượng: BA, Consultant, Key User"
    Dành cho **BA, Consultant và Key User**. Tài liệu mô tả **yêu cầu nghiệp vụ, quy trình, cấu hình và nguyên tắc hoạt động** của hệ thống, phục vụ **triển khai, kiểm thử và đào tạo**.

Phần **Chức năng** đặc tả **chức năng của hệ thống** (đang phát triển hoặc đã triển khai) trên Odoo 17: mục tiêu nghiệp vụ, phạm vi, luồng xử lý, màn hình, cấu hình, quy tắc và tiêu chí nghiệm thu.

!!! info "Khác gì với Hướng dẫn người dùng?"
    - **[Hướng dẫn người dùng](../huong-dan/index.md)** — tính năng **đã chạy**, hướng dẫn thao tác.
    - **Chức năng** (phần này) — chức năng **chưa xong** (còn thiết kế / đang code / đang thử nghiệm), viết dưới dạng **đặc tả**.
    - Khi một chức năng hoàn thành và lên production → chuyển nội dung sang **Hướng dẫn người dùng**.

## Ai nên đọc / viết phần này?

- **BA / phân tích nghiệp vụ** — viết đặc tả, chốt phạm vi
- **Chủ nhiệm dự án / trưởng nhóm** — theo dõi tiến độ, ưu tiên
- **Người nghiệm thu (UAT)** — đối chiếu tiêu chí nghiệm thu
- **Developer** — hiểu yêu cầu nghiệp vụ trước khi code (chi tiết kỹ thuật vẫn ở tab **[Kỹ thuật](../technical/index.md)**)

## Trạng thái chức năng

| Trạng thái | Ý nghĩa |
|------------|---------|
| 🟡 **Đề xuất** | Ý tưởng/yêu cầu mới, chưa chốt phạm vi |
| 🔵 **Đang phát triển** | Đã chốt đặc tả, đang code |
| 🟣 **Thử nghiệm (UAT)** | Có bản chạy thử, đang nghiệm thu |
| 🟢 **Hoàn thành** | Đã release → chuyển sang *Hướng dẫn người dùng* |
| ⚪ **Tạm dừng** | Hoãn lại / chờ quyết định |

## Danh sách chức năng đang theo dõi

> Thêm dòng cho mỗi chức năng và tạo trang đặc tả tương ứng từ [mẫu đặc tả](mau-dac-ta-chuc-nang.md).

| STT | Chức năng | Module | Trạng thái | Đặc tả |
|----|-----------|--------|------------|--------|
| 1 | Phiếu nhập/xuất kho Edupath | `edupath_stock` | 🔵 Đang phát triển | [Xem](edupath-stock.md) |
| 2 | Edupath ERP — CRM & Hồ sơ dịch vụ | `lead_view` | 🔵 Đang phát triển | [Xem](lead-view.md) |
| 3 | Email Marketing Edupath | `Edupath_Email_Marketing` | 🔵 Đang phát triển | [Xem](edupath-email-marketing.md) |
| 4 | Dashboard Quản trị Hồ sơ | `edupath_project_dashboard` | 🔵 Đang phát triển | [Xem](edupath-project-dashboard.md) |
| 5 | Quản lý Thanh toán | `fin_qlthanhtoan` | 🔵 Đang phát triển | [Xem](fin-qlthanhtoan.md) |
| 6 | Hỗ trợ CNTT (Service Desk) | `th_service_desk` | 🔵 Đang phát triển | [Xem](th-service-desk.md) |
| 7 | Bộ Danh Mục | `danhmuc` | 🔵 Đang phát triển | [Xem](danhmuc.md) |

## Cách thêm một chức năng mới

1. Sao chép [Mẫu đặc tả chức năng](mau-dac-ta-chuc-nang.md) thành file mới trong thư mục `docs/functional/`, đặt tên theo chức năng, ví dụ `ten-chuc-nang.md`.
2. Điền các mục trong mẫu (mục tiêu, phạm vi, luồng, màn hình, tiêu chí nghiệm thu…).
3. Thêm 1 dòng vào **Danh sách chức năng đang theo dõi** ở trên.
4. Khai báo trang mới trong `nav:` của `mkdocs.yml` dưới nhóm **Chức năng**.

!!! tip "Nguyên tắc viết đặc tả"
    Mô tả **chức năng phải làm gì** (góc nghiệp vụ), không mô tả **cách code**. Chi tiết kỹ thuật (model, field, view XML) để ở tab **Kỹ thuật** và liên kết chéo khi cần.
