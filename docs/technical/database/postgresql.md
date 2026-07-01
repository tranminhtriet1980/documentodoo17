# PostgreSQL với Odoo

## Vai trò

Odoo dùng PostgreSQL làm **nguồn dữ liệu duy nhất** — không dùng MySQL/SQLite production.

## User & quyền

Tạo role riêng cho Odoo:

```sql
CREATE USER odoo WITH PASSWORD 'strong_password';
CREATE DATABASE odoo_prod OWNER odoo;
```

Odoo tự tạo bảng khi `-i base`. Không chỉnh schema thủ công trừ khi biết rõ hậu quả.

## Kết nối

Cấu hình trong `odoo.conf`: `db_host`, `db_port`, `db_user`, `db_password`.

## Hiệu năng

- `shared_buffers`, `work_mem` — tune theo RAM server
- Index — Odoo ORM tạo sẵn; tránh query SQL trực tiếp trên production
- **Connection pool** — `db_maxconn` trong odoo.conf khi nhiều worker

## Multi-database

List DB: `http://server:8069/web/database/manager` (cần `admin_passwd`).

`dbfilter` hạn chế DB theo hostname:

```ini
dbfilter = ^%d$
```

Xem: [Backup & restore](backup-restore.md) | [Multi-company](multi-company.md)
