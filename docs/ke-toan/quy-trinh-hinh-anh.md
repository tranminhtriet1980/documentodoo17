# Phụ lục — Hình ảnh quy trình kế toán

Theo file *01. Quy trình xử lý nghiệp vụ kế toán - odoo 18* (MR UT), **từ trên xuống**.

[← Quy trình nghiệp vụ (đầy đủ)](quy-trinh-nghiep-vu.md)

---

## I. Khai báo hệ thống tài khoản {#i-he-thong}

Hệ thống **tài khoản kế toán**, **tài khoản ngân hàng**, **sổ nhật ký** và **Cost Center**
(chi tiết: file quản lý hệ thống tài khoản).

1. Tài khoản
2. Cost Center

![Hệ thống tài khoản](images/quy-trinh/slide-02-03.jpg){ .doc-screenshot-sm }

![Hệ thống tài khoản](images/quy-trinh/slide-02-04.jpg){ .doc-screenshot-sm }

---

## II. Ghi nhận doanh thu — Thu tiền khách hàng {#ii-doanh-thu}

### 1. Quy trình

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | TVV | Lên đơn hàng, **Confirm** khi đã thống nhất dịch vụ, sản phẩm, giá |
| **1** | Kế toán | Kiểm tra SO đủ thông tin |
| **2** | Kế toán | Tạo **Invoice** (doanh thu, phí thu hộ). Sai TK khi đã Payment → hủy Payment, sửa Invoice |
| **3** | Kế toán | **Thu tiền** khách theo điều khoản hợp đồng |

Luồng: **SO → Kiểm tra SO → Invoice → Payment**.

### 2. Quy trình 

Sơ đồ chi tiết: kiểm tra SO → Invoice → Payment (nhánh hủy/điều chỉnh nếu cần).

![Quy trình chi tiết](images/quy-trinh/slide-04-03.jpg){ .doc-screenshot }

### 3. Tạo Invoice 

Tạo **Invoice** ghi nhận doanh thu từ đơn bán.

![Tạo Invoice](images/quy-trinh/slide-04-03.jpg){ .doc-screenshot }

### 4. Tạo Invoice, hợp đồng 

**Kiểm tra thông tin đơn hàng:**

- Đơn **có hợp đồng**: thực hiện **(2) → (3) → (1) → (4)**
- Đơn **không cần hợp đồng**: **(2) → (3)**, xong thực hiện **(1) → (4)**

!!! note "Ghi chú hợp đồng"
    - Đơn **có** hợp đồng: **bật màu xanh** ở bước (2)
    - Đơn **không** hợp đồng: **tắt** bước (2), **tạo hợp đồng** ở bước (3)

![Invoice và hợp đồng](images/quy-trinh/slide-06-03.jpg){ .doc-screenshot }

![Invoice và hợp đồng](images/quy-trinh/slide-06-04.jpg){ .doc-screenshot }

### 5. Chi tiết tạo Invoice 

Hóa đơn đã tạo — kiểm tra đã ghi nhận đúng:

- **Sổ nhật ký**, **tài khoản** doanh thu / thu hộ, **giá tiền**
- Đúng → chọn **Xác nhận**

!!! note "Tỷ giá manual"
    Chọn **Use manual Exchange Rate** để nhập tỷ giá; không chọn → hệ thống lấy tỷ giá mặc định.

![Chi tiết Invoice](images/quy-trinh/slide-07-03.jpg){ .doc-screenshot }

### 6. Tạo Payment 

- Tạo **Payment** thu tiền khách theo hợp đồng/đơn (đủ một lần hoặc nhiều đợt)
- Xem và **in phiếu thu** cho khách ký
    - CN Việt Nam: **01-TT / 02-TT**
    - CN Mỹ: phiếu thu/chi theo mẫu chi nhánh

![Tạo Payment](images/quy-trinh/slide-08-03.jpg){ .doc-screenshot }

![Tạo Payment](images/quy-trinh/slide-08-04.jpg){ .doc-screenshot }

![Phiếu thu](images/quy-trinh/slide-09-03.jpg){ .doc-screenshot }

![Phiếu thu](images/quy-trinh/slide-09-04.jpg){ .doc-screenshot }

![In phiếu thu](images/quy-trinh/slide-10-03.jpg){ .doc-screenshot }

---

## III. Các bút toán chi tiền {#iii-but-toan-chi}

| Nghiệp vụ | Bút toán (tóm tắt) |
|-----------|-------------------|
| Hoàn phí chương trình | Nợ 3388 (chi tiết ĐT) / Có 112, 111 |
| Hoàn phí ký quỹ | Nợ 344 (chi tiết ĐT) / Có 112, 111 |
| TT đối tác nước ngoài | TT: Nợ 331 / Có 112,111 — Kết chuyển: Nợ 3388 / Có 331 |
| TT NCC trong nước | Nợ CP 641,642 (Cost Center) / Có 331 → TT: Nợ 331 / Có 112,111 |
| Lương, BHXH, thuế… | TT: Nợ 3341, 3335… / Có 112,111 — Kết chuyển: Nợ 6425 / Có 3341, 3335 |

!!! note "Slide 11"
    Slide gốc là **sơ đồ quy trình** trên PowerPoint (không có ảnh chụp Odoo).

---

## IV. Ghi nhận chi phí / mua hàng — Thanh toán NCC {#iv-ncc}

### Quy trình

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | User | Đề xuất mua hàng **đã duyệt**, đủ chứng từ |
| **1** | User / KT | Tạo **Bill** → sau duyệt KT **Xác nhận** |
| **2** | User | Tạo **đề nghị thanh toán** — loại TT đúng → Mục V |
| **3** | Kế toán | **Chi tiền** theo Bill + đề nghị đã duyệt |

