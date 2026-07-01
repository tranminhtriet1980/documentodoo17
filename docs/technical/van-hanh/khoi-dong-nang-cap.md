# Khởi động & nâng cấp

## Khởi động service

```bash
sudo systemctl start odoo
sudo systemctl status odoo
```

## Cập nhật module (upgrade)

```bash
./odoo-bin -c /etc/odoo/odoo.conf -d ten_database -u ten_module --stop-after-init
```

Nhiều module:

```bash
-u sale,purchase,stock --stop-after-init
```

## Nâng cấp phiên bản Odoo (16 → 17)

1. Backup DB + filestore
2. Clone code 17.0, cập nhật `addons_path`
3. Chạy upgrade trên **staging**
4. Kiểm tra custom module tương thích
5. `-u all` hoặc từng module theo kế hoạch
6. UAT nghiệp vụ (tab Functional)
7. Cutover production có cửa sổ bảo trì

!!! danger "`-u all` trên production"
    Chỉ chạy khi đã test staging; có thể lâu và khóa bảng.

## Restart sau đổi code Python

- Sửa `.py` → restart service (hoặc workers reload)
- Sửa XML/static → `-u module` hoặc upgrade app trong UI

Xem: [Sao lưu & phục hồi](sao-luu-phuc-hoi.md)
