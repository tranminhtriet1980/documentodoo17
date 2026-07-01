# QUẢN LÝ PIPELINE CƠ HỘI

## GIỚI THIỆU

### Mục tiêu

Tài liệu này hướng dẫn người dùng xử lý cơ hội sau khi Lead đã được chuyển sang Opportunity.

Mục tiêu chính là giúp Tư vấn viên theo dõi đúng giai đoạn tư vấn, cập nhật pipeline kịp thời, ghi nhận kết quả xử lý và xác định cơ hội đang tiếp tục, thành công hay thất bại.


### Vị trí trong quy trình CRM

```text
Lead đủ điều kiện
↓
Chuyển cơ hội
↓
Pipeline cơ hội
↓
Tư vấn chuyên sâu
↓
Test tiếng Anh
↓
Đề xuất giải pháp
↓
Cân nhắc đăng ký
↓
Chuyển hợp đồng
↓
Thành công / Thất bại
```

`New Quotation` và `View Quotation` không phải là stage bắt buộc trong pipeline. `New Quotation` dùng để tạo báo giá mới; `View Quotation` dùng để mở lại báo giá đã có, thường tại stage `Cân nhắc đăng ký` hoặc `Chuyển hợp đồng`.

### Đối tượng sử dụng

| Nhóm người dùng | Vai trò |
|---|---|
| Tư vấn viên | Xử lý cơ hội và cập nhật pipeline |
| Quản lý kinh doanh | Theo dõi pipeline, tiến độ và kết quả |
| CSKH | Tiếp nhận các trường hợp thất bại hoặc cần chăm sóc lại |

## TỔNG QUAN PIPELINE CƠ HỘI

### Pipeline là gì?

Pipeline là luồng theo dõi cơ hội từ lúc khách hàng được chuyển từ xác minh sang Tư vấn chuyên sâu và đến khi có kết quả cuối cùng.

Mỗi cột trên màn hình Kanban thể hiện một giai đoạn xử lý. Tư vấn viên cần cập nhật cơ hội đúng giai đoạn thực tế để quản lý và các bộ phận liên quan theo dõi được tiến độ.

### Các giai đoạn chính

| Giai đoạn | Ý nghĩa |
|---|---|
| Tư vấn chuyên sâu | TVV tư vấn chi tiết theo nhu cầu khách hàng |
| Test tiếng Anh | Khách thực hiện hoặc được sắp xếp kiểm tra tiếng Anh nếu cần |
| Đề xuất giải pháp | TVV đề xuất chương trình, lộ trình hoặc phương án phù hợp |
| Cân nhắc đăng ký | Khách đang cân nhắc trước khi đăng ký hoặc ký hợp đồng |
| Chuyển hợp đồng | Khách đã đủ điều kiện chuyển sang bước hợp đồng |
| Thành công | Cơ hội được hệ thống tự động chuyển sang khi báo giá được `Confirm` |
| Thất bại | Cơ hội không tiếp tục, bị khóa stage và cần ghi nhận lý do |

## NGUYÊN TẮC CẬP NHẬT PIPELINE

- Khi chuyển sang giai đoạn cơ hội nếu có `Người đại diện` hoặc `Đối tác`, TVV cần kiểm tra và gom nhóm quan hệ khách hàng bằng `Create Relationship` hoặc `Related Contacts`.
- Cơ hội phải nằm đúng giai đoạn xử lý thực tế.
- Khi có thay đổi, TVV cần cập nhật stage kịp thời.
- Không để cơ hội đứng lâu ở một giai đoạn nếu đã có kết quả mới.
- Sau mỗi phiên làm việc với khách hàng, TVV phải ghi lại toàn bộ nội dung CSKH bằng `Lognote/Ghi chú` trên CRM.
- Nội dung cần ghi gồm cuộc gọi, tin nhắn, Zalo, nội dung tư vấn, phản hồi của khách, lý do chuyển stage, lý do thất bại nếu có và bước xử lý tiếp theo.
- Lognote là lịch sử chính thức để theo dõi chăm sóc khách hàng và xác minh khi có tranh chấp hoặc vấn đề phát sinh.
- Nếu khách cần follow-up, TVV cần tạo hoạt động hoặc lịch nhắc.
- Khi thất bại, phải chọn lý do thất bại rõ ràng.
- Không chuyển `Thành công` thủ công bằng tay; cơ hội chỉ tự động sang `Thành công` khi báo giá được `Confirm`.
- Từ giai đoạn `Thất bại`, cơ hội không được chuyển ngược về các giai đoạn khác.
- Khi khách đổi ý sau khi cơ hội đã `Thất bại`, TVV phải mở cơ hội của khách hàng và thực hiện lại quy trình từ đầu theo quy định nội bộ.

