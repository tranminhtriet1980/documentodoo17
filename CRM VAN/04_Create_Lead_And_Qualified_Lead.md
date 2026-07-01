# TẠO LEAD MỚI VÀ ĐÁNH GIÁ QUALIFIED LEAD

## GIỚI THIỆU

### Mục tiêu

Tài liệu này hướng dẫn người dùng cách tạo Lead mới, cập nhật đúng loại khách hàng sau khi liên hệ, nhập đầy đủ các trường bắt buộc và đánh giá chất lượng Lead trước khi chuyển thành cơ hội.

Mục tiêu chính là giúp Tư vấn viên ghi nhận đúng thông tin khách hàng, xác định đúng khả năng tư vấn và chỉ chuyển cơ hội đối với Lead đạt tiêu chí.

### Vị trí trong quy trình CRM

Quy trình này được thực hiện sau bước Lead mới đi vào hệ thống và đã qua kiểm tra trùng.

```text
Lead đi vào CRM
↓
Kiểm tra trùng
↓
Tạo Lead mới với tình trạng Mới
↓
TVV liên hệ khách hàng
↓
Cập nhật loại khách hàng và thông tin bắt buộc
↓
Đánh giá Qualified Lead
↓
Đánh giá điểm sao
↓
Chuyển cơ hội nếu đạt điều kiện
```

### Đối tượng sử dụng

| Nhóm người dùng | Vai trò |
|---|---|
| Tư vấn viên | Liên hệ khách, cập nhật thông tin, đánh giá Lead |
| Marketing | Theo dõi chất lượng Lead từ nguồn Marketing |
| Telesale | Xác minh thông tin ban đầu nếu có |
| CRM Admin | Hỗ trợ kiểm tra dữ liệu và cấu hình quy tắc |
| Quản lý | Theo dõi Lead qualified và hiệu quả chuyển đổi |

## NGUYÊN TẮC TẠO LEAD MỚI

### Loại khách hàng mặc định

Khi Lead mới đi vào hệ thống, `Loại khách hàng` mặc định là:

```text
Khách hàng
```

Đây chỉ là giá trị mặc định ban đầu. Sau khi Tư vấn viên liên hệ khách và xác minh thông tin, Tư vấn viên cần điều chỉnh lại loại khách hàng cho chính xác.

### Vì sao cần cập nhật loại khách hàng?

Mỗi loại khách hàng có cách nhập liệu khác nhau. Nếu chọn sai loại khách hàng, thông tin lưu trên CRM sẽ không đúng với thực tế và có thể ảnh hưởng đến quá trình tư vấn, chăm sóc và báo cáo.

Ví dụ:

- Người trực tiếp có nhu cầu du học là `Khách hàng`.
- Phụ huynh hoặc người liên hệ thay cho học sinh là `Người đại diện`.
- Đơn vị hoặc cá nhân giới thiệu khách hàng là `Đối tác`.

## CÁC LOẠI KHÁCH HÀNG

### 1. Loại khách hàng: Khách hàng

Sử dụng khi người đang được nhập trên Lead là khách hàng chính hoặc người có nhu cầu trực tiếp.

Thông tin cần nhập:

| Trường thông tin | Ghi chú |
|---|---|
| Tên khách hàng | Họ tên khách hàng chính |
| Giới tính | Chọn đúng giới tính sau khi xác minh |
| Email khách hàng | Nhập nếu có |
| SĐT / Mã quốc gia | Nhập đúng mã quốc gia và số điện thoại |
| VP tư vấn | Văn phòng hoặc chi nhánh tư vấn |
| Nhu cầu | Nhu cầu khách quan tâm |
| Thị trường | Quốc gia hoặc thị trường khách quan tâm |
| Nhân viên kinh doanh | Người phụ trách xử lý |
| Nguồn | Nguồn phát sinh Lead |
| Tình trạng | Trạng thái xử lý Lead hiện tại |
| Edupath Tag | Các tiêu chí đánh giá chất lượng Lead |

### 2. Loại khách hàng: Người đại diện

Sử dụng khi người liên hệ không phải khách hàng chính, nhưng đại diện trao đổi thông tin với công ty.

Ví dụ:

- Bố hoặc mẹ của học sinh.
- Người thân liên hệ thay.
- Người bảo hộ.

Thông tin cần nhập:

| Trường thông tin | Ghi chú |
|---|---|
| Loại khách hàng | Chọn `Người đại diện` |
| Mối quan hệ | Ví dụ: Bố/Mẹ, Anh/Chị, Người thân |
| Họ và tên | Họ tên người đại diện |
| Giới tính | Giới tính người đại diện |
| Email | Email người đại diện nếu có |
| SĐT / Mã quốc gia | Số điện thoại người đại diện |
| Thông tin khách hàng chính | Cập nhật thêm nếu đã xác minh được |

