# Kiến trúc Odoo 17

## Mô hình 3 tầng

| Tầng | Thành phần | Vai trò |
|------|------------|---------|
| **Presentation** | Web client (OWL/JS), Website | Giao diện trình duyệt |
| **Business** | Python ORM, modules (addons) | Logic nghiệp vụ, workflow |
| **Data** | PostgreSQL | Lưu trữ bản ghi, transaction |

## Module (Addon)

Mỗi app (CRM, Stock…) là một hoặc nhiều **module** trong thư mục `addons/`:

- `__manifest__.py` — metadata, dependency
- `models/` — Python ORM
- `views/` — XML UI
- `security/` — groups, access rights
- `data/` — XML/CSV khởi tạo

## Multi-database

Một process Odoo phục vụ **nhiều database** — mỗi công ty/khách hàng thường một DB riêng (on-premise).

## Worker & cron

- **HTTP workers** — xử lý request web
- **Cron jobs** — `ir.cron` chạy tác vụ định kỳ (email queue, reorder rules…)
- **Longpolling / bus** — Discuss, notification (có thể cần gevent hoặc proxy riêng)

Xem: [Triển khai](trien-khai.md) | [Cấu trúc module](../module/cau-truc-module.md)
