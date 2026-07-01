# Quy trình xử lý nghiệp vụ kế toán

!!! info "Nguồn tài liệu"
    MR UT — *01. Quy trình xử lý nghiệp vụ kế toán - odoo 18*. Áp dụng tương tự **Odoo 17**.

!!! tip "Hình ảnh"
    - Trang này: quy trình + hình theo **đúng thứ tự slide** PowerPoint
    - [Phụ lục hình ảnh](quy-trinh-hinh-anh.md) — xem riêng từng slide
    - Sửa tay: `BuildTaiLieu.bat` — tạo lại từ PPTX (ghi đè): `TrichAnhTuPptx.bat`

---

## I. Khai báo hệ thống tài khoản

Cấu hình trước khi vận hành (chi tiết: file quản lý hệ thống tài khoản & Cost Center):

| STT | Hạng mục |
|-----|----------|
| 1 | **Tài khoản** kế toán |
| 2 | **Tài khoản ngân hàng** |
| 3 | **Sổ nhật ký** kế toán |
| 4 | **Cost Center** |

![Hệ thống tài khoản](images/quy-trinh/slide-02-03.jpg){ .doc-screenshot-sm }

![Hệ thống tài khoản](images/quy-trinh/slide-02-04.jpg){ .doc-screenshot-sm }

---

## II. Ghi nhận doanh thu — Thu tiền khách hàng

### 1. Quy trình — tổng quan

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | TVV | Lên đơn hàng, **Confirm** khi đã thống nhất dịch vụ, sản phẩm, giá với khách |
| **1** | Kế toán | Kiểm tra SO đủ thông tin |
| **2** | Kế toán | Tạo **Invoice** (doanh thu, phí thu hộ). Sai TK sau Payment → **hủy Payment**, sửa Invoice |
| **3** | Kế toán | **Thu tiền** khách theo điều khoản hợp đồng |

```mermaid
flowchart LR
    SO[SO] --> K{KT kiểm tra}
    K -->|OK| INV[Invoice]
    INV --> PAY[Payment]
```
![Quy trình tổng quan](images/quy-trinh/quy-trinh-ke-toan.png){ .doc-screenshot }
### 2. Quy trình — chi tiết

Luồng: **SO → Kiểm tra thông tin SO → Invoice → Payment** (có nhánh hủy/điều chỉnh nếu sai).

![Quy trình doanh thu](images/quy-trinh/slide-04-03.jpg){ .doc-screenshot }

### 3. Tạo Invoice

Tạo hóa đơn ghi nhận doanh thu từ đơn bán.

![Tạo Invoice](images/quy-trinh/slide-04-03.jpg){ .doc-screenshot }

### 4. Tạo Invoice & hợp đồng

**Kiểm tra thông tin đơn hàng:**

| Trường hợp | Thứ tự |
|------------|--------|
| **Có hợp đồng** | (2) → (3) → (1) → (4) |
| **Không cần hợp đồng** | (2) → (3), sau đó (1) → (4) |

!!! note "Cờ hợp đồng trên SO"
    - Đơn **có** hợp đồng: **bật màu xanh** ở bước (2)
    - Đơn **không** hợp đồng: **tắt** bước (2), tạo hợp đồng ở bước (3)

![Invoice và hợp đồng](images/quy-trinh/slide-06-03.jpg){ .doc-screenshot }

![Invoice và hợp đồng](images/quy-trinh/slide-06-04.jpg){ .doc-screenshot }

### 5. Chi tiết tạo Invoice — xác nhận

Kiểm tra hóa đơn đã ghi nhận đúng:

- **Sổ nhật ký**, **tài khoản** doanh thu / thu hộ, **giá tiền**
- Đúng → chọn **Xác nhận** (Post/Confirm)

!!! note "Tỷ giá manual"
    Bật **Use manual Exchange Rate** để nhập tỷ giá; không chọn → hệ thống lấy tỷ giá mặc định.

![Chi tiết Invoice](images/quy-trinh/slide-07-03.jpg){ .doc-screenshot }

### 6. Tạo Payment — thu tiền khách

- Tạo **Payment** thu tiền theo hợp đồng/đơn (đủ một lần hoặc nhiều đợt)
- Xem và **in phiếu thu** cho khách ký
    - CN Việt Nam: mẫu **01-TT / 02-TT**
    - CN Mỹ: phiếu thu/chi theo mẫu chi nhánh