## QUY ĐỊNH TÊN CƠ HỘI VÀ KIỂM TRA TRÙNG

### Cấu trúc tên cơ hội

Tên cơ hội phải được đặt theo cấu trúc:

```text
Chương trình - Thị trường - Năm chương trình
```

Ví dụ:

```text
AY-USA-2026
EB3TT-USA-2027
CD-DH-CAD-2026
```

### Quy định kiểm tra trùng cơ hội

Trên cùng một khách hàng, không được phép tạo các cơ hội trùng nhau nếu cơ hội đang ở trạng thái khác `Thất bại` hoặc `Thành công`.

Nếu hệ thống phát hiện trùng, hệ thống sẽ không cho phép tạo cơ hội mới.

TVV cần:

1. Không cố tạo lại nhiều lần.
2. Kiểm tra lại danh sách cơ hội của khách hàng.
3. Liên hệ CRM Admin để kiểm tra và xử lý.

### Trường hợp được phép có nhiều cơ hội

Trên cùng một khách hàng có thể mở nhiều cơ hội do nhiều Tư vấn viên khác nhau phụ trách, miễn là không trùng tên cơ hội theo cú pháp quy định.

Ví dụ:

| Khách hàng | Cơ hội | Hợp lệ |
|---|---|---|
| Nguyễn Văn A | `AY-USA-2026` | Có |
| Nguyễn Văn A | `EB3TT-USA-2026` | Có |
| Nguyễn Văn A | `AY-USA-2026` đang xử lý | Không được tạo thêm cơ hội trùng |

## TẠO CƠ HỘI TỪ CONTACT ĐÃ CÓ

### Khi nào sử dụng?

Mục này áp dụng khi TVV muốn tạo cơ hội cho một khách hàng đã có hồ sơ trong module `Contact`.

Trước khi tạo cơ hội, TVV cần kiểm tra:

- Contact đó đã từng có cơ hội hay chưa.
- Các cơ hội hiện có có bị trùng với cơ hội chuẩn bị tạo hay không.
- Contact có đúng là khách hàng cần xử lý hay không.

### Trường hợp 1: Contact đã có cơ hội

Nếu khách hàng đã từng có cơ hội, hệ thống có thể hiển thị nút `Create Opportunity` trên hồ sơ Contact.

TVV xử lý như sau:

1. Mở đúng Contact của khách hàng.
2. Kiểm tra `Opportunity Count` hoặc danh sách cơ hội liên quan.
3. Kiểm tra các cơ hội hiện có để tránh tạo trùng.
4. Nếu không trùng theo quy định, bấm `Create Opportunity`.
5. Nhập thông tin cơ hội mới theo đúng nhu cầu, chương trình, thị trường và năm chương trình.
6. Ghi `Lognote/Ghi chú` nếu cần lưu lại lý do mở thêm cơ hội.

Lưu ý:

- Không cần biết cơ hội cũ đang thuộc TVV nào, vẫn phải kiểm tra nguyên tắc trùng trước khi tạo cơ hội mới.
- Nếu đã có cơ hội cùng tên/cùng chương trình đang ở trạng thái chưa `Thành công` hoặc chưa `Thất bại`, không tạo thêm cơ hội trùng.
- Nếu không rõ có được tạo tiếp hay không, báo quản lý hoặc CRM Admin kiểm tra.

### Trường hợp 2: Contact chưa từng có cơ hội

Nếu Contact chưa từng có cơ hội, ví dụ `Opportunity Count = 0`, hệ thống có thể chưa hiển thị hoặc chưa cho tạo cơ hội trực tiếp từ Contact.

Khi đó TVV không tạo cơ hội trực tiếp từ Contact. TVV quay lại module `Lead` để tạo Lead từ Contact đã có sẵn, sau đó thực hiện lại trình tự đánh giá Lead và chuyển cơ hội.

Các điểm cần nhớ:

1. Vào module `Lead` và tạo Lead mới.
2. Chọn Contact đã có tại trường `Tên khách hàng`.
3. Không nhập khách vào trường `Tên liên hệ` như một khách hàng mới hoàn toàn.
4. Thực hiện tiếp quy trình tạo Lead, đánh giá Lead và chuyển cơ hội.

