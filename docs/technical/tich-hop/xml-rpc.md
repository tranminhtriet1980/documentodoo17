# XML-RPC & JSON-RPC

## Endpoint

```
POST http://server:8069/xmlrpc/2/common   # authenticate
POST http://server:8069/xmlrpc/2/object   # execute
```

## Xác thực (Python ví dụ)

```python
import xmlrpc.client

url = 'https://odoo.example.com'
db = 'odoo_prod'
username = 'api_user@company.com'
password = 'api_password'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
ids = models.execute_kw(db, uid, password,
    'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 5})
```

## execute_kw

| Tham số | Mô tả |
|---------|--------|
| model | Tên model (`sale.order`) |
| method | `search`, `read`, `create`, `write`, `unlink` |
| args | Tham số positional |
| kwargs | `fields`, `limit`, `context` |

## User API riêng

Tạo user **chỉ có quyền** cần thiết — không dùng admin.

## Giới hạn

- Không thay thế batch lớn — cân nhắc queue job
- Rate limit phía proxy nếu public internet

Xem: [REST API](rest-api.md)
