# KIỂM TRA TRÙNG KHI TẠO LEAD MỚI

## GIỚI THIỆU

### Mục tiêu

Tài liệu này hướng dẫn người dùng hiểu quy trình tiếp nhận Lead mới từ nhiều nguồn đầu vào và cách hệ thống kiểm tra trùng dữ liệu trước khi Lead được xử lý tiếp.

Mục tiêu chính là đảm bảo mỗi khách hàng chỉ có một dữ liệu chính xác trên CRM, tránh việc nhiều nhân sự cùng xử lý một khách hàng hoặc tạo nhiều hồ sơ trùng số điện thoại.

### Phạm vi áp dụng

Quy trình này áp dụng cho tất cả Lead mới được đưa vào hệ thống CRM Odoo từ các nguồn:

- Lead từ hệ thống Marketing.
- Lead do Tư vấn viên nhập tay.
- Lead data từ sự kiện.
- Lead data từ đối tác.
- Lead import từ file Excel.
- Lead từ hotline, form đăng ký, Zalo, website, landing page, email.

### Đối tượng sử dụng

| Nhóm người dùng | Vai trò trong quy trình |
|---|---|
| Marketing | Tạo hoặc import Lead từ các kênh Marketing |
| Tư vấn viên | Nhập tay Lead hoặc tiếp nhận khách hàng mới |
| Telesale | Nhập hoặc xử lý data từ sự kiện, đối tác |
| CRM Admin | Kiểm tra và xử lý Lead bị báo trùng |
| Quản lý | Theo dõi chất lượng dữ liệu Lead |

## TỔNG QUAN QUY TRÌNH

### Ý nghĩa của kiểm tra trùng

Kiểm tra trùng là bước hệ thống kiểm tra số điện thoại của khách hàng trước khi cho phép Lead tiếp tục được xử lý.

Nếu số điện thoại đã tồn tại trong module `Lead` hoặc `Contact`, hệ thống sẽ đánh dấu Lead là trùng và khóa Lead lại để CRM Admin kiểm tra.

### Quy trình tổng quan

```text
Nguồn đầu vào
↓
Tạo Lead mới
↓
Tình trạng mặc định: Mới
↓
Hệ thống kiểm tra số điện thoại
↓
Kiểm tra trong module Lead
↓
Kiểm tra trong module Contact
↓
Nếu không trùng: Lead tiếp tục được xử lý
↓
Nếu trùng: Lead bị báo trùng và khóa lại
↓
CRM Admin kiểm tra và xử lý
```

## DỮ LIỆU ĐẦU VÀO

### Các nguồn tạo Lead

| Nguồn Lead | Cách đưa vào hệ thống | Người phụ trách |
|---|---|---|
| Hệ thống Marketing | Tự động import | Marketing / CRM Admin |
| Tư vấn viên | Nhập tay | Tư vấn viên |
| Sự kiện | Import theo file Excel | Marketing / Telesale / CRM Admin |
| Đối tác | Import theo file Excel | Marketing / Telesale / CRM Admin |
| Hotline | Nhập tay hoặc tích hợp hệ thống | Tư vấn viên / Telesale |
| Website / Landing Page/ Fanpage | Tự động import | Marketing |
| Zalo / Email | Tự động hoặc nhập tay tùy cấu hình | Marketing / Tư vấn viên |

### Dữ liệu bắt buộc khi tạo Lead

| Trường dữ liệu | Bắt buộc | Ghi chú |
|---|---|---|
| Tên khách hàng | Có | Nếu chưa biết tên thật, ghi theo thông tin khách cung cấp |
| Số điện thoại | Có | Đây là dữ liệu chính để kiểm tra trùng |
| Nguồn Lead | Có | Ví dụ: Website, Zalo, Hotline, Event, Partner |
| Nhu cầu | Có | Giúp người xử lý hiểu khách quan tâm gì |
| Thị trường | Có | Ví dụ: USA, CAD, AUS |
| Chi nhánh / VP tư vấn | Có | Giúp phân tuyến xử lý |
| Người phụ trách | Tùy quy trình | Có thể gán tự động hoặc gán sau |

### Trạng thái mặc định

Khi Lead mới được tạo vào CRM, tình trạng mặc định là:

```text
Mới
```

Trạng thái này cho biết Lead vừa được đưa vào hệ thống và chưa hoàn tất quá trình xử lý ban đầu.

## NGUYÊN TẮC KIỂM TRA TRÙNG

### Dữ liệu dùng để kiểm tra

Hệ thống ưu tiên kiểm tra trùng bằng số điện thoại.

Ví dụ:

```text
0901234567
+84 901 234 567
84 901 234 567
```

Các định dạng này cần được chuẩn hóa để hệ thống nhận diện đúng là cùng một số điện thoại.