Lưu ý:

- Không nhập người đại diện như khách hàng chính nếu thực tế họ chỉ là người liên hệ thay.
- Cần ghi rõ mối quan hệ để Tư vấn viên và CSKH hiểu vai trò của người liên hệ.

### 3. Loại khách hàng: Đối tác

Sử dụng khi Lead đến từ đối tác hoặc người/đơn vị giới thiệu khách hàng.

Thông tin cần nhập:

| Trường thông tin | Ghi chú |
|---|---|
| Loại khách hàng | Chọn `Đối tác` |
| Tên đối tác | Tên cá nhân hoặc tổ chức đối tác |
| SĐT / Mã quốc gia | Số điện thoại liên hệ |
| Email | Email đối tác nếu có |
| Nguồn | Chọn nguồn liên quan đến đối tác |
| Ghi chú | Ghi rõ khách hàng được giới thiệu hoặc bối cảnh hợp tác |

Lưu ý:

- Nếu đối tác giới thiệu một khách hàng cụ thể, cần phân biệt rõ thông tin đối tác và thông tin khách hàng được giới thiệu.
- Không dùng hồ sơ đối tác thay cho hồ sơ khách hàng chính.

## CÁC TRƯỜNG BẮT BUỘC

### Danh sách trường bắt buộc

Khi tạo hoặc cập nhật Lead, người dùng cần kiểm tra đầy đủ các trường sau:

| Trường bắt buộc | Mục đích |
|---|---|
| Giới tính | Xác định thông tin cá nhân cơ bản |
| SĐT / Mã quốc gia | Liên hệ khách hàng và kiểm tra trùng |
| VP tư vấn | Xác định đơn vị phụ trách tư vấn |
| Nhu cầu | Biết khách hàng đang quan tâm dịch vụ nào |
| Thị trường | Biết thị trường hoặc quốc gia khách quan tâm |
| Nhân viên kinh doanh | Xác định người phụ trách xử lý |
| Nguồn | Theo dõi hiệu quả từng nguồn Lead |
| Tình trạng | Theo dõi trạng thái xử lý Lead |
| Edupath Tag | Đánh giá chất lượng Lead qualified |

### Edupath Tag dùng để làm gì?

`Edupath Tag` là nhóm tiêu chí dùng để đánh giá chất lượng Lead và khả năng chuyển thành cơ hội.

Các tag chính:

| Edupath Tag | Ý nghĩa |
|---|---|
| Tài chính | Khách có khả năng hoặc điều kiện tài chính phù hợp |
| Năng lực hồ sơ | Hồ sơ hoặc năng lực của khách phù hợp |
| Thời điểm | Khách có thời điểm dự kiến phù hợp để triển khai |
| Mục tiêu | Khách có mục tiêu rõ ràng |

## ĐÁNH GIÁ QUALIFIED LEAD

### Mục tiêu

Sau khi liên hệ khách hàng, Tư vấn viên cần đánh giá Lead đang ở trạng thái nào để quyết định tiếp tục tư vấn, liên hệ sau, ngừng chăm sóc hoặc chuyển cơ hội.

### Các trạng thái đánh giá

| Trạng thái Qualified Lead | Ý nghĩa |
|---|---|
| New | Lead mới, chưa xử lý hoặc vừa được tạo |
| Not Qualified | Lead không đủ điều kiện tiếp tục tư vấn tại thời điểm hiện tại |
| Qualified | Lead đã được xác minh và có đủ thông tin để tiếp tục đánh giá |

## QUY TẮC PHÂN LOẠI LEAD

### 1. New

`New` là tình trạng mặc định khi Lead mới đi vào hệ thống.

Áp dụng khi:

- Lead vừa được tạo.
- Chưa liên hệ khách hàng.
- Chưa xác minh nhu cầu.
- Chưa đánh giá Edupath Tag.

### 2. Not Qualified

`Not Qualified` áp dụng khi Lead không đủ điều kiện tiếp tục xử lý theo quy trình tư vấn.

Các tình trạng liên quan:

- Close.
- Liên hệ sau.
- Ngừng chăm sóc.

Các lý do thường gặp:

| Lý do | Mô tả |
|---|---|
| Không nghe máy | Gọi nhiều lần nhưng khách không nghe máy |
| Không có nhu cầu ngay từ đầu | Khách xác nhận không có nhu cầu |
| Trùng | Lead bị trùng với Lead hoặc Contact đã có |
| Chọn đơn vị khác | Khách đã chọn đơn vị tư vấn khác |

