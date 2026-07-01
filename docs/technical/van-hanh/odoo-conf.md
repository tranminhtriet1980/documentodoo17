# File cấu hình odoo.conf

## Vị trí

Thường `/etc/odoo/odoo.conf` hoặc tham số `-c /path/odoo.conf`.

## Tham số thường dùng

```ini
[options]
admin_passwd = master_password_change_me
db_host = localhost
db_port = 5432
db_user = odoo
db_password = secret
addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom
data_dir = /var/lib/odoo
http_port = 8069
workers = 4
max_cron_threads = 2
logfile = /var/log/odoo/odoo.log
log_level = info
proxy_mode = True
```

| Tham số | Ý nghĩa |
|---------|---------|
| `admin_passwd` | Master password (manage databases) |
| `addons_path` | Danh sách thư mục module, phân cách dấu phẩy |
| `data_dir` | Filestore + session |
| `workers` | Multi-process (production) |
| `proxy_mode` | Bật khi sau Nginx (URL, HTTPS header) |
| `dbfilter` | Regex lọc DB hiển thị (multi-tenant) |

## Bảo mật file

```bash
chmod 640 odoo.conf
chown odoo:odoo odoo.conf
```

Không commit `odoo.conf` chứa mật khẩu vào Git.

Xem: [SSL & domain](../bao-mat/ssl-domain.md)
