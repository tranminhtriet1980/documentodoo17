# GitHub → Docker (tài liệu Odoo 17)

Repo: **https://github.com/tranminhtriet1980/documentodoo17**

## Trên máy Docker — lần đầu

### Windows (CMD)

```bat
cd C:\Docker
git clone https://github.com/tranminhtriet1980/documentodoo17.git documentodoo17
cd documentodoo17
py -3 scripts\generate_htpasswd.py -p Edupath2026!
docker compose build
docker compose up -d
```

Hoặc:

```bat
scripts\DeployTuGitHub.bat
```

### Linux

```bash
sudo mkdir -p /opt
cd /opt
git clone https://github.com/tranminhtriet1980/documentodoo17.git documentodoo17
cd documentodoo17
python3 scripts/generate_htpasswd.py -p 'Edupath2026!'
docker compose build
docker compose up -d
```

## Cập nhật khi có thay đổi trên GitHub

**Quan trọng:** Phải `git pull` **và** `docker compose build --no-cache` — site được build **bên trong image**, không dùng thư mục `site/` cũ.

### Windows server (`C:\Docker\docs`)

```bat
cd C:\Docker\docs
scripts\CapNhatTrenServer.bat
```

Hoặc tay:

```bat
cd C:\Docker\docs
git pull
docker compose down
docker compose build --no-cache
docker compose up -d
```

### Linux server

```bash
cd /opt/documentodoo17
./scripts/cap-nhat-tren-server.sh
```

## Server chưa thấy dữ liệu mới?

1. Server **chưa phải git repo** → ghi đè như lần đầu (clone lại).
2. Chỉ `docker compose restart` → **không đủ**, phải `build --no-cache`.
3. Bản Docker cũ mount `./site` → xóa thư mục `site/` cũ, dùng repo mới (không cần `site/` local).
4. Trình duyệt cache → thử Ctrl+F5 hoặc tab ẩn danh.

## Truy cập

| | URL |
|---|-----|
| HTTP | http://\<IP-máy\>:4546/ |
| HTTPS | https://\<IP-máy\>:4547/ |
| Kỹ thuật | user `technical`, mật khẩu theo `config/htpasswd` |

## Đổi mật khẩu Kỹ thuật

```bat
py -3 scripts\generate_htpasswd.py
docker compose restart
```
