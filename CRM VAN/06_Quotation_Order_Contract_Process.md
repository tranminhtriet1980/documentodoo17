# BÁO GIÁ VÀ ĐƠN BÁN HÀNG

## GIỚI THIỆU

### Mục tiêu

Tài liệu này hướng dẫn TVV xử lý quy trình báo giá và đơn bán hàng sau khi cơ hội đủ điều kiện báo giá.

Phạm vi tài liệu chỉ bao gồm:

- Tạo báo giá mới bằng nút `New Quotation` khi cơ hội cần gửi báo giá cho khách hàng.
- Mở lại báo giá đã có bằng nút `View Quotation` khi đứng ở cơ hội.
- Kiểm tra và điền đúng dữ liệu trên báo giá.
- Xử lý đúng `Discount` hoặc `Promotion` nếu khách có ưu đãi.
- Gửi email báo giá.
- Confirm khi khách hàng đồng ý.
- Kiểm tra trạng thái `Đơn bán hàng`.
- Nắm nguyên tắc xử lý khi khách đổi sản phẩm, huỷ đơn hàng và tính KPI.

Trọng tâm tài liệu vẫn là thao tác CRM dành cho TVV. Các phần liên quan đến kế toán và KPI được đưa vào để TVV hiểu nguyên tắc phối hợp sau khi đơn hàng được tạo.

### Vị trí trong quy trình

```text
Cơ hội đủ điều kiện báo giá
↓
Bấm New Quotation
↓
Màn hình Báo giá/Đơn hàng
↓
Gửi email
↓
Báo giá đã gửi
↓
Khách đồng ý
↓
Confirm
↓
Đơn bán hàng
```

### Đối tượng sử dụng

| Nhóm người dùng | Vai trò |
|---|---|
| Tư vấn viên | Kiểm tra báo giá, gửi email, confirm đơn hàng |
| Quản lý kinh doanh | Kiểm tra thông tin báo giá và đơn bán hàng |
| Kế toán | Kiểm tra đơn hàng cuối cùng, xử lý huỷ đơn, hoàn tất hợp đồng và cập nhật điều kiện ghi nhận KPI |
| CRM Admin | Hỗ trợ lỗi bảng giá, mã hợp đồng hoặc sản phẩm |

Trọng tâm training của tài liệu này là thao tác CRM dành cho TVV. Phần kế toán chỉ được nhắc ở mức TVV cần biết để hiểu vì sao đơn hàng có thể bị trả lại.

Sau mỗi phiên làm việc với khách hàng trong quy trình báo giá hoặc đơn hàng, TVV phải ghi lại toàn bộ nội dung CSKH bằng `Lognote/Ghi chú` trên CRM. Nội dung cần ghi gồm trao đổi về báo giá, ưu đãi, voucher, promotion, xác nhận đồng ý, lý do khách chưa ký, lý do cancel, đơn hàng bị trả lại hoặc yêu cầu chỉnh sửa. Đây là căn cứ chính thức để xác minh lịch sử chăm sóc khách hàng và phối hợp với kế toán/quản lý.

## TRẠNG THÁI BÁO GIÁ / ĐƠN HÀNG

### Ba trạng thái chính

| Trạng thái | Ý nghĩa | Hành động của TVV |
|---|---|---|
| Báo giá | Quotation mới được tạo từ nút `New Quotation` | Kiểm tra và điền đúng thông tin, trường `Bảng giá/Pricelist`, mã hợp đồng và sản phẩm |
| Báo giá đã gửi | Báo giá đã được gửi email cho khách hàng | Theo dõi phản hồi của khách |
| Đơn bán hàng | Khách đồng ý và TVV đã bấm `Confirm` | Kiểm tra đơn bán hàng |

### Nguyên tắc trạng thái

