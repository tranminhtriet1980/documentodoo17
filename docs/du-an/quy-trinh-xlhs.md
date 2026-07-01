# Quy trình xử lý hồ sơ (XLHS) trên Odoo

!!! info "Nguồn tài liệu"
    Mr Khanh — *TÀI LIỆU XLHS _ODDO.pptx*. Áp dụng module **Project (QLHS)** trên **Odoo 17**.

!!! tip "Hình ảnh"
    - Trang này: quy trình + hình theo **thứ tự slide** PowerPoint
    - [Phụ lục hình ảnh](phu-luc-hinh-anh.md) — xem riêng từng mục
    - Sửa tay: `BuildTaiLieu.bat` — tạo lại từ PPTX (ghi đè): `TrichAnhTuPptxDuAn.bat`

---

## Chương I — Giới thiệu tổng quan

### 1. Tổng quan Project (QLHS)

Phần mềm quản lý **hồ sơ du học – du lịch – định cư** trên Odoo; liên kết **CRM** và **Kế toán**.


### 2. Đăng nhập hệ thống

- URL: `https://internal.edupath.org.vn`
- **Login with Email — Microsoft 365**

![Đăng nhập](images/xlhs/slide-04-02.jpg){ .doc-screenshot-sm }

![Đăng nhập](images/xlhs/slide-05-02.jpg){ .doc-screenshot-sm }

### 3. Màn hình chính

- **Trang chủ Project (QLHS):** danh mục hồ sơ theo nhóm (Định cư, Du học, Du lịch, Bảo lãnh…)
- **My Task:** module To-do → My Task — theo hạn (Today, This Week, This Month…)

![Màn hình slide 6](images/xlhs/slide-06-02.jpg){ .doc-screenshot }

![Màn hình slide 7](images/xlhs/slide-07-02.jpg){ .doc-screenshot }

![Màn hình slide 8](images/xlhs/slide-08-02.jpg){ .doc-screenshot }

### 4. Thanh công cụ

- **Search** — tìm hồ sơ, task
- **Thông báo** — tin nhắn, task tới due date

![Thanh công cụ](images/xlhs/slide-09-02.jpg){ .doc-screenshot }

![Thanh công cụ](images/xlhs/slide-10-02.jpg){ .doc-screenshot }

---

## Chương II — Quy trình xử lý hồ sơ

### 1. Quy trình tiếp nhận

Luồng từ **Sales Order**: tiếp nhận → phê duyệt → khởi tạo dự án/hồ sơ.

| Bước | Mô tả |
|------|--------|
| Tiếp nhận | Đủ thông tin: chi phí, nhu cầu, chương trình |
| Kế toán | Kiểm tra thông tin khách tham gia chương trình |
| Khởi tạo | Theo **SO** sau duyệt — mẫu dự án theo chương trình (EB3, Du học Mỹ, Canada/Úc, Du lịch…) |

!!! note "Slide 12"
    Sơ đồ quy trình tiếp nhận trên slide 12 (flowchart PowerPoint).


### 2. Vai trò

| Vai trò | Trách nhiệm |
|---------|-------------|
| **Project Manager** | Chịu trách nhiệm chính; kiểm tra thông tin; khởi tạo; phân công task |
| **Admission, Immigration, Visa, Translate** | Các stage lớn; hoàn thành task; liên hệ bộ phận khác |



### 2.1. Quy trình XLHS EB3

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS EB3](images/xlhs/slide-16-02.jpg){ .doc-screenshot }

### 2.2. Quy trình XLHS EB3-TT

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS EB3-TT](images/xlhs/slide-17-02.jpg){ .doc-screenshot }

### 2.3. Quy trình XLHS Du học Mỹ

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Du học Mỹ](images/xlhs/slide-18-02.jpg){ .doc-screenshot }

### 2.4. Quy trình XLHS Du học Canada/Úc

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Du học Canada/Úc](images/xlhs/slide-19-02.jpg){ .doc-screenshot }

### 2.5. Quy trình XLHS Du lịch Mỹ

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Du lịch Mỹ](images/xlhs/slide-20-02.jpg){ .doc-screenshot }

### 2.6. Quy trình XLHS Du lịch Canada/Úc

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Du lịch Canada/Úc](images/xlhs/slide-21-02.jpg){ .doc-screenshot }

### 2.7. Quy trình XLHS GHLT - CD F1 

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS GHLT - CD F1](images/xlhs/slide-22-02.jpg){ .doc-screenshot }

### 2.8. Quy trình XLHS Bảo lãnh (IN USA) 

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Bảo lãnh (IN USA)](images/xlhs/slide-23-02.jpg){ .doc-screenshot }

### 2.9. Quy trình XLHS Bảo lãnh (OUT USA) 