Chi tiết thao tác xem trong tài liệu:

```text
Tạo Lead và Qualified Lead
```

## GOM NHÓM QUAN HỆ KHI CHUYỂN CƠ HỘI

### Mục tiêu

Khi Lead được chuyển sang cơ hội, nếu `Loại khách hàng` là `Người đại diện` hoặc `Đối tác`, hệ thống có thể hiển thị nút `Create Relationship`.

TVV cần bấm nút này để gom các Contact liên quan vào cùng một nhóm quan hệ.

Việc gom nhóm rất quan trọng vì:

- Không làm thất lạc khách hàng trong cùng một nhóm gia đình.
- Giúp công ty nhận diện quan hệ giữa du học sinh, bố mẹ, người thân hoặc người cùng ký.
- Hỗ trợ áp dụng promotion liên quan đến nhóm gia đình nếu có.
- Với đối tác/agent, giúp công ty xác minh quan hệ giới thiệu khách hàng.
- Là cơ sở để kiểm tra và chi trả commission cho agent đã ký hợp đồng giới thiệu khách hàng cho công ty.

### Khi nào cần Create Relationship?

| Trường hợp | Hành động |
|---|---|
| Loại khách hàng là `Người đại diện` | Bấm `Create Relationship` để gom nhóm gia đình/người thân |
| Loại khách hàng là `Đối tác` | Bấm `Create Relationship` để gom quan hệ đối tác - khách hàng |
| Nút tự động không hiện | Kiểm tra thủ công trong Contact và liên kết bằng `Related Contacts` |

### Trường hợp nút không tự động hiển thị

Trong một số trường hợp, nút `Create Relationship` có thể không hiển thị tự động.

Ví dụ:

- Dữ liệu được import từ hệ thống cũ.
- Contact chưa được mapping đúng.
- Người đại diện, người thân hoặc đối tác đã có trên hệ thống nhưng chưa được liên kết.
- Một số số điện thoại trong nhóm khách hàng đã tồn tại rời rạc trong Contact.

Khi đó, TVV cần xử lý thủ công:

1. Kiểm tra tất cả số điện thoại của nhóm khách hàng trong module `Contact`.
2. Xác định các Contact thuộc cùng một nhóm gia đình hoặc nhóm đối tác - khách hàng.
3. Mở Contact chính.
4. Vào tab `Related Contacts`.
5. Thêm các Contact liên quan.
6. Chọn đúng mối quan hệ như Bố/Mẹ, Người thân, Agent, Đối tác hoặc quan hệ phù hợp.
7. Ghi chú lại nếu cần để Admin/Quản lý kiểm tra.

Chi tiết thao tác được tách riêng trong tài liệu:

```text
Quản lý Related Contacts và nhóm quan hệ khách hàng
```

## CÁC TRƯỜNG THÔNG TIN PIPELINE CẦN ĐIỀN ĐÚNG

Trước khi cập nhật các giai đoạn xử lý, TVV cần hiểu rõ các trường thông tin trên pipeline. Các trường này không chỉ dùng để theo dõi tư vấn mà còn được hệ thống sử dụng để tạo báo giá, lấy đúng bảng giá và chọn đúng sản phẩm.

Thông tin cần cập nhật:

| Trường thông tin | Ghi chú |
|---|---|
| Nhu cầu thực tế | Phải khớp với cột `Nhu Cầu` trong bảng giá |
| Chương trình tư vấn | Phải khớp với cột `Chương Trình` trong bảng giá |
| Thị trường | Phải khớp với cột `Tại Quốc Gia` trong bảng giá |
| Năm chương trình | Năm kinh doanh thực tế theo năm học của công ty |
| Người phụ trách | TVV đang xử lý cơ hội |
| Đội ngũ kinh doanh | Team phụ trách |
| Ngày chốt dự kiến | Thời điểm dự kiến chốt |

### Dữ liệu pipeline dùng để xác định trường Bảng giá/Pricelist

Khi TVV tạo báo giá bằng `New Quotation` hoặc mở lại báo giá bằng `View Quotation`, hệ thống sẽ dùng dữ liệu đã nhập ở pipeline để xác định trường `Bảng giá/Pricelist`, sản phẩm và đơn giá phù hợp trong màn hình `Báo giá/Đơn hàng`.

Ba trường quan trọng nhất là:

| Trường trên pipeline | Cột tương ứng trong bảng giá | Bắt buộc đúng |
|---|---|---|
| Nhu cầu thực tế | `Nhu Cầu` | Có |
| Chương trình tư vấn | `Chương Trình` | Có |
| Thị trường | `Tại Quốc Gia` | Có |