**PO → Bill → Đề nghị thanh toán → Payment**

### Tạo Bill — hình slide 13; nội dung & hình
- Chọn **nhà cung cấp** (chưa có → tạo mới)
- **Loại thanh toán**, **sổ nhật ký**, **tiền tệ** (VND/USD)
- Sản phẩm/dịch vụ, **TK chi phí**, số lượng, số tiền

![Tạo Bill](images/quy-trinh/slide-13-03.jpg){ .doc-screenshot }
![Tạo Bill](images/quy-trinh/slide-14-03.jpg){ .doc-screenshot }

![Tạo Bill](images/quy-trinh/slide-14-04.jpg){ .doc-screenshot }

### Tạo Payment thanh toán

1. **Xác nhận** Bill (sau khi đề nghị được duyệt)
2. **Register Payment** — ngân hàng/tiền mặt, số tiền, nội dung

![Payment NCC](images/quy-trinh/slide-15-03.jpg){ .doc-screenshot }

![Payment NCC](images/quy-trinh/slide-15-04.jpg){ .doc-screenshot }

![Payment NCC](images/quy-trinh/slide-16-03.jpg){ .doc-screenshot }

![Payment NCC](images/quy-trinh/slide-16-04.jpg){ .doc-screenshot }

### In phiếu 
In **phiếu chi** sau khi thanh toán.

![In phiếu chi](images/quy-trinh/slide-17-03.jpg){ .doc-screenshot }

![In phiếu chi](images/quy-trinh/slide-17-04.jpg){ .doc-screenshot }

---

## V. Đề xuất thanh toán {#v-dntt}

### Quy trình

| Level | Vai trò | Mô tả |
|-------|---------|--------|
| **0** | Người lập ĐNTT | Lập yêu cầu; thu thập chứng từ theo danh mục KT |
| **1** | QLBP / TCN | Duyệt / Từ chối (ghi lý do) |
| **2** | Kế toán / HR | Checklist chứng từ → Duyệt; sau BOD → thanh toán |
| **3** | BOD | Duyệt / Từ chối |

### Tạo đề xuất thanh toán
**Thông tin chung:** Chi nhánh, phòng ban, phê duyệt cuối, loại yêu cầu, danh mục thanh toán.

**Thông tin chi tiết:** Loại tiền, hình thức TT, số tiền, nội dung ĐNTT, STK (CK/Sec), thông tin HĐ.

**QLBP/TCN** và **Checklist** chứng từ theo loại thanh toán.
![Tạo đề xuất TT](images/quy-trinh/slide-19-03.jpg){ .doc-screenshot }

![Tạo đề xuất TT](images/quy-trinh/slide-19-04.jpg){ .doc-screenshot }
![Tạo đề xuất TT](images/quy-trinh/slide-20-03.jpg){ .doc-screenshot }
![Tạo đề xuất TT](images/quy-trinh/slide-20-04.jpg){ .doc-screenshot }
![Tạo đề xuất TT](images/quy-trinh/slide-21-03.jpg){ .doc-screenshot }

![Tạo đề xuất TT](images/quy-trinh/slide-21-04.jpg){ .doc-screenshot }

### View đề nghị thanh toán — hình & nội dung 
Sau khi lưu ĐNTT → trên **Bill** hiển thị **View DNTT** → đính kèm hồ sơ → **Xác nhận** yêu cầu.

![View DNTT](images/quy-trinh/slide-22-03.jpg){ .doc-screenshot }

![View DNTT](images/quy-trinh/slide-22-04.jpg){ .doc-screenshot }

### Xem trạng thái thanh toán
Sau **phê duyệt** → quay lại Bill → **Xác nhận** → tạo **Payment** NCC.

![Trạng thái thanh toán](images/quy-trinh/slide-23-03.jpg){ .doc-screenshot }

![Trạng thái thanh toán](images/quy-trinh/slide-23-04.jpg){ .doc-screenshot }

---

## VI. Bút toán tổng hợp {#vi-but-toan-th}

### Tạo bút toán (thu hộ / chi hộ theo đối tượng)

- Loại thanh toán, **sổ nhật ký**, loại tiền, Account, hạng mục, số tiền
- Chọn **SO** (đối tượng chi hộ); nhiều đối tượng → thêm nhiều dòng SO
- **Nợ:** chi hộ | **Có:** thu hộ — nhập số tiền, TK ngân hàng/tiền mặt
- Sau tạo bút toán → **Tạo đề nghị thanh toán** (giống Mục V)
![Bút toán thu chi hộ](images/quy-trinh/slide-24-03.jpg){ .doc-screenshot }

![Bút toán thu chi hộ](images/quy-trinh/slide-24-04.jpg){ .doc-screenshot }

![Bút toán thu chi hộ](images/quy-trinh/slide-25-03.jpg){ .doc-screenshot }

![Bút toán thu chi hộ](images/quy-trinh/slide-25-04.jpg){ .doc-screenshot }
![Bút toán thu chi hộ](images/quy-trinh/slide-26-03.jpg){ .doc-screenshot }
![Bút toán thu chi hộ](images/quy-trinh/slide-26-04.jpg){ .doc-screenshot }
### Bút toán tổng hợp

Tạo đề nghị thanh toán giống **Mục V** → sau khi duyệt → quay lại bút toán → **Post (Vào sổ)**.

!!! note
    Đề nghị thanh toán tạo **giống** đề nghị thanh toán NCC.