### Phạm vi kiểm tra

Khi Lead mới vào hệ thống, hệ thống cần kiểm tra số điện thoại ở hai nơi:

1. Module `Lead`.
2. Module `Contact`.

Nếu số điện thoại đã tồn tại ở một trong hai module này, Lead mới được xem là có khả năng trùng.

### Kết quả kiểm tra

| Kết quả | Hành động của hệ thống |
|---|---|
| Không trùng | Lead được giữ trạng thái Mới và tiếp tục chuyển sang bước xử lý Lead |
| Trùng trong Lead | Hệ thống đánh dấu trùng và khóa Lead để Admin kiểm tra |
| Trùng trong Contact | Hệ thống đánh dấu trùng và khóa Lead để Admin kiểm tra |

## HƯỚNG DẪN THEO TỪNG NGUỒN LEAD

### 1. Lead từ hệ thống Marketing

Lead từ hệ thống Marketing được tự động import vào CRM.

Ví dụ nguồn Marketing:

- Website.
- Landing page.
- Zalo.
- Email.
- Campaign.
- Form đăng ký.

Quy trình:

```text
Khách để lại thông tin
↓
Hệ thống Marketing ghi nhận Lead
↓
Lead được tự động import vào CRM
↓
CRM tạo Lead mới với tình trạng Mới
↓
Hệ thống kiểm tra trùng số điện thoại
```

Người dùng không cần tạo tay Lead trong trường hợp này, nhưng cần kiểm tra danh sách Lead để xử lý các Lead được phân công.

### 2. Lead từ Tư vấn viên

Lead từ Tư vấn viên là Lead được nhập tay khi Tư vấn viên tiếp nhận thông tin khách hàng trực tiếp.

Ví dụ:

- Khách gọi trực tiếp cho Tư vấn viên.
- Khách nhắn tin riêng.
- Khách được giới thiệu từ người quen.

Các bước thực hiện:

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Chọn `Mới`.
4. Nhập thông tin khách hàng.
5. Nhập số điện thoại.
6. Chọn nguồn Lead phù hợp.
7. Chọn `Lưu`.
8. Hệ thống tự động kiểm tra trùng.

Kết quả mong đợi:

- Nếu không trùng, Lead được tạo thành công với tình trạng `Mới`.
- Nếu trùng, hệ thống báo trùng và khóa Lead lại.

### 3. Lead data từ sự kiện hoặc đối tác

Lead từ sự kiện hoặc đối tác thường được import theo file Excel.

Ví dụ:

- Danh sách khách đăng ký tại hội thảo.
- Danh sách khách từ đối tác.
- Data từ chương trình branding.

Quy trình:

```text
Nhận file data
↓
Kiểm tra format file
↓
Import file vào CRM
↓
CRM tạo Lead mới
↓
Tình trạng mặc định: Mới
↓
Hệ thống kiểm tra trùng số điện thoại
```

Lưu ý khi chuẩn bị file:

- Mỗi dòng là một khách hàng.
- Số điện thoại không được để trống.
- Không nhập nhiều số điện thoại vào cùng một ô nếu hệ thống chưa hỗ trợ.
- Cần có cột nguồn Lead để biết data đến từ đâu.
- Cần kiểm tra lỗi chính tả hoặc sai định dạng trước khi import.

## HƯỚNG DẪN KIỂM TRA TRÊN MÀN HÌNH LEAD

### Mục tiêu

Người dùng biết cách nhận biết Lead mới, Lead không trùng và Lead bị trùng trên màn hình danh sách Lead.

### Các cột cần chú ý

Trên màn hình danh sách Lead, cần chú ý các cột:

| Cột | Ý nghĩa |
|---|---|
| Lead | Tên Lead |
| Tên liên hệ | Tên khách hàng nhập vào |
| SĐT khách hàng | Số điện thoại dùng để kiểm tra trùng |
| Nhu cầu | Nhu cầu ban đầu của khách |
| Thị trường | Thị trường khách quan tâm |
| VP tư vấn | Văn phòng hoặc chi nhánh xử lý |
| Nhân viên | Người phụ trách |
| Đội ngũ | Team xử lý |
| Duplicate | Kết quả kiểm tra trùng |
| Created on | Ngày tạo Lead |
| Tình trạng | Trạng thái xử lý Lead |
| Qualify Lead | Trạng thái qualify |

### Cách đọc cột Duplicate

| Giá trị hiển thị | Ý nghĩa |
|---|---|
| Không trùng | Số điện thoại chưa tồn tại trong Lead hoặc Contact |
| Trùng | Số điện thoại đã tồn tại trong Lead hoặc Contact |