![Slide 8](images/quy-trinh/slide-08-03.jpg){ .doc-screenshot }
![Slide 8](images/quy-trinh/slide-08-04.jpg){ .doc-screenshot }
![Slide 9](images/quy-trinh/slide-09-03.jpg){ .doc-screenshot }
![Slide 9](images/quy-trinh/slide-09-04.jpg){ .doc-screenshot }
![Slide 10](images/quy-trinh/slide-10-03.jpg){ .doc-screenshot }

---

## III. Các bút toán chi tiền

| Nghiệp vụ | Bút toán (tóm tắt) |
|-----------|-------------------|
| Hoàn phí chương trình | Nợ 3388 (chi tiết ĐT) / Có 112, 111 |
| Hoàn phí ký quỹ | Nợ 344 (chi tiết ĐT) / Có 112, 111 |
| TT đối tác nước ngoài | TT: Nợ 331 / Có 112,111 — Kết chuyển: Nợ 3388 / Có 331 |
| TT NCC trong nước | Nợ CP 641,642 (Cost Center) / Có 331 → TT: Nợ 331 / Có 112,111 |
| Lương, BHXH, thuế… | TT: Nợ 3341, 3335… / Có 112,111 — Kết chuyển: Nợ 6425 / Có 3341, 3335 |

---

## IV. Ghi nhận chi phí / mua hàng — Thanh toán NCC