Lưu ý:

- Nếu Lead là `Not Qualified`, cần ghi rõ lý do.
- Không chuyển cơ hội đối với Lead chưa đủ điều kiện.

### 3. Qualified

`Qualified` áp dụng khi Lead đã được xác minh và có thông tin đủ rõ để tiếp tục xử lý.

Các trường hợp có thể thuộc nhóm Qualified:

- Đã xác minh thông tin khách hàng.
- Đã gặp hoặc trao đổi được với khách hàng.
- Đã xác định được nhu cầu.
- Đã có đủ dữ liệu để đánh giá chất lượng Lead.
- Ngừng chăm sóc sau khi đã tư vấn nhưng không tiếp tục vì lý do cụ thể.

Các lý do ngừng chăm sóc trong nhóm Qualified có thể gồm:

- Khách hàng chọn đơn vị khác do giá.
- Tài chính không phù hợp.
- Đã tư vấn nhưng khách chưa có kế hoạch hoặc không phản hồi.
- Chương trình không phù hợp với nhu cầu hoặc điều kiện của khách hàng.

## ĐÁNH GIÁ ĐIỂM QUALIFIED VÀ CHUYỂN CƠ HỘI

### Mục tiêu

Điểm Qualified giúp xác định Lead có đủ chất lượng để chuyển thành cơ hội hay chưa.

Hệ thống dựa trên `Edupath Tag` để đánh giá số sao.

### Quy tắc chấm sao

| Mức sao | Điều kiện Edupath Tag | Ý nghĩa |
|---|---|---|
| 0 sao | Chỉ có `Mục tiêu` hoặc `Thời điểm` | Lead có thông tin ban đầu nhưng chưa đủ mạnh |
| 1 sao | Có `Tài chính` hoặc `Năng lực hồ sơ` | Lead có một tiêu chí quan trọng |
| 2 sao | Có cả `Tài chính` và `Năng lực hồ sơ` | Lead đủ điều kiện tốt để xem xét chuyển cơ hội |
| 3 sao | Có đủ 4 tiêu chí: `Tài chính`, `Năng lực hồ sơ`, `Thời điểm`, `Mục tiêu` | Lead có chất lượng cao |

### Điều kiện hiện pop-up thông tin cơ hội

Khi Lead đạt mức:

- 2 sao.
- 3 sao.

Hệ thống sẽ hiển thị pop-up thông tin cơ hội để người dùng kiểm tra và chuyển Lead sang cơ hội.

### Tiêu chí chuyển cơ hội

Lead nên được chuyển cơ hội khi có các thông tin tối thiểu sau:

- Tên khách hàng.
- Số điện thoại khách hàng.
- Đã đúng chức năng sau 2-3 cuộc gọi tư vấn.
- Khách hàng tương tác sau khi chuyển hợp đồng mẫu hoặc tư vấn chuyên sâu.
- Khách lên văn phòng.
- Test tiếng Anh.
- Khách có nhu cầu tham gia chương trình trong năm.

## CÁC BƯỚC THỰC HIỆN TRÊN ODOO

### Bước 1: Mở Lead mới

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Mở Lead cần xử lý.
4. Kiểm tra tình trạng ban đầu là `Mới`.
5. Kiểm tra Lead có bị trùng hay không.

### Bước 2: Liên hệ khách hàng

1. Gọi điện hoặc liên hệ khách qua kênh phù hợp.
2. Xác minh khách là khách hàng chính, người đại diện hay đối tác.
3. Ghi nhận kết quả trao đổi.
4. Cập nhật thông tin còn thiếu.

### Bước 3: Cập nhật loại khách hàng

1. Tại trường `Loại khách hàng`, kiểm tra giá trị hiện tại.
2. Nếu đúng là khách hàng chính, giữ `Khách hàng`.
3. Nếu là phụ huynh hoặc người liên hệ thay, đổi thành `Người đại diện`.
4. Nếu là đơn vị hoặc người giới thiệu, đổi thành `Đối tác`.
5. Nhập các trường thông tin tương ứng với từng loại khách hàng.

### Bước 4: Cập nhật trường bắt buộc

Kiểm tra và nhập đầy đủ:

1. Giới tính.
2. SĐT và mã quốc gia.
3. VP tư vấn.
4. Nhu cầu.
5. Thị trường.
6. Nhân viên kinh doanh.
7. Nguồn.
8. Tình trạng.
9. Edupath Tag.

### Bước 5: Đánh giá Qualified Lead

1. Nếu chưa liên hệ hoặc chưa xử lý, giữ trạng thái `New`.
2. Nếu Lead không đủ điều kiện, chọn `Not Qualified` và nhập lý do.
3. Nếu Lead đã xác minh và có thông tin rõ, chọn `Qualified`.
4. Cập nhật Edupath Tag theo kết quả tư vấn.
5. Kiểm tra mức sao của Lead.