Khi cột `Duplicate` hiển thị `trùng`, người dùng không nên tiếp tục xử lý Lead đó cho đến khi CRM Admin kiểm tra.

## XỬ LÝ KHI LEAD BỊ TRÙNG

### Mục tiêu

Đảm bảo Lead trùng không bị xử lý sai hoặc xử lý song song bởi nhiều người.

### Hành động của hệ thống

Khi phát hiện trùng, hệ thống cần:

- Đánh dấu Lead là `trùng`.
- Khóa Lead lại.
- Không cho người dùng tiếp tục qualify hoặc xử lý nếu chưa được Admin kiểm tra.
- Giữ lại thông tin nguồn Lead để Admin đối chiếu.

### Người dùng cần làm gì?

Nếu thấy Lead bị báo trùng:

1. Báo CRM Admin hoặc người phụ trách dữ liệu kiểm tra.
2. Chờ kết quả xử lý từ Admin.

### CRM Admin cần kiểm tra gì?

CRM Admin cần kiểm tra:

- Số điện thoại trùng với Lead nào.
- Số điện thoại trùng với Contact nào.
- Lead cũ đang do ai phụ trách.
- Lead cũ đang ở trạng thái nào.
- Lead mới có nguồn nào.
- Lead mới có thông tin nào bổ sung hữu ích không.

### Các hướng xử lý của Admin

| Trường hợp | Hướng xử lý |
|---|---|
| Lead mới trùng hoàn toàn với Lead cũ | Không tạo hồ sơ mới, cập nhật ghi chú nếu cần |
| Lead mới có thông tin bổ sung | Gộp hoặc cập nhật thêm vào hồ sơ hiện có |
| Lead cũ đã lâu không xử lý | Kiểm tra lại quyền xử lý và phân công theo quy định |
| Trùng với Contact đã là khách hàng | Cập nhật lịch sử tương tác vào Contact/Opportunity phù hợp |
| Số điện thoại nhập sai | Sửa lại số điện thoại nếu có bằng chứng rõ ràng |

## KẾT QUẢ MONG ĐỢI

Sau khi quy trình hoạt động đúng:

- Lead mới được tạo với tình trạng mặc định là `Mới`.
- Tất cả nguồn đầu vào đều được kiểm tra trùng.
- Hệ thống kiểm tra số điện thoại trong cả `Lead` và `Contact`.
- Lead trùng được đánh dấu rõ ràng.
- Lead trùng bị khóa để tránh xử lý sai.
- CRM Admin có cơ sở để kiểm tra và xử lý dữ liệu.
- Người dùng không tạo nhiều hồ sơ cho cùng một khách hàng.

## LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Lead bị trùng nhưng vẫn tiếp tục xử lý | Người dùng chưa hiểu ý nghĩa cột Duplicate | Dừng xử lý và báo Admin |
| Không phát hiện trùng | Số điện thoại nhập sai định dạng | Kiểm tra lại format số điện thoại |
| Một khách có nhiều Lead | Import nhiều nguồn chưa được kiểm tra tốt | Admin rà soát và gộp dữ liệu |
| Lead từ file import bị thiếu số điện thoại | File data thiếu thông tin bắt buộc | Bổ sung số điện thoại trước khi import |
| Không biết Lead trùng với hồ sơ nào | Người dùng không có quyền xem dữ liệu liên quan | Báo CRM Admin kiểm tra |

## CHECKLIST CHO NGƯỜI DÙNG

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Lead có số điện thoại |  |  |
| Lead có nguồn rõ ràng |  |  |
| Tình trạng Lead là Mới |  |  |
| Cột Duplicate là Không trùng hoặc Trùng |  |  |
| Nếu Trùng, đã dừng xử lý |  |  |
| Nếu Trùng, đã báo CRM Admin |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Tạo Lead nhập tay

Yêu cầu:

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Tạo một Lead mới.
4. Nhập tên khách hàng, số điện thoại, nguồn Lead và nhu cầu.
5. Lưu Lead.
6. Kiểm tra cột `Tình trạng`.
7. Kiểm tra cột `Duplicate`.

Kết quả cần đạt:

- Lead được tạo với tình trạng `Mới`.
- Người dùng biết Lead có bị trùng hay không.

### Bài 2: Nhận biết Lead trùng

Yêu cầu:

1. Mở danh sách Lead.
2. Tìm các Lead có cột `Duplicate` hiển thị `trùng`.
3. Ghi nhận Lead nào đang bị khóa.
4. Không xử lý tiếp Lead đó.
5. Báo CRM Admin kiểm tra.

Kết quả cần đạt:

- Người dùng nhận biết đúng Lead trùng.
- Người dùng không tự ý xử lý Lead trùng.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Lead Duplicate Check Process |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / CRM / Lead Management |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
| Ngày phát hành |  |