### 1. Quy trình

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | User | Đề xuất mua hàng **đã duyệt**, đủ chứng từ (HĐ, chứng từ CP…) |
| **1** | User / KT | Tạo **Bill**. Sau duyệt đề nghị → KT **Xác nhận** Bill |
| **2** | User | Tạo **đề nghị thanh toán** theo Bill — chọn **loại thanh toán** đúng → [Mục V](#v-de-xuat-thanh-toan) |
| **3** | Kế toán | **Chi tiền** theo Bill + đề nghị đã duyệt |

```mermaid
flowchart LR
    PO[PO / Mua hàng] --> BILL[Bill]
    BILL --> DNTT[Đề nghị TT]
    DNTT --> PAY[Payment]
    PAY --> PRINT[In phiếu chi]
```
![Quy trình thanh toán NCC](images/quy-trinh/quy-trinh-thanh-ncc.png){ .doc-screenshot }
!!! note "Slide 12"
    Slide gốc là **sơ đồ quy trình** trên PowerPoint (không có ảnh chụp Odoo).

### 2. Tạo Bill — ghi nhận hóa đơn mua

**Kế toán › Nhà cung cấp › Hóa đơn** (hoặc PO → Create Bill):

- Chọn **nhà cung cấp** (chưa có → tạo mới)
- **Loại thanh toán**, **sổ nhật ký**, **tiền tệ** (VND/USD)
- Chi tiết: sản phẩm/dịch vụ, **TK chi phí**, số lượng, số tiền
- Ghi nhận CP theo **Cost Center** (TK 641, 642…)

![Slide 13](images/quy-trinh/slide-13-03.jpg){ .doc-screenshot }

![Slide 14](images/quy-trinh/slide-14-03.jpg){ .doc-screenshot }

![Slide 14](images/quy-trinh/slide-14-04.jpg){ .doc-screenshot }

### 3. Tạo Payment thanh toán NCC (Slide 15, 16)

1. **Xác nhận** Bill (sau khi đề nghị được duyệt — Mục V)
2. **Register Payment** — chọn ngân hàng/tiền mặt, số tiền, nội dung

![Slide 15](images/quy-trinh/slide-15-03.jpg){ .doc-screenshot }

![Slide 15](images/quy-trinh/slide-15-04.jpg){ .doc-screenshot }

![Slide 16](images/quy-trinh/slide-16-03.jpg){ .doc-screenshot }

![Slide 16](images/quy-trinh/slide-16-04.jpg){ .doc-screenshot }

### 4. In phiếu chi

In phiếu chi sau khi thanh toán (mẫu theo chi nhánh).

![In phiếu chi](images/quy-trinh/slide-17-03.jpg){ .doc-screenshot }

![In phiếu chi](images/quy-trinh/slide-17-04.jpg){ .doc-screenshot }

---

## V. Đề xuất thanh toán (DNTT) {#v-de-xuat-thanh-toan}

### 1. Quy trình phê duyệt

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | Người lập ĐNTT | Lập yêu cầu; thu thập chứng từ theo **danh mục** KT |
| **1** | QLBP / TCN | Kiểm tra → Duyệt/Từ chối (ghi lý do). Áp dụng khi loại TT cần QLBP |
| **2** | Kế toán / HR | Kiểm tra + **Checklist** chứng từ → Duyệt/Từ chối. Sau BOD → thanh toán |
| **3** | BOD | Duyệt / Từ chối |

![Quy trình đề nghị thanh toán](images/quy-trinh/quy-trinh-dntt.png){ .doc-screenshot }
!!! note "Slide 18"
    Slide gốc là **sơ đồ quy trình** trên PowerPoint (không có ảnh chụp Odoo).

### 2. Tạo đề xuất thanh toán

**Thông tin chung:** Chi nhánh, phòng ban, người phê duyệt cuối, loại yêu cầu, danh mục thanh toán.

**Thông tin chi tiết:** Loại tiền, hình thức TT, số tiền, nội dung ĐNTT, STK (nếu CK/Sec), thông tin HĐ (nếu có).

**QLBP/TCN:** Thêm người duyệt nếu loại thanh toán đi qua QLBP/TCN.

**Checklist:** Đủ chứng từ, HĐ theo từng loại thanh toán.

![Slide 19](images/quy-trinh/slide-19-03.jpg){ .doc-screenshot }

![Slide 19](images/quy-trinh/slide-19-04.jpg){ .doc-screenshot }

![Slide 20](images/quy-trinh/slide-20-03.jpg){ .doc-screenshot }

![Slide 20](images/quy-trinh/slide-20-04.jpg){ .doc-screenshot }

![Slide 21](images/quy-trinh/slide-21-03.jpg){ .doc-screenshot }

![Slide 21](images/quy-trinh/slide-21-04.jpg){ .doc-screenshot }

### 3. View đề nghị thanh toán trên Bill (Slide 22)

1. Lưu đề nghị thanh toán
2. Trên **Bill** → nút **View DNTT**
3. Chọn **View DNTT** → đính kèm hồ sơ → **Xác nhận** yêu cầu thanh toán

![View DNTT](images/quy-trinh/slide-22-03.jpg){ .doc-screenshot }

![View DNTT](images/quy-trinh/slide-22-04.jpg){ .doc-screenshot }

### 4. Xem trạng thái & thanh toán sau duyệt

Sau khi **phê duyệt** → quay lại Bill → **Xác nhận** → tạo **Payment** NCC.

![Trạng thái thanh toán](images/quy-trinh/slide-23-03.jpg){ .doc-screenshot }

![Trạng thái thanh toán](images/quy-trinh/slide-23-04.jpg){ .doc-screenshot }

---

## VI. Bút toán tổng hợp — Không có hóa đơn

### 1. Tạo bút toán thu hộ / chi hộ

- Chọn loại thanh toán, **sổ nhật ký**, loại tiền, Account, hạng mục, số tiền
- Chọn **SO** (đối tượng chi hộ); nhiều đối tượng → thêm nhiều dòng SO
- **Nợ:** đối tượng **chi hộ** | **Có:** đối tượng **thu hộ**
- Nhập số tiền, TK ngân hàng/tiền mặt chi ra
- Sau khi tạo bút toán → **Tạo đề nghị thanh toán** (giống Mục V)

![Slide 24](images/quy-trinh/slide-24-03.jpg){ .doc-screenshot }

![Slide 24](images/quy-trinh/slide-24-04.jpg){ .doc-screenshot }

![Slide 25](images/quy-trinh/slide-25-03.jpg){ .doc-screenshot }

![Slide 25](images/quy-trinh/slide-25-04.jpg){ .doc-screenshot }

![Slide 26](images/quy-trinh/slide-26-03.jpg){ .doc-screenshot }

![Slide 26](images/quy-trinh/slide-26-04.jpg){ .doc-screenshot }

### 2. Đề nghị thanh toán & vào sổ

Tạo đề nghị thanh toán giống **Mục V**. Sau khi ĐNTT **được duyệt** → quay lại bút toán → **Post (Vào sổ)**.

!!! note
    Đề nghị thanh toán tạo **giống** đề nghị thanh toán NCC.

---

Xem thêm: [Phụ lục hình ảnh](quy-trinh-hinh-anh.md) | [Hóa đơn](hoa-don.md) | [Thanh toán](thanh-toan.md) | [Sổ cái](so-cai.md)

!!! note "Slide 27"
    Slide gốc là **sơ đồ quy trình** trên PowerPoint (không có ảnh chụp Odoo).