Nếu chọn sai một trong ba trường này, khi mở báo giá, báo giá có thể không hiện đúng đơn giá sản phẩm.

Ví dụ đúng:

| Nhu cầu thực tế | Chương trình tư vấn | Thị trường |
|---|---|---|
| Du học cao đẳng - đại học | CĐ-ĐH | USA |
| Du học sau đại học | SAU ĐH | CAD |
| Du học trung học | THPT-AY | AUS |
| Định cư và làm việc | EB3 | USA |
| Dịch vụ du học | VISA DU HỌC | CAD |

### Cách xác định Năm chương trình

Do tính chất của công ty du học, `Năm chương trình` không được hiểu đơn giản là năm dương lịch.

`Năm chương trình` là năm kinh doanh thực tế của công ty, được tính theo năm học thực tế.

Ví dụ:

| Khoảng thời gian năm học | Năm chương trình |
|---|---|
| 09/2025 - 08/2026 | 2026 |
| 09/2026 - 08/2027 | 2027 |
| 09/2027 - 08/2028 | 2028 |

Nguyên tắc:

- Nếu chương trình bắt đầu từ tháng 9 năm trước và kết thúc tháng 8 năm sau, `Năm chương trình` lấy theo năm kết thúc.
- Ví dụ khách tham gia ký hợp đồng trong giai đoạn `09/2025 - 08/2026`, người dùng chọn `Năm chương trình` là `2026`.
- `Năm chương trình` cần được cập nhật đúng vì ảnh hưởng đến pipeline, báo giá, báo cáo doanh thu và năm kinh doanh thực tế của công ty.

## CÁC GIAI ĐOẠN XỬ LÝ CƠ HỘI

### 1. Tư vấn chuyên sâu

Mục tiêu:

TVV tư vấn sâu theo nhu cầu, thị trường, điều kiện tài chính, năng lực hồ sơ và mục tiêu của khách hàng.

Các bước thực hiện:

1. Xác nhận nhu cầu thực tế của khách.
2. Cập nhật đúng `Nhu cầu thực tế`, `Chương trình tư vấn`, `Thị trường` và `Năm chương trình`.
3. Ghi `Lognote/Ghi chú` toàn bộ nội dung tư vấn.
4. Tạo activity follow-up nếu khách cần thêm thời gian.
5. Cập nhật stage tiếp theo khi có kết quả mới.

### 2. Test tiếng Anh

Mục tiêu:

Ghi nhận tình trạng kiểm tra tiếng Anh nếu chương trình yêu cầu.

Các bước thực hiện:

1. Xác định khách có cần test tiếng Anh hay không.
2. Sắp xếp lịch test nếu cần.
3. Ghi nhận kết quả hoặc tình trạng test.
4. Cập nhật stage sang `Test tiếng Anh` nếu khách đang ở bước này.

### 3. Đề xuất giải pháp

Mục tiêu:

TVV đề xuất lộ trình, chương trình hoặc phương án phù hợp với khách.

Các bước thực hiện:

1. Xác nhận nhu cầu thực tế.
2. Đối chiếu tài chính, năng lực hồ sơ, thời điểm và mục tiêu.
3. Đề xuất giải pháp phù hợp.
4. Cập nhật đúng `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường` theo bảng giá.
5. Ghi chú nội dung đã tư vấn.
6. Chuyển cơ hội sang stage `Đề xuất giải pháp`.

### 4. Cân nhắc đăng ký

Mục tiêu:

Theo dõi khách hàng đang cân nhắc quyết định đăng ký. Giai đoạn này giúp TVV ghi nhận lý do khách còn phân vân, hẹn follow-up và chuẩn bị dữ liệu trước khi khách sẵn sàng nhận báo giá hoặc chuyển hợp đồng.

Người dùng cần làm:

1. Cập nhật stage `Cân nhắc đăng ký`.
2. Ghi chú lý do khách đang cân nhắc.
3. Tạo hoạt động follow-up.
4. Cập nhật ngày chốt dự kiến nếu có thay đổi.
5. Kiểm tra lại các trường pipeline quan trọng nếu khách đã gần đủ điều kiện nhận báo giá.

Các trường hợp thường gặp:

- Khách cần trao đổi thêm với gia đình.
- Khách cần cân nhắc tài chính.
- Khách cần so sánh với phương án khác.
- Khách cần thêm thời gian để quyết định.