- `Báo giá` là trạng thái ban đầu khi TVV mở báo giá.
- Sau khi gửi email thành công, trạng thái chuyển sang `Báo giá đã gửi`.
- Khi khách đồng ý và TVV bấm `Confirm`, trạng thái chuyển sang `Đơn bán hàng`.
- Nếu khách không đồng ý tiếp tục ký, TVV bấm `Cancel` báo giá. Hệ thống sẽ xử lý theo automation của pipeline.

## DỮ LIỆU BÁO GIÁ BẮT BUỘC ĐÚNG

### Dữ liệu cần kiểm tra trên báo giá

Khi TVV bấm `New Quotation`, hệ thống tạo báo giá mới và mở sang màn hình `Báo giá/Đơn hàng`.

Khi TVV bấm `View Quotation`, hệ thống mở lại báo giá đã có từ cơ hội. Đây không phải là thao tác tạo báo giá mới.

Trên màn hình `Báo giá/Đơn hàng`, hệ thống lấy dữ liệu từ cơ hội để xác định trường `Bảng giá/Pricelist`, mã hợp đồng và danh sách sản phẩm.

Các trường cần kiểm tra:

| Trường thông tin | Ghi chú |
|---|---|
| Báo giá/Quotation | Đúng báo giá của cơ hội và đúng khách hàng |
| Khách hàng | Đúng khách hàng hoặc người đại diện liên quan |
| Email | Bắt buộc nếu gửi báo giá qua email |
| Ngày sinh | Bắt buộc trước khi confirm nếu hệ thống yêu cầu |
| Địa chỉ | Bắt buộc trước khi confirm nếu hệ thống yêu cầu |
| Nhu cầu | Phải khớp bảng giá |
| Chương trình | Phải khớp bảng giá |
| Thị trường | Phải khớp bảng giá |
| Năm chương trình | Đúng năm kinh doanh thực tế |
| Bảng giá/Pricelist | Phải đúng theo nhu cầu, chương trình, thị trường và năm chương trình |
| Sản phẩm trong `Order Lines` | Phải mở đúng và chọn đủ sản phẩm cần báo giá |
| VP tư vấn | Đúng văn phòng phụ trách |

### Thông tin khách hàng phục vụ team Docs

Trong đơn hàng, TVV cần kiểm tra thêm tab `Other Info`, phần `Thông tin khách hàng`.

Những thông tin này không chỉ phục vụ báo giá. Đây là dữ liệu đầu vào để team Docs tiếp nhận và xử lý hồ sơ sau này. Nếu thiếu hoặc sai, đơn hàng có thể bị kế toán trả lại để TVV chỉnh trước khi chuyển tiếp.

Đối với chương trình định cư:

| Trường thông tin | Ghi chú |
|---|---|
| Hãng xưởng | Bắt buộc nếu chương trình yêu cầu thông tin hãng xưởng |

Đối với chương trình du học:

| Trường thông tin | Ghi chú |
|---|---|
| Lớp | Lớp hiện tại hoặc lớp theo thông tin tư vấn trên hệ thống |
| Kỳ nhập học | Kỳ nhập học dự kiến của khách hàng |
| Tên trường | Tên trường theo chương trình tư vấn |
| Tổ chức (tuỳ chương trình) | Tổ chức tham gia |
| Ngành học (tuỳ chương trình) | Ngành học khách hàng đăng ký |

TVV cần nhập đúng theo thông tin đã tư vấn với khách hàng. Không bỏ trống các trường hệ thống yêu cầu bắt buộc.


## DISCOUNT VÀ PROMOTION

### Phân biệt hai nút

| Nút | Dùng khi nào | Lưu ý bắt buộc |
|---|---|---|
| `Discount` | Chỉ dùng cho voucher được tặng riêng cho khách hàng | TVV phải `Add note` ghi rõ sử dụng voucher gì |
| `Promotion` | Dùng cho ưu đãi hội thảo, sự kiện lớn hoặc chương trình ưu đãi chính thức của công ty | Không dùng `Discount` thay cho `Promotion` |

TVV không được bấm `Discount` cho các promotion của công ty. Kế toán sẽ kiểm tra đơn hàng cuối cùng; nếu thấy dùng sai thao tác, kế toán không duyệt đơn hàng và trả lại TVV để xử lý đúng.

