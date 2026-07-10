# Hướng dẫn người dùng

!!! info "Đối tượng: Người dùng cuối"
    Dành cho **người dùng cuối** trong quá trình làm việc hằng ngày. Tài liệu tập trung vào các **thao tác trên giao diện** và **quy trình sử dụng** chức năng đã được triển khai, **không** giải thích chi tiết về thiết kế nghiệp vụ hoặc mã nguồn.

Phần **Hướng dẫn người dùng** mô tả **cách sử dụng các tính năng đã chạy** của Odoo 17 trong công việc hàng ngày: quy trình nghiệp vụ, màn hình, nút bấm, báo cáo.

## Ai nên đọc phần này?

- Nhân viên **Bán hàng / CRM**
- **Kế toán**, **thủ kho**, **mua hàng**
- **HR**, **marketing**, **dự án**
- **Quản trị viên nghiệp vụ** (cài app, tạo user, phân quyền cơ bản)

## Phân biệt với các phần khác

| Phần | Trả lời câu hỏi | Đối tượng |
|------|-----------------|-----------|
| **Hướng dẫn người dùng** (phần này) | *“Bấm nút nào để làm việc X?”* — tính năng **đã có** | Người dùng nghiệp vụ |
| **[Chức năng](../functional/index.md)** | *“Chức năng Y sắp có sẽ hoạt động thế nào?”* — đặc tả chức năng **đang phát triển** | BA, chủ nhiệm dự án, người nghiệm thu |
| **[Kỹ Thuật](../technical/index.md)** | *“Cài server / backup / viết module thế nào?”* — hạ tầng & mã nguồn | IT, admin, developer |

## Không nằm trong phần này

- Cài Odoo trên server, file `odoo.conf`, backup PostgreSQL → **[Kỹ thuật](../technical/index.md)**
- Viết module Python, kế thừa view XML, XML-RPC / API → **[Kỹ thuật](../technical/index.md)**
- Đặc tả chức năng chưa release (còn thiết kế/đang code) → **[Chức năng](../functional/index.md)**

## Cấu trúc

| STT | Nhóm | Mô tả |
|-----|------|--------|
| I | [Bắt đầu](../gioi-thieu/odoo17.md) | Giới thiệu, giao diện, đăng nhập |
| II | [Bán hàng](../ban-hang/index.md) | CRM, báo giá, đơn bán |
| III | [Mua hàng](../mua-hang/index.md) | PO, nhà cung cấp |
| IV | [Kho vận](../kho/index.md) | Nhập/xuất, tồn |
| V | [Kế toán](../ke-toan/index.md) | Hóa đơn, thanh toán |
| VI | [Nhân sự](../nhan-su/index.md) | HR, nghỉ phép |
| VII | [Dự án](../du-an/index.md) | Task, timesheet |
| VIII | [Website](../website/index.md) | Site, eCommerce |
| IX | [Marketing](../marketing/index.md) | Email, sự kiện |
| X | [Sản xuất](../san-xuat/index.md) | BOM, MO |
| XI | [Năng suất](../productivity/index.md) | Discuss, lịch |
| XII | [Quản trị nghiệp vụ](../cai-dat/index.md) | App, user, quyền (góc admin vận hành) |

!!! tip "Đường dẫn menu"
    Ghi dạng **Ứng dụng › Menu › Mục** — ví dụ **CRM › Cấu hình › Cài đặt**.
