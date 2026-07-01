# Sao lưu & phục hồi (tổng quan)

## Thành phần cần backup

| Thành phần | Công cụ |
|------------|---------|
| **Database** | `pg_dump` |
| **Filestore** | `rsync` / archive thư mục `data_dir/filestore/<db>` |
| **Custom addons** | Git repository |
| **odoo.conf** | Copy file (không lộ secret) |

## Lịch backup khuyến nghị

- **Full DB** — hàng ngày (off-peak)
- **Filestore** — hàng ngày hoặc incremental
- **Giữ bản** — 7 ngày daily + 4 weekly (tùy chính sách)

## Phục hồi nhanh

1. Dừng Odoo
2. Tạo DB mới hoặc drop & restore
3. `pg_restore` / `psql < dump.sql`
4. Đồng bộ filestore đúng tên database
5. Khởi động Odoo, kiểm tra attachment

Chi tiết: [Backup PostgreSQL](../database/backup-restore.md)

!!! warning
    Restore thử trên server **khác** trước khi ghi đè production.