### Quy tắc sử dụng Discount

`Discount` chỉ sử dụng khi khách hàng có voucher hợp lệ.

Khi dùng `Discount`, TVV cần thực hiện:

1. Kiểm tra voucher khách hàng được tặng.
2. Bấm `Discount`.
3. Nhập mức chiết khấu theo đúng voucher.
4. `Add note` trên báo giá/đơn hàng để ghi rõ thông tin voucher.

Ví dụ nội dung note:

```text
Khách sử dụng voucher [tên voucher/mã voucher] theo chương trình [tên chương trình].
```

### Quy tắc sử dụng Promotion

`Promotion` sử dụng cho các ưu đãi chính thức của công ty, ví dụ ưu đãi hội thảo, chương trình sự kiện lớn, hoặc ưu đãi theo nhóm khách hàng liên quan.

Để bấm được `Promotion`, khách hàng phải đủ điều kiện theo cấu hình hệ thống.

Trường hợp promotion theo chiến dịch sự kiện:

- TVV vào `Contact` của khách hàng.
- Bấm `Register Campaign`.
- Chọn đúng tên campaign/sự kiện áp dụng cho khách hàng.
- Khách hàng phải đăng ký đúng sự kiện được tạo trên hệ thống.
- `Nhu cầu` và `Chương trình` phải đúng với tiêu chí sự kiện.
- Thời gian ưu đãi vẫn còn hiệu lực.
- Nếu sự kiện yêu cầu check-in, khách hàng phải có check-in hợp lệ.

Trường hợp promotion theo nhóm liên hệ:

- Áp dụng cho các ưu đãi như du học sinh ký định cư, phụ huynh du học sinh, hoặc người thân cùng ký.
- Khách hàng phải đăng ký đúng tiêu đề sự kiện/chương trình promotion.
- Hệ thống kiểm tra `Related Contacts` để xác định nhóm khách hàng có liên quan.
- Nếu nhóm liên hệ chưa được gom đúng, TVV cần kiểm tra và xử lý theo quy trình `Related Contacts` trước khi áp dụng promotion.

## THAY ĐỔI SẢN PHẨM, HUỶ ĐƠN HÀNG VÀ KPI

### Trường hợp khách thay đổi sản phẩm trước khi ký hợp đồng

Nếu khách chưa ký hợp đồng nhưng muốn thay đổi sản phẩm, chương trình, thị trường hoặc năm chương trình, TVV không chỉnh trực tiếp trên báo giá để khớp tạm.

TVV cần quay lại quy trình Opportunity để cập nhật đúng dữ liệu pipeline:

```text
Khách muốn thay đổi sản phẩm trước khi ký
↓
Quay lại Opportunity
↓
Cập nhật Nhu cầu thực tế / Chương trình tư vấn / Thị trường / Năm chương trình
↓
Mở lại báo giá bằng View Quotation hoặc tạo báo giá mới bằng New Quotation theo tình huống hệ thống
↓
Tiếp tục gửi email báo giá và Confirm nếu khách đồng ý
```

Nguyên tắc:

- Báo giá và đơn hàng phải đi theo dữ liệu đúng từ Opportunity.
- Không sửa tay sản phẩm trên báo giá nếu dữ liệu pipeline đang sai.
- Sau khi Opportunity được cập nhật đúng, TVV tiếp tục thực hiện các bước cuối của đơn hàng: kiểm tra báo giá, gửi email báo giá và `Confirm` khi khách đồng ý.

### Trường hợp khách đã ký nhưng muốn thay đổi sản phẩm

Nếu khách hàng đã ký nhưng sau đó muốn thay đổi sản phẩm/chương trình, TVV không chỉnh trực tiếp trên đơn hàng cũ theo cách thủ công.

Quy trình xử lý:

