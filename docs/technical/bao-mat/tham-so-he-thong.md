# Tham số hệ thống (ir.config_parameter)

## Truy cập

**Cài đặt › Technical › System Parameters** (developer mode)

Hoặc code:

```python
self.env['ir.config_parameter'].sudo().get_param('web.base.url')
self.env['ir.config_parameter'].sudo().set_param('my.key', 'value')
```

## Tham số quan trọng

| Key | Ý nghĩa |
|-----|---------|
| `web.base.url` | URL công khai Odoo |
| `database.secret` | Secret nội bộ |
| `mail.catchall.domain` | Domain nhận mail |
| Custom `my_module.*` | Cấu hình module riêng |

## XML data (module)

```xml
<record id="param_my_setting" model="ir.config_parameter">
    <field name="key">my_module.api_url</field>
    <field name="value">https://api.example.com</field>
</record>
```

## Bảo mật

- Không lưu password plain text nếu có Secret store
- Phân quyền chỉ admin đọc Technical menu
- Audit thay đổi parameter nhạy cảm

## Documentation URL tùy chỉnh (tích hợp tài liệu)

Để link Help trong Odoo trỏ docs nội bộ, custom module có thể override widget `DocumentationLink` hoặc dùng URL đầy đủ trong `documentation="https://docs..."` trên view Settings.

Phía user đọc tài liệu: mở `MoTaiLieu.bat` hoặc host `site/` nội bộ.
