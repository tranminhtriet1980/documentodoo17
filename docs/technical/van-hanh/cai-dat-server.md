# Cài đặt server (On-premise)

## Yêu cầu tối thiểu (tham khảo)

| Thành phần | Phiên bản gợi ý |
|------------|-----------------|
| **OS** | Ubuntu 22.04 LTS / Debian 12 |
| **Python** | 3.10+ (theo Odoo 17 requirement) |
| **PostgreSQL** | 14+ |
| **RAM** | 4 GB+ (production 16 GB+) |

## Các bước tóm tắt

1. Cài PostgreSQL, tạo user `odoo`
2. Clone `odoo/odoo` branch **17.0**
3. Tạo virtualenv, `pip install -r requirements.txt`
4. Tạo database: `createdb odoo_prod`
5. Chạy lần đầu: `odoo-bin -d odoo_prod -i base --stop-after-init`
6. Cấu hình **systemd** hoặc Windows service
7. Cấu hình **Nginx** reverse proxy + SSL

## Thư mục quan trọng

| Đường dẫn | Nội dung |
|-----------|----------|
| `addons/` | Module community + custom |
| `data/filestore/` | File đính kèm |
| `odoo.conf` | Cấu hình runtime |

## User hệ thống

Chạy Odoo bằng user không phải root, quyền ghi `filestore` và log.

Xem: [odoo.conf](odoo-conf.md) | [Khởi động & nâng cấp](khoi-dong-nang-cap.md)

!!! note "Windows"
    Dev trên Windows dùng PowerShell; production Linux được khuyến nghị.