```text
Khách muốn thay đổi sản phẩm
↓
TVV tạo cơ hội mới
↓
TVV tạo đơn hàng mới theo sản phẩm mới
↓
Kế toán huỷ toàn bộ đơn hàng cũ
↓
Đơn hàng mới được dùng để xử lý tiếp
```

Nguyên tắc:

- Đơn hàng cũ được kế toán xử lý huỷ toàn bộ.
- TVV tạo cơ hội mới và đơn hàng mới theo đúng sản phẩm/chương trình mới.
- Không tự sửa sản phẩm trên đơn hàng cũ nếu quy trình yêu cầu tạo đơn mới.
- Điểm KPI của TVV vẫn giữ nguyên theo nguyên tắc ghi nhận nội bộ.
- TVV cần ghi `Lognote/Ghi chú` lý do khách đổi sản phẩm và đơn hàng mới liên quan.

### Nguyên tắc tính điểm KPI

Điểm KPI được tính dựa trên:

- Hợp đồng.
- Ngày đóng tiền của khách hàng.

Kế toán chịu trách nhiệm hoàn thành hợp đồng trên hệ thống để điểm KPI của TVV được nhảy lên hệ thống.

TVV cần lưu ý:

- Kiểm tra thông tin đơn hàng, khách hàng, sản phẩm và chương trình trước khi confirm.
- Nếu phát hiện sai thông tin ảnh hưởng đến hợp đồng hoặc KPI, báo kế toán/quản lý xử lý sớm.
- Không tự kết luận điểm KPI đã được ghi nhận nếu kế toán chưa hoàn thành bước hợp đồng trên hệ thống.

### Trường hợp cancel đơn hàng

| Trường hợp cancel | Nguyên tắc KPI |
|---|---|
| Đơn hàng huỷ hoàn tiền | Huỷ toàn bộ điểm của đơn hàng đó |
| Đơn hàng huỷ không hoàn tiền | Giữ nguyên điểm |

Kế toán là bộ phận xử lý nghiệp vụ huỷ đơn hàng trên hệ thống. TVV cần ghi nhận rõ lý do khách huỷ hoặc thay đổi trên `Lognote/Ghi chú` để có căn cứ kiểm tra.

### Trường hợp chuyển điểm giữa các TVV

Nguyên tắc chuyển điểm:

| Trường hợp | Cách xử lý |
|---|---|
| Chuyển điểm trong cùng kỳ | Chuyển điểm cho người phụ trách cuối |
| Khác kỳ | Không chuyển điểm |

Một kỳ KPI được tính theo 4 tháng trong năm kinh doanh của công ty.

Ví dụ:

```text
TVV A ký khách trong tháng 10.
Tháng 12 TVV A nghỉ việc và bàn giao khách cho TVV B.
Vì vẫn cùng kỳ, điểm được chuyển cho TVV B.
```

```text
TVV A ký khách trong tháng 10.
Tháng 1 TVV A nghỉ việc và bàn giao khách cho TVV B.
Vì đã sang kỳ KPI mới, điểm không chuyển cho TVV B.
```

Khi có bàn giao khách hoặc chuyển người phụ trách, TVV/quản lý cần ghi rõ trên `Lognote/Ghi chú` để có căn cứ xác minh.

## QUY TRÌNH THỰC HIỆN

### Bước 1: Tạo hoặc mở báo giá từ cơ hội

1. Mở đúng cơ hội cần báo giá cho khách hàng.
2. Nếu cơ hội chưa có báo giá và cần gửi báo giá mới cho khách, bấm `New Quotation`.
3. Nếu cơ hội đã có báo giá, bấm `View Quotation` để mở lại báo giá đã tạo.
4. Hệ thống chuyển sang màn hình `Báo giá/Đơn hàng`.
5. Kiểm tra đây là màn hình báo giá của đúng khách hàng và đúng cơ hội.

Lưu ý:

- `New Quotation` là tạo báo giá mới.
- `View Quotation` là mở lại báo giá đã có.

### Bước 2: Kiểm tra và điền đúng thông tin báo giá