### 5. Chuyển hợp đồng

Mục tiêu:

Đưa cơ hội sang bước chuẩn bị hợp đồng khi khách đã đồng ý tiếp tục.

Điều kiện thường gặp:

- Khách đã thống nhất chương trình.
- Khách đồng ý phương án tư vấn.
- Khách sẵn sàng nhận báo giá hoặc hợp đồng.
- TVV đã có đủ thông tin để chuyển sang quy trình báo giá/hợp đồng.

## KHI NÀO DÙNG NEW QUOTATION / VIEW QUOTATION

### Ý nghĩa

`Quotation` nghĩa là `Báo giá`.

Trong Opportunity:

- `New Quotation` dùng để tạo báo giá mới và chuyển sang màn hình `Báo giá/Đơn hàng`.
- `View Quotation` dùng khi cơ hội đã có quotation và TVV muốn mở lại/xem lại báo giá đó từ cơ hội.

Trong màn hình `Báo giá/Đơn hàng`, `Bảng giá/Pricelist` là một trường dữ liệu được hệ thống xác định dựa trên thông tin pipeline.

### Khi nào sử dụng?

TVV có thể tạo hoặc xem báo giá khi cơ hội đang ở:

- `Cân nhắc đăng ký`.
- `Chuyển hợp đồng`.

Không bắt buộc phải tạo báo giá ngay khi cơ hội vừa vào `Cân nhắc đăng ký`. TVV chỉ thực hiện khi đã đủ thông tin và cần gửi báo giá cho khách hàng.

### Cách thao tác ở mức pipeline

1. Mở đúng cơ hội cần gửi báo giá.
2. Kiểm tra cơ hội đang ở stage phù hợp: `Cân nhắc đăng ký` hoặc `Chuyển hợp đồng`.
3. Trước khi tạo hoặc xem báo giá, kiểm tra lại `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`.
4. Nếu chưa có báo giá, dùng `New Quotation` để tạo báo giá mới.
5. Nếu đã có báo giá, dùng `View Quotation` để mở lại báo giá đã tạo.
6. Sau khi vào màn hình `Báo giá/Đơn hàng`, thực hiện chi tiết theo tài liệu `Báo giá và đơn bán hàng`.

Nguyên tắc kiểm tra trước khi tạo hoặc xem báo giá:

- TVV phải kiểm tra lại `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`.
- Nếu báo giá không hiện đơn giá sản phẩm, kiểm tra lại ba trường trên trước khi báo lỗi hệ thống.
- Nếu đã chọn đúng nhưng vẫn không có giá, báo CRM Admin hoặc người phụ trách bảng giá kiểm tra cấu hình.

## THÀNH CÔNG VÀ THẤT BẠI

### Đánh dấu Thành công

TVV không được chuyển cơ hội sang `Thành công` thủ công bằng tay.

`Thành công` là kết quả automation khi báo giá được bấm `Confirm`.

Quy trình:

```text
Cơ hội đang xử lý
↓
Bấm New Quotation hoặc View Quotation nếu đã có báo giá
↓
Màn hình Báo giá/Đơn hàng
↓
Khách đồng ý
↓
Confirm báo giá
↓
Hệ thống tự động chuyển cơ hội sang Thành công
```

Sau khi đánh dấu thành công, người dùng tiếp tục xử lý ở tài liệu:

```text
Báo giá, đơn hàng và hợp đồng
```

### Đánh dấu Thất bại

Nếu khách hàng không tiếp tục tại bất kỳ bước nào trước `Thành công`, TVV chuyển cơ hội về giai đoạn `Thất bại` và ghi nhận lý do.

Ngoài ra, nếu đang ở bước báo giá và khách hàng không đồng ý tiếp tục ký, TVV bấm `Cancel` báo giá. Khi báo giá bị cancel, hệ thống tự động chuyển cơ hội về `Thất bại`.

Các lý do thất bại thường gặp:

| Lý do thất bại | Mô tả |
|---|---|
| Tài chính không phù hợp | Khách không đáp ứng hoặc chưa phù hợp về tài chính |
| Đã tư vấn không phản hồi | Đã tư vấn nhưng khách không phản hồi tiếp |
| Không phù hợp điều kiện | Khách không đáp ứng điều kiện chương trình |
| Thời gian chưa phù hợp | Thời điểm tham gia chưa phù hợp |
| Lý lịch tư pháp | Khách gặp vấn đề liên quan đến lý lịch tư pháp |
| Mục tiêu du học khác | Mục tiêu của khách không phù hợp chương trình tư vấn |
| Không phù hợp độ tuổi | Độ tuổi không phù hợp chương trình |
| Xuất khẩu lao động | Khách quan tâm hướng xuất khẩu lao động thay vì chương trình tư vấn |
| Năng lực đảng viên | Không phù hợp do yếu tố năng lực/hồ sơ đảng viên |
| Tìm hiểu cho biết | Khách chỉ tìm hiểu thông tin, chưa có nhu cầu thực tế |
| Đổi người đứng đương đơn | Cần thay đổi người đứng đương đơn |
| Đơn hàng bị huỷ | Đơn hàng hoặc báo giá đã bị hủy |

Sau khi thất bại:

```text
Thất bại
↓
Ghi nhận lý do
↓
Chuyển CSKH nếu cần chăm sóc lại
```

Lưu ý:

- Không để cơ hội thất bại mà không có lý do.
- Khi cơ hội đã về giai đoạn `Thất bại`, người dùng không được chuyển về các giai đoạn khác.
- Nếu khách hàng thay đổi ý định sau khi đã thất bại, TVV phải mở lại cơ hội của khách hàng và thực hiện quy trình lại từ đầu theo quy định nội bộ.

## CÁC BƯỚC THỰC HIỆN TRÊN ODOO

### Bước 1: Mở pipeline cơ hội

1. Vào module `CRM`.
2. Chọn menu `Bán hàng`.
3. Chọn `Quy trình của tôi` hoặc pipeline được phân quyền.
4. Kiểm tra các cột stage trên màn hình Kanban.

### Bước 2: Mở cơ hội cần xử lý

1. Tìm cơ hội theo tên khách hàng, mã cơ hội hoặc số điện thoại.
2. Mở cơ hội.
3. Kiểm tra thông tin khách hàng, nhu cầu thực tế, chương trình tư vấn, thị trường, năm chương trình và người phụ trách.

### Bước 3: Cập nhật stage

1. Xác định tình trạng xử lý thực tế.
2. Cập nhật stage phù hợp.
3. Ghi chú nội dung trao đổi nếu có.
4. Tạo hoạt động follow-up nếu khách chưa có quyết định.

### Bước 4: Tạo hoặc xem báo giá khi cần gửi khách hàng

1. Kiểm tra cơ hội đang ở stage phù hợp: `Cân nhắc đăng ký` hoặc `Chuyển hợp đồng`.
2. Xác định khách đã đủ thông tin và cần nhận báo giá.
3. Trước khi tạo hoặc xem báo giá, kiểm tra đúng `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`.
4. Nếu chưa có báo giá, dùng `New Quotation`.
5. Nếu đã có báo giá, dùng `View Quotation`.
6. Khi vào màn hình `Báo giá/Đơn hàng`, tiếp tục theo tài liệu `Báo giá và đơn bán hàng`.
7. Nếu báo giá không hiện đơn giá sản phẩm, quay lại kiểm tra ba trường dữ liệu pipeline theo bảng giá.
8. Nếu khách đồng ý, tiếp tục xử lý báo giá theo tài liệu báo giá/hợp đồng.
9. Nếu khách không đồng ý tiếp tục ký, bấm `Cancel` báo giá để hệ thống chuyển cơ hội về `Thất bại`.

### Bước 5: Xử lý Thành công hoặc Thất bại

1. Nếu khách đồng ý và báo giá được `Confirm`, hệ thống tự động chuyển cơ hội sang `Thành công`.
2. Không chuyển `Thành công` thủ công bằng tay.
3. Nếu khách không tiếp tục ở bất kỳ bước nào trước Thành công, chuyển cơ hội về `Thất bại` và chọn lý do.
4. Nếu báo giá bị `Cancel`, hệ thống tự động chuyển cơ hội về `Thất bại`.
5. Nếu cần CSKH chăm sóc lại, ghi chú rõ nội dung cần bàn giao.

## KẾT QUẢ MONG ĐỢI

Sau khi thực hiện đúng quy trình:

- Cơ hội được cập nhật đúng stage.
- Thông tin khách hàng, nhu cầu thực tế, chương trình tư vấn, thị trường và ngày chốt dự kiến được cập nhật rõ ràng.
- Dữ liệu pipeline khớp với bảng giá để khi mở báo giá, trường `Bảng giá/Pricelist` và sản phẩm được xác định đúng.
- TVV biết tạo báo giá bằng `New Quotation` hoặc mở lại báo giá đã có bằng `View Quotation`.
- Cơ hội chỉ chuyển `Thành công` tự động khi báo giá được `Confirm`.
- Cơ hội thất bại có lý do rõ ràng.
- Cơ hội đã `Thất bại` không được chuyển ngược về stage khác.
- Tên cơ hội đúng cấu trúc `Chương trình - Thị trường - Năm chương trình`.
- Hệ thống ngăn tạo cơ hội trùng trên cùng khách hàng nếu cơ hội chưa `Thất bại` hoặc `Thành công`.
- Cơ hội thành công sẵn sàng chuyển sang quy trình báo giá/hợp đồng.

## LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Cơ hội nằm sai stage | TVV quên cập nhật pipeline | Cập nhật lại stage theo tình trạng thực tế |
| Không có lịch follow-up | TVV chưa tạo hoạt động sau tư vấn | Tạo activity hoặc lịch nhắc xử lý |
| Báo giá không hiện đơn giá sản phẩm | Sai `Nhu cầu thực tế`, `Chương trình tư vấn` hoặc `Thị trường`, làm trường `Bảng giá/Pricelist` chưa đúng | Kiểm tra lại dữ liệu pipeline theo bảng giá |
| Thất bại nhưng không có lý do | Người dùng chỉ chọn Thất bại nhưng không ghi nhận nguyên nhân | Chọn hoặc ghi rõ lý do thất bại |
| TVV chuyển Thành công thủ công | Chưa hiểu quy tắc automation | Không chuyển tay; Thành công chỉ tự động khi báo giá được Confirm |
| Cancel báo giá nhưng chưa về Thất bại | Hệ thống chưa chạy hoặc dữ liệu chưa đồng bộ | Kiểm tra lại báo giá/cơ hội và báo Admin nếu cần |
| Muốn kéo cơ hội từ Thất bại về stage khác | Cơ hội thất bại bị khóa stage | Mở lại cơ hội và thực hiện quy trình lại từ đầu theo quy định |
| Tạo cơ hội bị báo trùng | Trên cùng khách hàng đã có cơ hội cùng tên chưa Thành công/Thất bại | Liên hệ Admin kiểm tra xử lý |
| Không thấy nút `Create Opportunity` trên Contact | Contact chưa từng có cơ hội hoặc dữ liệu cũ chưa mapping đủ | Quay lại module `Lead`, tạo Lead mới và chọn Contact tại trường `Tên khách hàng` |
| Tạo cơ hội từ Contact bị báo trùng | Contact đã có cơ hội cùng tên/chương trình đang xử lý | Không tạo thêm, báo Admin hoặc quản lý kiểm tra |
| Tên cơ hội sai cú pháp | Chưa đặt theo `Chương trình - Thị trường - Năm chương trình` | Cập nhật lại tên cơ hội đúng chuẩn |
| Thông tin khách hàng bị nhầm vai trò | Khách hàng và người đại diện chưa được cập nhật đúng | Cập nhật lại thông tin khách hàng trước khi xử lý tiếp |

## CHECKLIST CHO TVV

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Đã ghi `Lognote/Ghi chú` toàn bộ nội dung CSKH sau phiên làm việc |  |  |
| Đã mở đúng cơ hội |  |  |
| Đã kiểm tra khách hàng/người đại diện |  |  |
| Đã cập nhật stage đúng thực tế |  |  |
| Đã cập nhật nhu cầu thực tế |  |  |
| Đã cập nhật chương trình tư vấn |  |  |
| Đã cập nhật thị trường đúng theo bảng giá |  |  |
| Bộ 3 nhu cầu/chương trình/thị trường khớp bảng giá |  |  |
| Đã cập nhật năm chương trình |  |  |
| Tên cơ hội đúng cú pháp |  |  |
| Đã kiểm tra cơ hội trùng trên cùng khách hàng |  |  |
| Nếu tạo từ Contact, đã kiểm tra `Opportunity Count` |  |  |
| Nếu Contact đã có cơ hội, đã kiểm tra nút `Create Opportunity` |  |  |
| Nếu Contact chưa từng có cơ hội, đã quay lại module Lead để tạo Lead đúng trình tự |  |  |
| Đã cập nhật ngày chốt dự kiến |  |  |
| Nếu có người đại diện/đối tác, đã gom nhóm quan hệ |  |  |
| Nếu nút Create Relationship không hiện, đã kiểm tra Related Contacts |  |  |
| Đã ghi chú nội dung tư vấn quan trọng |  |  |
| Đã tạo activity follow-up nếu cần |  |  |
| Nếu cần gửi báo giá, đã xác định dùng `New Quotation` hay `View Quotation` |  |  |
| Không chuyển Thành công thủ công |  |  |
| Nếu báo giá Confirm, đã kiểm tra cơ hội tự sang Thành công |  |  |
| Nếu báo giá Cancel, đã kiểm tra cơ hội tự sang Thất bại |  |  |
| Nếu Thất bại, đã chọn lý do thất bại |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Cập nhật stage cơ hội

