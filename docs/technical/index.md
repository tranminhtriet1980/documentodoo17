# Kỹ Thuật

!!! info "Đối tượng: Developer"
    Dành cho **Developer**. Tài liệu mô tả **kiến trúc kỹ thuật, cấu trúc dữ liệu, API, mô hình dữ liệu, mã nguồn** và các thành phần cần thiết để **phát triển, bảo trì hoặc mở rộng** hệ thống.

Phần **Technical** dành cho **IT, quản trị hệ thống và developer**: triển khai, vận hành, database, module tùy chỉnh, tích hợp và bảo mật hạ tầng.

## Ai nên đọc phần này?

- **System admin** — server, backup, SSL
- **Odoo implementer** — cài module, nâng cấp, debug
- **Developer** — Python, XML, API

## Không nằm trong phần Technical

Hướng dẫn *“bấm nút nào để tạo báo giá”*, *“phê duyệt nghỉ phép”* → tab **[Hướng dẫn người dùng](../huong-dan/index.md)**. Đặc tả chức năng đang phát triển → tab **[Chức năng](../functional/index.md)**.

## Cấu trúc

| STT | Nhóm | Nội dung |
|-----|------|----------|
| I | [Tổng quan](tong-quan/kien-truc.md) | Kiến trúc Odoo, phiên bản, mô hình triển khai |
| II | [Cài đặt & vận hành](van-hanh/cai-dat-server.md) | Server, `odoo.conf`, khởi động, nâng cấp |
| III | [Cơ sở dữ liệu](database/postgresql.md) | PostgreSQL, backup |
| IV | [Module & mã nguồn](module/cau-truc-module.md) | Cấu trúc addon, developer mode |
| V | [Tích hợp & API](tich-hop/xml-rpc.md) | XML-RPC, REST, email gateway |
| VI | [Bảo mật kỹ thuật](bao-mat/quyen-ky-thuat.md) | Record rules, SSL, system parameters |

```mermaid
flowchart TB
    subgraph functional [Hướng dẫn người dùng]
        U[Người dùng nghiệp vụ]
        P[Quy trình & màn hình Odoo]
    end
    subgraph technical [Kỹ thuật - Technical]
        S[Server / odoo.conf]
        D[(PostgreSQL)]
        M[Module / API]
    end
    U --> P
    P --> S
    S --> D
    M --> S
```

!!! danger "Môi trường production"
    Thao tác backup, nâng cấp, sửa database chỉ thực hiện trên bản **staging** trước, có kế hoạch rollback.
