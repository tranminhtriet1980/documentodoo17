# Docker — Tài liệu Odoo 17

## Yêu cầu

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows) hoặc Docker trên Linux
- Đã build thư mục **`site/`** (chạy `BuildTaiLieu.bat` ở thư mục gốc project)

## Port

| Giao thức | URL ví dụ |
|-----------|-----------|
| **HTTP** | `http://192.168.1.10:4546/index.html` |
| **HTTPS** | `https://192.168.1.10:4547/index.html` |

Map Docker: `4546:4546` (HTTP), `4547:4547` (HTTPS). Cùng một cổng TCP không thể vừa HTTP vừa HTTPS nên HTTPS dùng **4547**.

## Trên máy đang soạn tài liệu (build + chạy thử)

```bat
BuildTaiLieu.bat
ChayDocker.bat
```

Hoặc:

```bat
docker compose build
docker compose up -d
```

## Copy sang máy khác

1. Chạy **`DongGoiDocker.bat`** (copy tự động sang `C:\Docker\docs`), hoặc copy tay:
   - `Dockerfile`
   - `docker-compose.yml`
   - **`nginx.conf`** (cùng cấp với Dockerfile — bắt buộc)
   - `.dockerignore` (tùy chọn)
   - **`site/`** (bắt buộc, có `index.html`)
2. Trên máy mới cài Docker, mở CMD tại folder đó:

```bat
docker compose build
docker compose up -d
```

3. Mở trình duyệt: `http://localhost:4546/`

## Cập nhật nội dung

1. Sửa file trong `docs/`, chạy `BuildTaiLieu.bat`
2. Trên máy Docker:

```bat
docker compose restart
```

(vì `docker-compose.yml` mount `./site` — chỉ cần restart, không bắt buộc build lại image)

## Lệnh hữu ích

```bat
docker compose ps
docker compose logs -f
docker compose down
```

## HTTPS

Image tự tạo chứng chỉ **tự ký** khi khởi động. Trình duyệt sẽ cảnh báo — chọn tiếp tục (môi trường nội bộ). Muốn chứng chỉ thật: thay bằng reverse proxy (IIS/nginx) phía trước.