1. Kiểm tra `Báo giá/Quotation` đang mở đúng cơ hội và đúng khách hàng.
2. Kiểm tra `Khách hàng`.
3. Kiểm tra `Nhu cầu`.
4. Kiểm tra `Chương trình`.
5. Kiểm tra `Thị trường`.
6. Kiểm tra `Năm chương trình`.
7. Kiểm tra trường `Bảng giá/Pricelist`.
8. Kiểm tra `Mã hợp đồng`.
9. Kiểm tra sản phẩm trong tab `Order Lines` đã mở đúng theo bảng giá.
10. Chọn đủ sản phẩm cần báo giá cho khách hàng.
11. Kiểm tra tab `Other Info`, phần `Thông tin khách hàng`, đặc biệt với chương trình định cư và du học.

Nếu một trong các trường `Nhu cầu`, `Chương trình`, `Thị trường`, `Năm chương trình` đang sai, TVV không chọn sản phẩm gần đúng trên báo giá. TVV cần quay lại Opportunity để cập nhật đúng dữ liệu, sau đó mở lại báo giá bằng `View Quotation` hoặc tạo báo giá mới bằng `New Quotation` theo tình huống hệ thống.

Nếu danh sách sản phẩm không hiện đúng hoặc không có đơn giá, TVV kiểm tra lại `Bảng giá/Pricelist` và các trường dữ liệu từ Opportunity trước khi báo lỗi hệ thống.

### Bước 3: Xử lý Discount hoặc Promotion nếu có

1. Xác định khách đang dùng voucher hay promotion của công ty.
2. Nếu là voucher, dùng nút `Discount` và `Add note` thông tin voucher.
3. Nếu là ưu đãi hội thảo, sự kiện hoặc chương trình ưu đãi công ty, dùng nút `Promotion`.
4. Nếu promotion theo campaign/sự kiện, vào `Contact` khách hàng, bấm `Register Campaign`, và chọn đúng tên campaign.
5. Kiểm tra điều kiện promotion trước khi gửi báo giá.
6. Nếu promotion không áp dụng được, kiểm tra lại đăng ký sự kiện, thời hạn hiệu lực, check-in nếu có, và `Related Contacts` nếu là ưu đãi theo nhóm.

### Bước 4: Gửi email báo giá

1. Kiểm tra email khách hàng.
2. Chọn `Gửi email`.
3. Nếu hệ thống báo thiếu email, bổ sung email khách hàng.
4. Gửi lại email.
5. Kiểm tra trạng thái chuyển sang `Báo giá đã gửi`.
6. Nếu có nội dung trao đổi quan trọng với khách sau khi gửi báo giá, ghi `Lognote/Ghi chú`.

### Bước 5: Confirm khi khách đồng ý

1. Xác nhận khách hàng đã đồng ý.
2. Kiểm tra ngày sinh khách hàng.
3. Kiểm tra địa chỉ khách hàng.
4. Kiểm tra thông tin khách hàng phục vụ team Docs trong tab `Other Info`.
5. Chọn `Confirm`.
6. Nếu hệ thống báo thiếu ngày sinh, địa chỉ hoặc thông tin bắt buộc khác, bổ sung thông tin còn thiếu.
7. Chọn `Confirm` lại.
8. Kiểm tra trạng thái chuyển sang `Đơn bán hàng`.
9. Nếu kế toán trả lại đơn hàng do sai thông tin, TVV kiểm tra nội dung được yêu cầu chỉnh và cập nhật lại trên CRM.
10. Ghi `Lognote/Ghi chú` nếu có nội dung xác nhận, điều chỉnh hoặc trả lại đơn hàng cần lưu lịch sử.

## LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Báo giá không hiện đơn giá sản phẩm | Sai `Nhu cầu`, `Chương trình`, `Thị trường` hoặc `Năm chương trình` | Kiểm tra lại dữ liệu Opportunity và trường `Bảng giá/Pricelist` trên báo giá |
| `Bảng giá/Pricelist` không đúng | Dữ liệu từ Opportunity chuyển sang báo giá chưa đúng | Kiểm tra `Nhu cầu`, `Chương trình`, `Thị trường` và `Năm chương trình` |
| Mã hợp đồng không đúng | Trường `Bảng giá/Pricelist`, chương trình, thị trường hoặc năm chương trình chưa đúng | Kiểm tra dữ liệu Opportunity, kiểm tra lại báo giá và báo CRM Admin nếu cần |
| Không thấy sản phẩm cần chọn | Trường `Bảng giá/Pricelist` chưa đúng hoặc dữ liệu Opportunity đang sai | Kiểm tra trường `Bảng giá/Pricelist`, dữ liệu Opportunity và danh sách sản phẩm trong `Order Lines` |
| Dùng sai nút `Discount` cho promotion công ty | TVV thao tác nhầm giữa voucher và promotion | Huỷ thao tác sai nếu có thể, dùng lại nút `Promotion`, hoặc báo Admin/Kế toán hỗ trợ |
| `Promotion` không áp dụng được | Khách chưa đăng ký đúng sự kiện, sai nhu cầu/chương trình, hết hiệu lực, chưa check-in hoặc thiếu related contact | Kiểm tra điều kiện promotion và cập nhật lại dữ liệu liên quan |
| Gửi email bị báo lỗi thiếu email | Khách hàng chưa có email | Bổ sung email khách hàng rồi gửi lại |
| Confirm bị báo lỗi thiếu ngày sinh | Hồ sơ khách hàng thiếu ngày sinh | Bổ sung ngày sinh rồi confirm lại |
| Confirm bị báo lỗi thiếu địa chỉ | Hồ sơ khách hàng thiếu địa chỉ | Bổ sung địa chỉ rồi confirm lại |
| Kế toán trả lại đơn hàng do thiếu thông tin khách hàng | Tab `Other Info` chưa đủ dữ liệu cho chương trình định cư hoặc du học | Bổ sung đúng thông tin khách hàng theo yêu cầu rồi gửi kiểm tra lại |
| Khách muốn đổi sản phẩm trước khi ký | Dữ liệu Opportunity không còn đúng với sản phẩm khách muốn chọn | Quay lại Opportunity cập nhật nhu cầu thực tế, chương trình, thị trường hoặc năm chương trình rồi tạo lại báo giá bằng `New Quotation`, hoặc mở lại bằng `View Quotation` nếu đã có báo giá |
| Khách muốn đổi sản phẩm sau khi đã ký | Cần tạo cơ hội mới và đơn hàng mới | TVV tạo cơ hội/đơn hàng mới, kế toán huỷ đơn cũ theo quy trình |
| Huỷ đơn hàng nhưng chưa rõ ảnh hưởng KPI | Chưa xác định huỷ hoàn tiền hay không hoàn tiền | Kiểm tra với kế toán/quản lý trước khi kết luận điểm KPI |
| Tranh chấp chuyển điểm giữa TVV | Không rõ thời điểm bàn giao hoặc khác kỳ KPI | Kiểm tra lognote, ngày ký, ngày đóng tiền và kỳ KPI |
| Confirm khi khách chưa đồng ý | TVV thao tác quá sớm | Không confirm nếu chưa có xác nhận của khách |

## KẾT QUẢ MONG ĐỢI

Sau khi thực hiện đúng quy trình:

