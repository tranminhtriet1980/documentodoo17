# Email gateway & webhook

## Incoming mail → CRM / Helpdesk

1. **Cài đặt › Technical › Incoming Mail Servers**
2. IMAP/POP hoặc alias `catchall@domain.com`
3. Gán **Alias** trên Sales Team / Project

Lead tự tạo khi email đến.

## Outgoing mail

**Outgoing Mail Servers** — SMTP (Office 365, Gmail relay, SendGrid…).

Dùng `mail.template` gửi từ automation.

## Webhook tùy chỉnh

Module custom:

```python
from odoo import http

class WebhookController(http.Controller):
    @http.route('/api/webhook/order', type='json', auth='public', methods=['POST'], csrf=False)
    def order_webhook(self, **kw):
        # validate token, process payload
        return {'status': 'ok'}
```

- `auth='public'` + **token header** bắt buộc
- Không expose endpoint không xác thực

## Queue

Mail lớn dùng `mail.mail` queue + cron — tránh timeout HTTP.

Phía user: [Thảo luận](../../productivity/thao-luan.md)