- **Stage** lớn: từ trái sang phải (Sale Admin tiếp nhận HS, các giai đoạn hồ sơ…)
- **Task:** từ trên xuống — hồ sơ không cần task thì **Done** task đó

![Quy trình XLHS Bảo lãnh (OUT USA)](images/xlhs/slide-24-02.jpg){ .doc-screenshot }

---

## Chương III — Thao tác nghiệp vụ xử lý hồ sơ

### 1. Giới thiệu tính năng 

Module **Project** quản lý danh sách hồ sơ: tình trạng, ngày bắt đầu/kết thúc, tiến độ, công việc…


### 2. Tạo mới hồ sơ

**A. Tạo thủ công:** Module Project → **New** (Sales Admin).

**B. Tự động từ SO:** Tên hồ sơ theo **Tên KH + Chương trình tư vấn – SO**
(vd: *ĐOÀN VĂN ÚT – EB3 – SO00081*).

![Tạo hồ sơ](images/xlhs/slide-27-02.jpg){ .doc-screenshot }

![Tạo hồ sơ](images/xlhs/slide-28-02.jpg){ .doc-screenshot }

### 3. Tiếp nhận hồ sơ

1. Nhận thông báo → menu **⋮** → **Settings**
2. Bổ sung nhân sự (Admission, Leader…)
3. Chuyển trạng thái tiếp nhận → khởi tạo **Task**

![Tiếp nhận hồ sơ](images/xlhs/slide-29-02.jpg){ .doc-screenshot }

![Tiếp nhận hồ sơ](images/xlhs/slide-30-02.jpg){ .doc-screenshot }

### 4. Xử lý Task

- Chọn task từ danh mục hồ sơ
- Chuyển tình trạng: Request, Approved, Done…
- Cập nhật thông tin hồ sơ; **SharePoint** (Create / Open Folder)
- Task phụ — tick hoàn thành
- **Ghi chú**, **Activities** (loại hành động, Due date)
- **Giao** người thực hiện (@ tên)
- Theo dõi trên **My Task**


![Task slide 31](images/xlhs/slide-31-02.jpg){ .doc-screenshot }

![Task slide 32](images/xlhs/slide-32-02.jpg){ .doc-screenshot }


![Task slide 33](images/xlhs/slide-33-02.jpg){ .doc-screenshot }


![Task slide 34](images/xlhs/slide-34-02.jpg){ .doc-screenshot }


![Task slide 35](images/xlhs/slide-35-02.jpg){ .doc-screenshot }


![Task slide 36](images/xlhs/slide-36-02.jpg){ .doc-screenshot }

![Task slide 37](images/xlhs/slide-37-02.jpg){ .doc-screenshot }


![Task slide 38](images/xlhs/slide-38-02.jpg){ .doc-screenshot }


![Task slide 39](images/xlhs/slide-39-02.jpg){ .doc-screenshot }

### 5. Ràng buộc chuyển trạng thái 

Chỉ chuyển trạng thái khi đủ điều kiện; thiếu thông tin → thông báo lỗi (vd. thiếu *Ngày nhận hồ sơ Admission*).

!!! note "File điều kiện"
    Chi tiết: *Điều kiện chuyển Status.xlsx* (trên slide 43).

![Ràng buộc status](images/xlhs/slide-41-02.jpg){ .doc-screenshot }

![Ràng buộc status](images/xlhs/slide-42-02.jpg){ .doc-screenshot }

### 6. Thông báo tự động

Khi đủ điều kiện tiến trình → email/thông báo tự động cho bộ phận liên quan (Internal).

!!! note "Automation"
    Danh sách mẫu: *Automation.xlsx* (slide 46).

![Thông báo tự động](images/xlhs/slide-44-02.jpg){ .doc-screenshot }

![Thông báo tự động](images/xlhs/slide-45-02.jpg){ .doc-screenshot }

---

## Chương IV — Điều kiện phễu lọc

| Điều kiện | Ý nghĩa |
|-----------|---------|
| **All** | Thoả tất cả điều kiện |
| **Or** | Thoả một trong các điều kiện |
| **=** / **!=** | Bằng / khác |
| **is in** / **is not in** | Thuộc / không thuộc nhóm |
| **is set** / **is not set** | Có giá trị / trống |

Ví dụ: hồ sơ *Dung Ly*, stage *In Progress*, phụ trách *Thuý Hiên* và *Nguyệt*.

![Phễu lọc](images/xlhs/slide-49-02.jpg){ .doc-screenshot }

---

Xem thêm: [Phụ lục hình ảnh](phu-luc-hinh-anh.md) | [Nhiệm vụ](nhiem-vu.md) | [Timesheet](timesheet.md)