- Báo giá được mở đúng từ cơ hội đủ điều kiện.
- TVV phân biệt được `New Quotation` là tạo báo giá mới, còn `View Quotation` là mở lại báo giá đã có.
- Báo giá có đúng `Bảng giá/Pricelist`, mã hợp đồng và sản phẩm trong `Order Lines`.
- Nếu khách đổi sản phẩm trước khi ký, TVV biết quay lại Opportunity để cập nhật dữ liệu pipeline trước khi tiếp tục báo giá.
- TVV phân biệt đúng `Discount` cho voucher và `Promotion` cho ưu đãi công ty.
- Email được gửi sau khi khách hàng có email.
- Trạng thái chuyển đúng từ `Báo giá` sang `Báo giá đã gửi`.
- Confirm chỉ thực hiện khi khách đồng ý.
- Nếu thiếu ngày sinh, địa chỉ hoặc thông tin khách hàng phục vụ team Docs, TVV biết cách bổ sung và confirm lại.
- Trạng thái chuyển đúng sang `Đơn bán hàng`.
- TVV hiểu cách xử lý khi khách đổi sản phẩm sau khi đã ký.
- TVV hiểu nguyên tắc huỷ đơn hàng và ảnh hưởng KPI ở mức cần biết.
- TVV hiểu điểm KPI phụ thuộc hợp đồng, ngày đóng tiền và bước hoàn thành của kế toán.

## CHECKLIST CHO TVV

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Đã ghi `Lognote/Ghi chú` toàn bộ nội dung CSKH sau phiên làm việc |  |  |
| Cơ hội đủ điều kiện báo giá |  |  |
| `Báo giá/Quotation` đúng cơ hội và đúng khách hàng |  |  |
| Trạng thái là `Báo giá` |  |  |
| Khách hàng đúng |  |  |
| Email khách hàng đúng |  |  |
| Ngày sinh khách hàng đã có |  |  |
| Địa chỉ khách hàng đã có |  |  |
| Tab `Other Info` đã kiểm tra |  |  |
| Thông tin khách hàng cho chương trình định cư/du học đã đủ |  |  |
| Nhu cầu đúng theo bảng giá |  |  |
| Chương trình đúng theo bảng giá |  |  |
| Thị trường đúng theo bảng giá |  |  |
| Năm chương trình đúng |  |  |
| Trường `Bảng giá/Pricelist` đúng |  |  |
| Mã hợp đồng tự động đúng |  |  |
| Sản phẩm mở đúng theo bảng giá và đã chọn đủ |  |  |
| Nếu có voucher, đã dùng `Discount` và ghi note |  |  |
| Nếu có ưu đãi công ty, đã dùng `Promotion` |  |  |
| Điều kiện promotion đã hợp lệ |  |  |
| Related Contacts đã đúng nếu promotion theo nhóm khách hàng |  |  |
| Trạng thái là `Báo giá đã gửi` sau khi gửi email |  |  |
| Khách đã đồng ý trước khi Confirm |  |  |
| Trạng thái là `Đơn bán hàng` sau khi Confirm |  |  |
| Nếu khách đổi sản phẩm trước khi ký, đã quay lại Opportunity để cập nhật dữ liệu pipeline |  |  |
| Nếu khách đổi sản phẩm sau khi đã ký, đã tạo cơ hội mới và đơn hàng mới |  |  |
| Nếu đơn hàng cũ cần huỷ, đã báo kế toán xử lý |  |  |
| Nếu có thay đổi/cancel/chuyển điểm, đã ghi lognote |  |  |
| Đã hiểu KPI phụ thuộc hợp đồng và ngày đóng tiền |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Kiểm tra báo giá

Yêu cầu:

1. Mở một cơ hội đủ điều kiện báo giá.
2. Bấm `New Quotation` để tạo báo giá mới và mở màn hình `Báo giá/Đơn hàng`.
3. Nếu cơ hội đã có báo giá, bấm `View Quotation` để mở lại báo giá đã tạo.
4. Kiểm tra `Báo giá/Quotation` đúng cơ hội và đúng khách hàng.
5. Kiểm tra nhu cầu, chương trình, thị trường và năm chương trình.
6. Kiểm tra trường `Bảng giá/Pricelist` và mã hợp đồng.
7. Kiểm tra danh sách sản phẩm trong `Order Lines` đã mở đúng và chọn đủ.
8. Kiểm tra tab `Other Info`, phần `Thông tin khách hàng`.
9. Nếu sản phẩm khách muốn thay đổi trước khi ký, xác định cần quay lại Opportunity để cập nhật dữ liệu pipeline.

