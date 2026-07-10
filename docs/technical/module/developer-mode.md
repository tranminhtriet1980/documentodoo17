# Developer mode

## Bật

**Cài đặt › Kích hoạt chế độ nhà phát triển**

Hoặc URL: `?debug=1` (chỉ dùng dev/staging).

## Menu Technical hiện thêm

- **Models**, **Views**, **Actions**, **Security**
- Chỉnh XML view qua UI (không khuyến nghị trên production)
- **Edit Metadata** trên field

## Assets debug

`?debug=assets` — load JS/CSS không bundle (chậm, debug frontend).

## Log level

Trong `odoo.conf`:

```ini
log_level = debug
log_handler = odoo.tools.convert:DEBUG
```

## Shell Odoo

```bash
odoo-bin shell -d mydb
```

```python
env['sale.order'].search_count([])
```

!!! danger
    Không bật debug trên production cho user thường — lộ cấu trúc hệ thống.

Phía nghiệp vụ: [Quản trị ứng dụng](../../cai-dat/ung-dung.md) (Chức năng).