Yêu cầu:

1. Mở pipeline cơ hội.
2. Chọn một cơ hội đang xử lý.
3. Cập nhật stage theo tình huống giảng viên đưa ra.
4. Ghi chú nội dung tư vấn.
5. Tạo activity follow-up nếu khách chưa quyết định.

Kết quả cần đạt:

- Người dùng biết cách cập nhật pipeline.
- Cơ hội nằm đúng giai đoạn xử lý thực tế.

### Bài 2: Kiểm tra Create Relationship

Yêu cầu:

1. Mở một cơ hội có loại khách hàng là `Người đại diện` hoặc `Đối tác`.
2. Kiểm tra hệ thống có hiển thị nút `Create Relationship` hay không.
3. Nếu có, bấm `Create Relationship`.
4. Kiểm tra nhóm quan hệ được tạo đúng.
5. Nếu không có nút, kiểm tra các số điện thoại liên quan trong module `Contact`.
6. Ghi chú trường hợp cần liên kết thủ công bằng `Related Contacts`.

Kết quả cần đạt:

- Người dùng hiểu khi nào cần gom nhóm quan hệ.
- Người dùng không bỏ sót người đại diện, người thân hoặc đối tác liên quan đến khách hàng.

### Bài 3: Kiểm tra New Quotation / View Quotation

Yêu cầu:

1. Mở một cơ hội ở stage `Cân nhắc đăng ký` hoặc `Chuyển hợp đồng`.
2. Xác định tình huống khách cần nhận báo giá.
3. Kiểm tra `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`.
4. Đối chiếu ba trường này với bảng giá.
5. Nếu chưa có báo giá, xác định cần dùng `New Quotation`.
6. Nếu đã có báo giá, xác định dùng `View Quotation`.
7. Kiểm tra báo giá có lấy được đơn giá sản phẩm hay không.
8. Ghi nhận trường hợp khách đồng ý hoặc không đồng ý.

Kết quả cần đạt:

- Người dùng biết `New Quotation` là tạo báo giá mới, còn `View Quotation` là mở lại báo giá đã có.
- Người dùng hiểu dữ liệu pipeline phải khớp bảng giá thì báo giá mới có đúng trường `Bảng giá/Pricelist` và sản phẩm.
- Người dùng hiểu báo giá liên quan đến automation Thành công/Thất bại.

### Bài 4: Đánh dấu Thất bại

Yêu cầu:

1. Mở một cơ hội không tiếp tục.
2. Chọn `Thất bại`.
3. Chọn lý do thất bại.
4. Ghi chú nội dung cần CSKH theo dõi nếu có.

Kết quả cần đạt:

- Cơ hội được đóng đúng lý do.
- Người dùng không để cơ hội thất bại thiếu thông tin.

### Bài 5: Kiểm tra Thành công tự động

Yêu cầu:

1. Mở một cơ hội đã được khách đồng ý.
2. Kiểm tra thông tin cơ hội.
3. Mở báo giá liên quan.
4. Bấm `Confirm`.
5. Kiểm tra cơ hội tự động chuyển sang `Thành công`.

Kết quả cần đạt:

- Người dùng hiểu không chuyển `Thành công` thủ công.
- Người dùng biết Thành công là kết quả automation từ báo giá Confirm.

### Bài 6: Kiểm tra trùng tên cơ hội

Yêu cầu:

1. Mở hồ sơ một khách hàng đã có cơ hội đang xử lý.
2. Kiểm tra tên cơ hội theo cú pháp.
3. Thử xác định trường hợp trùng tên cơ hội.
4. Ghi nhận hướng xử lý là báo CRM Admin.

Kết quả cần đạt:

- Người dùng hiểu quy định tên cơ hội.
- Người dùng không tạo cơ hội trùng trên cùng khách hàng.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Opportunity Pipeline Process |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / CRM / Opportunity Management |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
| Ngày phát hành |  |