Kết quả cần đạt:

- Người dùng biết cách kiểm tra báo giá, trường `Bảng giá/Pricelist`, mã hợp đồng, sản phẩm và thông tin khách hàng phục vụ team Docs.
- Người dùng phân biệt được `New Quotation` là tạo báo giá mới, còn `View Quotation` là mở lại báo giá đã có.
- Người dùng hiểu nếu sản phẩm thay đổi trước khi ký thì xử lý lại từ Opportunity, không sửa tạm trên báo giá.

### Bài 2: Phân biệt Discount và Promotion

Yêu cầu:

1. Mở báo giá có voucher.
2. Dùng nút `Discount`.
3. `Add note` thông tin voucher.
4. Mở báo giá có ưu đãi sự kiện hoặc ưu đãi công ty.
5. Dùng nút `Promotion`.
6. Kiểm tra điều kiện promotion: sự kiện, nhu cầu, chương trình, thời hạn, check-in nếu có, và related contact nếu là ưu đãi theo nhóm.

Kết quả cần đạt:

- Người dùng biết voucher dùng `Discount`.
- Người dùng biết promotion công ty dùng `Promotion`.
- Người dùng không dùng `Discount` thay cho promotion của công ty.

### Bài 3: Gửi email báo giá

Yêu cầu:

1. Mở báo giá.
2. Kiểm tra email khách hàng.
3. Gửi email.
4. Nếu hệ thống báo thiếu email, bổ sung email.
5. Kiểm tra trạng thái `Báo giá đã gửi`.

Kết quả cần đạt:

- Người dùng biết cách gửi báo giá và xử lý lỗi thiếu email.

### Bài 4: Confirm đơn bán hàng

Yêu cầu:

1. Mở báo giá đã gửi.
2. Giả định khách đồng ý.
3. Chọn `Confirm`.
4. Nếu hệ thống báo thiếu ngày sinh, địa chỉ hoặc thông tin bắt buộc khác, bổ sung thông tin.
5. Confirm lại.
6. Kiểm tra trạng thái `Đơn bán hàng`.

Kết quả cần đạt:

- Người dùng biết cách chuyển báo giá sang đơn bán hàng.
- Người dùng biết xử lý lỗi thiếu ngày sinh, địa chỉ hoặc thông tin khách hàng phục vụ team Docs.

### Bài 5: Xử lý khách đổi sản phẩm sau khi đã ký

Yêu cầu:

1. Giả định khách đã ký nhưng muốn đổi sản phẩm/chương trình.
2. Tạo cơ hội mới cho nhu cầu/sản phẩm mới.
3. Tạo đơn hàng mới theo sản phẩm mới.
4. Ghi lognote lý do khách đổi sản phẩm và thông tin đơn hàng mới.
5. Báo kế toán xử lý huỷ toàn bộ đơn hàng cũ.

Kết quả cần đạt:

- Người dùng hiểu không tự sửa sản phẩm trên đơn hàng cũ.
- Người dùng biết tạo cơ hội mới, đơn hàng mới và báo kế toán xử lý đơn cũ.

### Bài 6: Nhận biết nguyên tắc KPI khi huỷ hoặc chuyển điểm

Yêu cầu:

1. Phân biệt đơn hàng huỷ hoàn tiền và huỷ không hoàn tiền.
2. Xác định ảnh hưởng KPI của từng trường hợp.
3. Xác định chuyển điểm trong cùng kỳ và khác kỳ.
4. Kiểm tra lognote nếu có bàn giao khách giữa các TVV.

Kết quả cần đạt:

- Người dùng biết huỷ hoàn tiền thì huỷ điểm, huỷ không hoàn tiền thì giữ điểm.
- Người dùng biết chỉ chuyển điểm trong cùng kỳ cho người phụ trách cuối.
- Người dùng biết khác kỳ thì không chuyển điểm.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Quotation and Sales Order Process |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / Sales |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
| Ngày phát hành |  |