### Bước 6: Chuyển cơ hội nếu đủ điều kiện

1. Kiểm tra Lead đạt 2 sao hoặc 3 sao.
2. Kiểm tra pop-up thông tin cơ hội.
3. Xác nhận lại thông tin khách hàng.
4. Cập nhật thông tin còn thiếu nếu có.
5. Thực hiện chuyển Lead sang cơ hội theo quy trình CRM.

## KẾT QUẢ MONG ĐỢI

Sau khi thực hiện đúng quy trình:

- Lead mới có loại khách hàng mặc định là `Khách hàng`.
- Tư vấn viên cập nhật đúng loại khách hàng sau khi xác minh.
- Các trường bắt buộc được nhập đầy đủ.
- Lead được đánh giá đúng `New`, `Not Qualified` hoặc `Qualified`.
- Edupath Tag phản ánh đúng chất lượng Lead.
- Lead đạt 2 sao hoặc 3 sao có thể hiển thị pop-up chuyển cơ hội.
- Chỉ Lead đủ tiêu chí mới được chuyển thành cơ hội.

## LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Không đổi loại khách hàng sau khi liên hệ | TVV giữ mặc định `Khách hàng` | Xác minh lại vai trò người liên hệ và cập nhật đúng loại |
| Thiếu mã quốc gia khi nhập số điện thoại | Nhập số điện thoại chưa đủ format | Bổ sung mã quốc gia như VN, US |
| Không chấm đúng sao | Chọn thiếu hoặc sai Edupath Tag | Kiểm tra lại 4 tag: Tài chính, Năng lực hồ sơ, Thời điểm, Mục tiêu |
| Chuyển cơ hội khi Lead chưa đủ điều kiện | Chưa xác minh hoặc chưa đủ 2 sao | Không chuyển cơ hội, tiếp tục tư vấn hoặc cập nhật thông tin |
| Not Qualified nhưng không có lý do | Người dùng quên nhập lý do | Cập nhật lý do rõ ràng trước khi đóng hoặc ngừng chăm sóc |

## CHECKLIST CHO TVV

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Lead không bị trùng |  |  |
| Tình trạng ban đầu là Mới |  |  |
| Đã liên hệ khách hàng |  |  |
| Đã xác định đúng loại khách hàng |  |  |
| Đã nhập giới tính |  |  |
| Đã nhập SĐT và mã quốc gia |  |  |
| Đã chọn VP tư vấn |  |  |
| Đã chọn nhu cầu |  |  |
| Đã chọn thị trường |  |  |
| Đã chọn nhân viên kinh doanh |  |  |
| Đã chọn nguồn |  |  |
| Đã cập nhật tình trạng |  |  |
| Đã chọn Edupath Tag |  |  |
| Đã kiểm tra số sao |  |  |
| Đã chuyển cơ hội nếu đủ điều kiện |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Tạo Lead mới

Yêu cầu:

1. Tạo một Lead mới.
2. Kiểm tra `Loại khách hàng` mặc định là `Khách hàng`.
3. Nhập các trường bắt buộc.
4. Lưu Lead.
5. Kiểm tra tình trạng Lead là `Mới`.

Kết quả cần đạt:

- Lead được tạo thành công.
- Loại khách hàng mặc định là `Khách hàng`.
- Các trường bắt buộc được nhập đầy đủ.

### Bài 2: Cập nhật loại khách hàng thành Người đại diện

Yêu cầu:

1. Mở Lead đã tạo.
2. Giả định người liên hệ là phụ huynh.
3. Đổi `Loại khách hàng` thành `Người đại diện`.
4. Nhập `Mối quan hệ`.
5. Nhập họ tên và số điện thoại người đại diện.

Kết quả cần đạt:

- CRM ghi nhận đúng người liên hệ là `Người đại diện`.
- Thông tin không bị nhầm với khách hàng chính.

### Bài 3: Đánh giá Edupath Tag và điểm sao

Yêu cầu:

1. Mở Lead đã xác minh.
2. Chọn Edupath Tag theo tình huống giảng viên đưa ra.
3. Kiểm tra mức sao.
4. Xác định Lead có đủ điều kiện chuyển cơ hội hay chưa.

Kết quả cần đạt:

- Người dùng hiểu cách chọn tag.
- Người dùng xác định đúng mức 0 sao, 1 sao, 2 sao hoặc 3 sao.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Create Lead and Qualified Lead |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / CRM / Lead Management |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
| Ngày phát hành |  |

