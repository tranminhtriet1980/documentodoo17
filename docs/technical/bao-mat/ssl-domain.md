# SSL, domain & reverse proxy

## Nginx mẫu (HTTPS)

```nginx
server {
    listen 443 ssl;
    server_name odoo.congty.vn;

    ssl_certificate     /etc/letsencrypt/live/odoo.congty.vn/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/odoo.congty.vn/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8069;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }

    location /longpolling {
        proxy_pass http://127.0.0.1:8072;
    }
}
```

## odoo.conf

```ini
proxy_mode = True
```

## web.base.url

System parameter — phải khớp URL public (`https://odoo.congty.vn`).

Freeze nếu multi URL:

- Key: `web.base.url.freeze` = `True`

## Let's Encrypt

Certbot renew tự động — kiểm tra cron certbot.

!!! warning
    Mixed HTTP/HTTPS gây lỗi session và PDF link.
