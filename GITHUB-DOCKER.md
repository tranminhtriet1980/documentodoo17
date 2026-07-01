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

```bat
cd C:\Docker\documentodoo17
git pull
docker compose build
docker compose up -d
```

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
