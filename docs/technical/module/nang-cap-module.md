# Nâng cấp & phát hành module

## Version trong manifest

`17.0.1.0.0` — `odoo_version.major.minor.patch.build`

Tăng version khi đổi XML/Python cần `-u`.

## Upgrade từ CLI

```bash
odoo-bin -d mydb -u my_module --stop-after-init
```

## Upgrade từ UI

**Apps › Module › Upgrade** (bật developer mode).

## Migration script

Thư mục `migrations/17.0.1.0.1/` — hàm `migrate(cr, version)` cho thay đổi schema phức tạp.

## Git workflow (khuyến nghị)

- Branch `17.0` cho code Odoo 17
- Tag release `v1.2.0` sau UAT
- Không sửa trực tiếp trên server production

## Dependency

Khai báo đúng `depends` — thiếu dependency gây lỗi install.

!!! warning
    Gỡ module (`uninstall`) có thể **xóa dữ liệu** model của module — backup trước.
