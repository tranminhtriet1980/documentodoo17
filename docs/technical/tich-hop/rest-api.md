# REST API (External API)

## Kích hoạt

Odoo 17 hỗ trợ **External JSON-2 API** (thay thế dần XML-RPC cho tích hợp mới — kiểm tra doc chính thức theo bản cài).

Tạo **API key** trên user:

**Preferences › Account Security › New API Key**

## Gọi HTTP (khái niệm)

```http
GET /json/2/res.partner/1
Authorization: bearer <API_KEY>
```

Chi tiết endpoint theo [Odoo 17 developer documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html).

## So sánh XML-RPC vs REST

| | XML-RPC | REST / JSON-2 |
|---|---------|----------------|
| Độ phổ biến | Rất phổ biến, ví dụ nhiều | Mới, chuẩn HTTP |
| Tooling | Mọi ngôn ngữ | Postman, OpenAPI-friendly |

## Best practice

- HTTPS bắt buộc
- API key rotate định kỳ
- Log request tích hợp riêng
- Idempotent cho `create` (external ID)

!!! note
    Custom module có thể expose controller `@http.route` riêng — cần review bảo mật.
