# Backup & restore PostgreSQL

## Backup (pg_dump)

```bash
pg_dump -Fc -f odoo_prod_$(date +%Y%m%d).dump odoo_prod
```

Format custom `-Fc` nén, phục hồi linh hoạt.

## Backup plain SQL

```bash
pg_dump odoo_prod > odoo_prod.sql
```

## Restore

```bash
createdb odoo_restore_test
pg_restore -d odoo_restore_test odoo_prod_20250101.dump
```

Hoặc:

```bash
psql odoo_restore_test < odoo_prod.sql
```

## Filestore

```bash
rsync -av /var/lib/odoo/filestore/odoo_prod/ /backup/filestore_odoo_prod/
```

Sau restore DB, **tên thư mục filestore** phải trùng tên database.

## Odoo Online / Odoo.sh

Backup do nền tảng quản lý — tải qua panel hoặc API support.

!!! danger
    Không restore bản production lên DB dev có email gateway thật — rủi ro gửi nhầm mail.
