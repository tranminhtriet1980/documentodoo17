# TẠO LEAD MỚI VÀ ĐÁNH GIÁ QUALIFIED LEAD

## GIỚI THIỆU

### Mục tiêu

Tài liệu này hướng dẫn TVV cách nhận Lead mới để xử lý, tạo Lead mới hoàn toàn khi khách chưa có trên hệ thống, cập nhật đúng loại khách hàng sau khi liên hệ, nhập đầy đủ các trường bắt buộc và đánh giá chất lượng Lead trước khi chuyển thành cơ hội.

Mục tiêu chính là giúp Tư vấn viên ghi nhận đúng thông tin khách hàng, xác định đúng khả năng tư vấn và chỉ chuyển cơ hội đối với Lead đạt tiêu chí.

### Vị trí trong quy trình CRM

Quy trình này được thực hiện khi Lead mới đi vào hệ thống hoặc khi TVV cần chủ động tạo Lead mới cho khách hàng chưa có trên CRM.

Nếu TVV chủ động tạo Lead bằng tay, cần tìm số điện thoại trong `Lead`, `Cơ hội` và `Contact` trước khi tạo. Cách tìm kiếm và ghi nhận lognote được hướng dẫn chung trong tài liệu `Thao tác chung trên CRM`.

Sau mỗi phiên làm việc với khách hàng, TVV phải ghi lại toàn bộ nội dung CSKH bằng `Lognote/Ghi chú` trên CRM, bao gồm cuộc gọi, tin nhắn, Zalo, nội dung tư vấn, kết quả follow-up và bước xử lý tiếp theo. Lịch sử này sẽ tiếp tục đi theo khách hàng từ Lead sang cơ hội và đơn hàng, đồng thời là căn cứ chính thức để xác minh khi có vấn đề phát sinh.

```text
Lead đi vào CRM hoặc TVV tạo Lead mới
↓
Kiểm tra trùng
↓
Nhận Lead/Tạo Lead với tình trạng Mới
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

## NHẬN LEAD MỚI ĐỂ XỬ LÝ

### Loại khách hàng mặc định

Khi Lead mới đi vào hệ thống, `Loại khách hàng` mặc định là:

```text
Khách hàng
```

Đây chỉ là giá trị mặc định ban đầu. Sau khi Tư vấn viên liên hệ khách và xác minh thông tin, Tư vấn viên cần điều chỉnh lại loại khách hàng cho chính xác.

### Mở trang làm việc với Lead

TVV vào module `CRM`, chọn menu `Lead` để mở danh sách Lead cần xử lý.

Đối với user là TVV:

- TVV nhìn thấy Lead của chính mình.
- TVV nhìn thấy Lead của VP/chi nhánh được phân quyền.
- Nếu Lead có `Nhân viên kinh doanh` là VP chung, chưa phải tên nhân viên cụ thể, TVV cần lấy Lead về mình trước khi xử lý.

### Lấy Lead VP về xử lý

Khi danh sách Lead có các Lead thuộc VP chung:

1. Tích chọn các Lead muốn lấy về xử lý.
2. Chọn một ô đại diện trong cột `Nhân viên kinh doanh`.
3. Cập nhật `Nhân viên kinh doanh` thành tên TVV phụ trách.
4. Xác nhận lại thay đổi.
5. Mở Lead để tiếp tục liên hệ và xử lý.

Mục tiêu là đảm bảo Lead có người phụ trách rõ ràng trước khi chăm sóc khách hàng.

### Liên hệ khách hàng từ Lead

Sau khi mở Lead, TVV liên hệ khách hàng bằng các nút thao tác trên màn hình.

Các bước:

1. Kiểm tra số điện thoại và mã quốc gia.
2. Nếu gọi khách, chọn đúng nút `Gọi` theo số cần liên hệ.
3. Nếu khách có số Việt Nam, gọi đúng số có mã quốc gia VN.
4. Nếu khách có số Mỹ hoặc số quốc tế, gọi đúng số theo mã quốc gia tương ứng.
5. Nếu không liên hệ được qua cuộc gọi, có thể dùng nút `SMS` để gửi tin nhắn chờ tư vấn.
6. Ghi `Lognote/Ghi chú` kết quả liên hệ.

Lưu ý:

- Không gọi nhầm số Việt Nam/Mỹ nếu Lead có nhiều số điện thoại.
- Nếu khách không nghe máy, cần ghi nhận lịch sử và tạo activity follow-up nếu cần.

### Bắt buộc ghi Lognote sau mỗi phiên làm việc

Sau mỗi phiên làm việc với Lead, TVV bắt buộc ghi lại toàn bộ nội dung CSKH bằng `Lognote/Ghi chú` trên hệ thống.

Nội dung cần ghi gồm:

- Đã gọi số nào, khách có nghe máy hay không.
- Đã gửi SMS/Zalo hay chưa.
- Khách phản hồi nội dung gì.
- Nội dung tư vấn hoặc thông tin đã xác minh.
- Lý do hẹn liên hệ lại hoặc ngừng chăm sóc nếu có.
- Bước xử lý tiếp theo.

Lognote là lịch sử chính thức của khách hàng trên CRM. Nếu có tranh chấp, kiểm tra trùng, bàn giao khách hàng hoặc xác minh ai đang xử lý khách, hệ thống chỉ căn cứ vào nội dung đã ghi nhận trên CRM.

### Cập nhật thông tin sau khi liên hệ

Sau khi liên hệ hoặc xác minh thông tin, TVV cần:

1. Kiểm tra và cập nhật `Loại khách hàng`.
2. Cập nhật tên, giới tính, email nếu có.
3. Kiểm tra số điện thoại và mã quốc gia.
4. Cập nhật VP tư vấn, nhu cầu, thị trường, nguồn.
5. Cập nhật `Nhân viên kinh doanh`.
6. Cập nhật `Tình trạng lead`.
7. Cập nhật `Edupath Tags` nếu đã xác minh được.
8. Lưu Lead.

Nếu hệ thống báo trùng sau khi lưu hoặc Lead bị khóa, TVV xử lý theo phần `Xử lý Lead trùng hoặc Contact đã có` ở bên dưới.

### Quy định cập nhật tình trạng Lead

Sau khi gọi Lead, nhắn tin hoặc có bất kỳ thao tác chăm sóc khách hàng nào, TVV cần cập nhật đúng `Tình trạng lead` theo kết quả xử lý thực tế.

Đây là thông tin quan trọng để hệ thống automation đánh giá Lead và để quản lý kiểm tra lịch sử chăm sóc.

| Tình trạng lead | Khi nào sử dụng | Lưu ý thao tác |
|---|---|---|
| Mới | Trạng thái mặc định khi Lead mới vào hệ thống | Chỉ giữ `Mới` khi chưa có bất kỳ cuộc gọi, tin nhắn hoặc thông tin xử lý nào đến khách hàng |
| Liên hệ sau | Khách chưa nghe máy hoặc chưa phản hồi nhưng vẫn cần tiếp tục follow-up | Nếu gọi điện: tối thiểu 3 cuộc gọi vẫn không nghe máy thì giữ `Liên hệ sau`. Nếu khách dùng Zalo nhưng không nghe điện thoại: kết bạn Zalo và nhắn tối thiểu 3 tin, mỗi tin cách nhau 24 giờ, nếu chưa phản hồi thì giữ `Liên hệ sau` |
| Đã xác minh | TVV đã gặp được khách hàng hoặc đã trao đổi được với khách hàng để xác minh thông tin | Chỉ dùng khi đã có thông tin thực tế từ khách hàng, không chọn chỉ vì đã gọi hoặc nhắn tin |
| Ngừng chăm sóc | Không tiếp tục follow-up khách hàng nữa | Bắt buộc chọn thêm `Lý do mất` để hệ thống ghi nhận nguyên nhân ngừng chăm sóc |
| Close | Khách rác hoặc dữ liệu không hợp lệ | Dùng cho các trường hợp số điện thoại không đúng, không có tín hiệu, sai số hoặc dữ liệu rác |

Lưu ý:

- Mỗi lần gọi, nhắn tin, kết bạn Zalo hoặc trao đổi với khách cần ghi nhận lại bằng `Lognote/Ghi chú`.
- Không chuyển Lead sang `Đã xác minh` nếu chưa thực sự gặp hoặc trao đổi được với khách hàng.
- Không chuyển Lead sang `Ngừng chăm sóc` nếu vẫn còn kế hoạch follow-up.
- Nếu chọn `Ngừng chăm sóc`, phải chọn thêm `Lý do mất`.

## TẠO LEAD MỚI HOÀN TOÀN

### Khi nào tạo Lead mới hoàn toàn?

TVV tạo Lead mới hoàn toàn khi khách hàng chưa có dữ liệu phù hợp trên hệ thống và TVV chủ động tiếp nhận thông tin khách hàng.

Ví dụ:

- Khách gọi trực tiếp cho TVV.
- Khách nhắn tin riêng.
- Khách được giới thiệu trực tiếp.
- Khách chưa có Lead, Contact hoặc cơ hội phù hợp trên CRM.

### Kiểm tra trước khi tạo Lead mới

Trước khi tạo Lead mới hoàn toàn, TVV phải tìm kiếm trên hệ thống:

1. Tìm trong module `Lead`.
2. Tìm trong module `Cơ hội`.
3. Tìm trong module `Contact`.

Cách tìm kiếm theo số điện thoại, tên hoặc email được hướng dẫn trong tài liệu `Thao tác chung trên CRM`.

Nếu đã có Lead, Contact hoặc cơ hội phù hợp, không tạo mới hoàn toàn. TVV xử lý theo tình huống tương ứng.

### Các bước tạo Lead mới hoàn toàn

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Chọn `Mới`.
4. Nếu khách hàng chưa có trên hệ thống, nhập thông tin tại trường `Tên liên hệ`.
5. Nhập số điện thoại và mã quốc gia.
6. Nhập nhu cầu, thị trường, VP tư vấn, nguồn và nhân viên kinh doanh.
7. Kiểm tra `Loại khách hàng` mặc định là `Khách hàng`.
8. Lưu Lead.
9. Liên hệ khách bằng nút `Gọi` hoặc `SMS`.
10. Cập nhật thông tin sau khi liên hệ theo các bước xử lý Lead mới.

Nếu sau khi lưu bị báo trùng, TVV không tạo lại nhiều lần. TVV kiểm tra Contact đã có trên hệ thống chưa hoặc báo CRM Admin xử lý.

## XỬ LÝ LEAD TRÙNG HOẶC CONTACT ĐÃ CÓ

### Tạo Lead từ Contact đã tồn tại

Mục này áp dụng cho trường hợp khách hàng phát sinh nhu cầu mới nhưng số điện thoại đã có trong module `Contact`.

Thông thường, khi chuyển cơ hội, hệ thống sẽ chuyển Lead thành `Contact` và `Cơ hội`.

Khi khách hàng đã có Contact nhưng cần tạo Lead để xử lý lại theo quy trình, TVV không tạo khách hàng mới hoàn toàn. TVV phải chọn Contact đã có tại trường `Tên khách hàng`.

Trong file tạo Lead này chỉ cần ghi nhớ:

- Nếu Contact đã tồn tại, tạo Lead bằng trường `Tên khách hàng`.
- Không nhập khách vào trường `Tên liên hệ` như một khách hàng mới hoàn toàn nếu Contact đã tồn tại.
- Nếu mục tiêu là tạo cơ hội mới trực tiếp từ Contact, xem quy trình chi tiết trong tài liệu `Quản lý Pipeline cơ hội`.

Mục tiêu là tạo Lead hợp lệ có liên kết với Contact đã tồn tại, tránh bị hệ thống báo trùng và khóa Lead.

Khi đó có thể xảy ra tình huống:

```text
Khách phát sinh nhu cầu mới
↓
Contact đã tồn tại trên hệ thống
↓
Nếu tạo Lead mới hoàn toàn bằng cùng số điện thoại
↓
Hệ thống báo trùng và khóa Lead
```

### Hai hướng xử lý

#### Trường hợp 1: Lead từ hệ thống hoặc import tự động

Người dùng thường khó biết trước Lead có bị trùng với Contact trống hay không.

Nếu Lead được cập nhật từ hệ thống hoặc import tự động và bị trùng với Contact đã có, hệ thống sẽ khóa Lead. Người dùng thông thường có thể không nhìn thấy Lead đó.

Hướng xử lý:

1. Không tạo lại Lead nhiều lần với cùng số điện thoại.
2. Ghi nhận thông tin khách hàng vừa nhập hoặc vừa nhận từ nguồn.
3. Báo CRM Admin kiểm tra.
4. Admin kiểm tra Contact/Lead bị trùng và xử lý theo quyền quản trị.

#### Trường hợp 2: TVV chủ động tạo Lead khi khách liên hệ trực tiếp

Khi khách liên hệ trực tiếp và Tư vấn viên là người chủ động tạo Lead, trước khi tạo mới cần kiểm tra trên cả module `Lead` và `Contact`.

Khuyến nghị kiểm tra thêm module `Cơ hội` để biết khách đã có cơ hội đang được xử lý hay chưa.

Nếu số điện thoại đã có trong module `Lead`:

1. Không tạo Lead mới.
2. Báo CRM Admin kiểm tra.
3. Nhờ Admin chuyển Lead về đúng người phụ trách nếu phù hợp.

Nếu số điện thoại đã có trong module `Contact`:

1. Vào màn hình tạo Lead mới.
2. Tại trường `Tên khách hàng`, chọn mục `Tìm kiếm thêm`.
3. Dán số điện thoại khách hàng vào ô tìm kiếm.
4. Chọn đúng khách hàng/Contact đã có trên hệ thống.
5. Tiếp tục nhập các thông tin còn thiếu của Lead.
6. Lưu Lead.

Khi chọn đúng Contact ở trường `Tên khách hàng`, Lead mới sẽ được tạo hợp lệ và liên kết với khách hàng đã có trên hệ thống.

### Phân biệt `Tên liên hệ` và `Tên khách hàng`

Đây là điểm quan trọng khi tạo Lead:

| Trường | Khi nào sử dụng | Ý nghĩa |
|---|---|---|
| Tên liên hệ | Khi tạo Lead mới hoàn toàn | Tạo thông tin liên hệ mới chưa có trên hệ thống |
| Tên khách hàng | Khi khách hàng/Contact đã có trên hệ thống | Chọn khách hàng đã tồn tại để tạo Lead hợp lệ |

Lưu ý:

- Nếu khách hàng đã có trong `Contact`, ưu tiên chọn tại trường `Tên khách hàng`.
- Nếu nhập vào `Tên liên hệ` như một khách hàng mới trong khi số điện thoại đã tồn tại, hệ thống có thể báo trùng và khóa Lead.
- Nếu không chắc khách đã có trên hệ thống hay chưa, cần tìm kiếm theo số điện thoại trong cả `Lead` và `Contact` trước khi tạo mới.

### Vì sao cần cập nhật loại khách hàng?

Mỗi loại khách hàng có cách nhập liệu khác nhau. Nếu chọn sai loại khách hàng, thông tin lưu trên CRM sẽ không đúng với thực tế và có thể ảnh hưởng đến quá trình tư vấn, chăm sóc và báo cáo.

Ví dụ:

- Người trực tiếp có nhu cầu du học/ định cư/ dịch vụ là `Khách hàng`.
- Phụ huynh hoặc người liên hệ thay cho học sinh/ khách hàng là `Người đại diện`.
- Đơn vị hoặc cá nhân (agent) giới thiệu khách hàng là `Đối tác`.

## CÁC LOẠI KHÁCH HÀNG

### 1. Loại khách hàng: Khách hàng

Sử dụng khi người đang được nhập trên Lead là khách hàng chính hoặc người có nhu cầu trực tiếp.

Thông tin cần nhập:

| Trường thông tin | Ghi chú |
|---|---|
| Tên liên hệ | Họ tên khách hàng chính |
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

Sau khi liên hệ khách hàng, Tư vấn viên cần cập nhật đúng `Tình trạng lead`. Nếu Lead thuộc tình trạng `Ngừng chăm sóc`, Tư vấn viên cần chọn thêm `Lý do mất`.

Dựa trên `Tình trạng lead` và `Lý do mất`, hệ thống automation sẽ tự động đánh giá Lead thuộc nhóm `New`, `Not Qualified` hoặc `Qualified`.

Người dùng không cần tự phân loại thủ công `New / Not Qualified / Qualified` khi hệ thống đã cấu hình automation.

### Dữ liệu dùng cho automation

| Dữ liệu | Người cập nhật | Mục đích |
|---|---|---|
| Tình trạng lead | Tư vấn viên | Xác định tình trạng xử lý thực tế của Lead |
| Lý do mất | Tư vấn viên | Bắt buộc khi Lead thuộc tình trạng `Ngừng chăm sóc` |
| Edupath Tag | Tư vấn viên | Đánh giá chất lượng Lead và tính điểm sao |

### Kết quả automation

| Trạng thái Qualified Lead | Ý nghĩa |
|---|---|
| New | Lead mới, chưa xử lý hoặc vẫn ở tình trạng mới |
| Not Qualified | Liên hệ sau/ Close/ Ngừng chăm sóc (Lead không đủ điều kiện tiếp tục tư vấn theo tình trạng hoặc lý do mất) |
| Qualified | Đã xác minh/ Ngừng chăm sóc kèm lý do mất phù hợp hoặc đã xử lý đủ thông tin để đánh giá tiếp |

## QUY TẮC PHÂN LOẠI LEAD

### 1. New

`New` là kết quả automation khi Lead mới đi vào hệ thống và `Tình trạng lead` vẫn là mới.

Áp dụng khi:

- Lead vừa được tạo.
- Chưa liên hệ khách hàng.
- Chưa cập nhật tình trạng xử lý khác.

### 2. Not Qualified

`Not Qualified` là kết quả automation khi `Tình trạng lead` hoặc `Lý do mất` cho thấy Lead không đủ điều kiện tiếp tục xử lý theo quy trình tư vấn.

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

- Nếu `Tình trạng lead` là `Ngừng chăm sóc`, người dùng cần chọn `Lý do mất`.
- Automation sẽ dựa vào lý do này để phân loại Lead.

### 3. Qualified

`Qualified` là kết quả automation khi Lead đã được xác minh hoặc đã xử lý đủ thông tin để tiếp tục đánh giá.

Các trường hợp có thể thuộc nhóm Qualified:

- Đã xác minh.
- Ngừng chăm sóc sau khi đã gặp hoặc tư vấn khách hàng nhưng không tiếp tục vì lý do cụ thể.

Các lý do `Ngừng chăm sóc` nhưng vẫn thuộc nhóm Qualified có thể gồm:

- Tài chính không phù hợp.
- Đã tư vấn không phản hồi.
- Không phù hợp điều kiện.
- Thời gian chưa phù hợp.
- Lý lịch tư pháp.
- Mục tiêu du học khác.
- Không phù hợp độ tuổi.
- Xuất khẩu lao động.
- Năng lực đảng viên.
- Tìm hiểu cho biết.

## ĐÁNH GIÁ ĐIỂM QUALIFIED VÀ CHUYỂN CƠ HỘI

### Mục tiêu

Điểm Qualified giúp xác định Lead có đủ chất lượng để chuyển thành cơ hội hay chưa.

Hệ thống dựa trên `Edupath Tag` để đánh giá số sao. Tiêu chí chuyển cơ hội phụ thuộc chính xác vào số sao và tình trạng xác minh của Lead.

Khi Lead đủ điều kiện, hệ thống automation sẽ tự động hiển thị pop-up chuyển cơ hội. Đây vẫn là thao tác mở để TVV nhập thông tin cơ hội trước khi tạo cơ hội chính thức.

### Quy tắc chấm sao

| Mức sao | Điều kiện Edupath Tag | Ý nghĩa |
|---|---|---|
| 0 sao | Chỉ có `Mục tiêu` hoặc `Thời điểm` | Lead có thông tin ban đầu nhưng chưa đủ mạnh |
| 1 sao | Có `Tài chính` hoặc `Năng lực hồ sơ` | Lead có một tiêu chí quan trọng |
| 2 sao | Có cả `Tài chính` và `Năng lực hồ sơ` | Lead đủ điều kiện tốt để xem xét chuyển cơ hội |
| 3 sao | Có đủ 4 tiêu chí: `Tài chính`, `Năng lực hồ sơ`, `Thời điểm`, `Mục tiêu` | Lead có chất lượng cao |

### Điều kiện hiện pop-up thông tin cơ hội

Pop-up chuyển cơ hội chỉ hiển thị khi Lead thỏa cả hai điều kiện:

1. `Tình trạng lead` là `Đã xác minh`.
2. Mức sao đạt tối thiểu `2 sao`.

Mức `2 sao` là điều kiện đủ tối thiểu vì Lead đã có cả hai tag quan trọng:

- `Tài chính`.
- `Năng lực hồ sơ`.

Mức `3 sao` là đủ điều kiện lý tưởng chuyển cơ hội vì đã có đủ 4 tiêu chí ra đơn hàng.

Nếu Lead không đúng tình trạng hoặc chưa đạt đủ 2 sao, hệ thống sẽ không cho chuyển cơ hội.

### Thao tác khi pop-up chuyển cơ hội hiển thị

Khi pop-up `Convert to Opportunity` hiển thị, TVV cần nhập đầy đủ thông tin trên pop-up trước khi chọn tạo cơ hội.

Các thông tin cần kiểm tra và nhập gồm:

| Trường trên pop-up | Ghi chú |
|---|---|
| Nhân viên kinh doanh | Người phụ trách cơ hội |
| Đội ngũ kinh doanh | Team xử lý cơ hội |
| Nhu cầu thực tế | Nhu cầu đã xác minh sau tư vấn |
| Chương trình tư vấn | Chương trình hoặc dịch vụ tư vấn phù hợp theo bảng giá |
| Năm chương trình | Năm kinh doanh thực tế theo năm học của công ty |
| Ngày chốt dự kiến | Thời điểm dự kiến chốt cơ hội |
| Customer | Chọn tạo khách hàng mới hoặc liên kết khách hàng theo tình huống |

Sau khi nhập đầy đủ thông tin, TVV chọn `Tạo cơ hội` để hoàn tất chuyển Lead sang cơ hội.

Lưu ý về `Năm chương trình`:

- `Năm chương trình` được tính theo năm kinh doanh của công ty, không chỉ theo năm dương lịch.
- Ví dụ giai đoạn `09/2025 - 08/2026` được ghi nhận là `Năm chương trình` `2026`.
- Người dùng cần chọn đúng năm chương trình vì thông tin này sẽ đi theo cơ hội, báo giá và báo cáo kinh doanh.

Lưu ý về `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`:

- Ba thông tin này cần khớp với bảng giá sản phẩm.
- Nếu chọn sai, khi tạo báo giá hệ thống có thể không tìm thấy đơn giá sản phẩm.
- Nếu không chắc chương trình hoặc thị trường, TVV cần kiểm tra lại trước khi tạo cơ hội hoặc báo giá.

### Trường hợp TVV tắt pop-up

Theo nguyên tắc vận hành, khi Lead đã đủ điều kiện chuyển cơ hội thì TVV không nên tắt pop-up.

Nếu TVV tắt pop-up và chưa chuyển cơ hội, hệ thống vẫn ghi nhận Lead đang đủ điều kiện chuyển cơ hội. Khi TVV mở lại Lead để xử lý tiếp, pop-up sẽ tiếp tục hiển thị để nhắc người dùng chuyển cơ hội.

Mục tiêu là tránh tình trạng Lead đã đủ điều kiện nhưng vẫn bị giữ lại ở bước Lead và không được chuyển sang cơ hội.

### Trường hợp hệ thống báo lỗi thiếu thông tin chuyển cơ hội

Nếu người dùng bấm nút `Convert to Opportunity` thủ công nhưng Lead chưa đủ điều kiện 2 sao, hệ thống sẽ hiển thị bảng lỗi thiếu thông tin chuyển cơ hội.

Người dùng cần kiểm tra lại:

| Nội dung cần kiểm tra | Cách xử lý |
|---|---|
| Tình trạng lead chưa phải `Đã xác minh` | Cập nhật lại tình trạng đúng theo kết quả liên hệ |
| Lead chưa đạt 2 sao | Kiểm tra lại Edupath Tag |
| Thiếu tag `Tài chính` | Xác minh lại khả năng tài chính của khách và cập nhật tag nếu đúng |
| Thiếu tag `Năng lực hồ sơ` | Xác minh lại điều kiện hoặc hồ sơ của khách và cập nhật tag nếu đúng |

Sau khi cập nhật đúng thông tin, nếu Lead đạt điều kiện, hệ thống sẽ tự động hiện pop-up chuyển cơ hội.

## CÁC BƯỚC THỰC HIỆN TRÊN ODOO

### Bước 1: Nhận Lead mới để xử lý

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Mở danh sách Lead cần xử lý.
4. Kiểm tra Lead đang thuộc `Nhân viên kinh doanh` nào.
5. Nếu Lead đang thuộc VP hoặc nhóm chung, tích chọn Lead cần lấy.
6. Cập nhật `Nhân viên kinh doanh` thành tên TVV phụ trách.
7. Lưu thay đổi.
8. Mở Lead để xử lý.

### Bước 2: Liên hệ khách hàng trên Lead

1. Kiểm tra số điện thoại và mã quốc gia.
2. Nếu gọi khách, chọn đúng nút `Gọi` theo số cần liên hệ.
3. Nếu khách có số Việt Nam, gọi đúng số VN.
4. Nếu khách có số Mỹ hoặc số quốc tế, gọi đúng số theo mã quốc gia tương ứng.
5. Nếu không liên hệ được, có thể dùng nút `SMS` để gửi tin nhắn chờ tư vấn.
6. Ghi `Lognote/Ghi chú` kết quả liên hệ.

### Bước 3: Cập nhật và lưu Lead sau khi liên hệ

1. Xác minh khách là khách hàng chính, người đại diện hay đối tác.
2. Cập nhật `Loại khách hàng` nếu cần.
3. Cập nhật thông tin khách hàng còn thiếu.
4. Cập nhật VP tư vấn, nhu cầu, thị trường, nguồn.
5. Cập nhật `Tình trạng lead`.
6. Cập nhật `Edupath Tags` nếu đã xác minh được.
7. Lưu Lead.
8. Nếu Lead bị báo trùng hoặc bị khóa, xử lý theo phần `Xử lý Lead trùng hoặc Contact đã có`.

### Bước 4: Tạo Lead mới hoàn toàn nếu khách chưa có trên hệ thống

1. Kiểm tra trước trong module `Lead`, `Cơ hội` và `Contact`.
2. Nếu đã có Lead phù hợp, không tạo mới và báo CRM Admin nếu cần chuyển phụ trách.
3. Nếu đã có Contact phù hợp, không tạo Lead mới hoàn toàn; xử lý theo Bước 5.
4. Nếu chưa có Lead, Cơ hội và Contact phù hợp, tạo Lead mới bằng trường `Tên liên hệ`.
5. Sau khi tạo, lặp lại các bước liên hệ, cập nhật thông tin và lưu Lead như quy trình nhận Lead mới.

### Bước 5: Tạo Lead từ Contact đã có

1. Vào module `CRM`.
2. Chọn menu `Lead`.
3. Chọn `Mới`.
4. Tại trường `Tên khách hàng`, chọn `Tìm kiếm thêm`.
5. Tìm đúng Contact khách hàng đã có trên hệ thống.
6. Chọn Contact đó.
7. Nhập các thông tin còn thiếu của Lead.
8. Lưu Lead.
9. Nếu vẫn lỗi hoặc bị khóa trùng, báo CRM Admin kiểm tra.

### Bước 6: Cập nhật loại khách hàng

1. Tại trường `Loại khách hàng`, kiểm tra giá trị hiện tại.
2. Nếu đúng là khách hàng chính, giữ `Khách hàng`.
3. Nếu là phụ huynh hoặc người liên hệ thay, đổi thành `Người đại diện`.
4. Nếu là đơn vị hoặc người giới thiệu, đổi thành `Đối tác`.
5. Nhập các trường thông tin tương ứng với từng loại khách hàng.

### Bước 7: Cập nhật trường bắt buộc

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

### Bước 8: Đánh giá Qualified Lead

1. Cập nhật `Tình trạng lead` theo kết quả liên hệ thực tế.
2. Nếu chọn tình trạng `Ngừng chăm sóc`, chọn thêm `Lý do mất`.
3. Cập nhật Edupath Tag theo kết quả tư vấn.
4. Lưu thông tin Lead.
5. Hệ thống automation tự động đánh giá Lead là `New`, `Not Qualified` hoặc `Qualified`.
6. Kiểm tra mức sao của Lead.

### Bước 9: Chuyển cơ hội nếu đủ điều kiện

1. Kiểm tra `Tình trạng lead` là `Đã xác minh`.
2. Kiểm tra Lead đạt tối thiểu `2 sao`.
3. Chờ hệ thống tự động hiển thị pop-up chuyển cơ hội.
4. Khi pop-up hiển thị, nhập đầy đủ thông tin trên pop-up.
5. Chọn `Tạo cơ hội`.
6. Nếu TVV tắt pop-up khi chưa tạo cơ hội, lần mở Lead tiếp theo pop-up sẽ tiếp tục hiển thị.
7. Nếu bấm `Convert to Opportunity` thủ công nhưng chưa đủ 2 sao, đọc bảng lỗi và cập nhật tag `Tài chính` hoặc `Năng lực hồ sơ` còn thiếu.

## KẾT QUẢ MONG ĐỢI

Sau khi thực hiện đúng quy trình:

- Lead mới có loại khách hàng mặc định là `Khách hàng`.
- TVV biết mở danh sách Lead được phân quyền để nhận Lead mới.
- TVV biết lấy Lead VP/nhóm chung về mình trước khi xử lý.
- TVV biết sử dụng nút `Gọi` và chọn đúng số điện thoại theo mã quốc gia VN, US hoặc quốc gia tương ứng.
- TVV biết sử dụng nút `SMS` để gửi tin nhắn chờ tư vấn khi chưa liên hệ được khách hàng.
- TVV biết cập nhật và lưu lại thông tin sau khi liên hệ khách hàng.
- TVV kiểm tra được khách hàng đã có trong `Lead`, `Cơ hội` hoặc `Contact` trước khi tạo mới.
- Nếu khách hàng chưa có trên hệ thống, Lead mới được tạo bằng trường `Tên liên hệ`.
- Nếu Contact đã tồn tại, Lead mới được liên kết đúng tại trường `Tên khách hàng`.
- Tư vấn viên cập nhật đúng loại khách hàng sau khi xác minh.
- Các trường bắt buộc được nhập đầy đủ.
- Tư vấn viên cập nhật đúng `Tình trạng lead` và `Lý do mất` nếu có.
- Hệ thống automation tự động đánh giá Lead đúng `New`, `Not Qualified` hoặc `Qualified`.
- Edupath Tag phản ánh đúng chất lượng Lead.
- Lead có `Tình trạng lead` là `Đã xác minh` và đạt tối thiểu 2 sao sẽ tự động hiển thị pop-up chuyển cơ hội.
- TVV nhập đầy đủ thông tin trong pop-up trước khi tạo cơ hội.
- Nếu TVV tắt pop-up khi chưa chuyển cơ hội, pop-up sẽ tiếp tục hiển thị khi mở lại Lead.
- Lead chưa đủ 2 sao sẽ hiển thị bảng lỗi để người dùng cập nhật tag `Tài chính` hoặc `Năng lực hồ sơ`.
- Chỉ Lead đủ tiêu chí mới được chuyển thành cơ hội.

## LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Tạo Lead mới nhưng bị báo trùng với Contact | Khách hàng đã có Contact trên hệ thống nhưng người dùng nhập vào `Tên liên hệ` như Lead mới hoàn toàn | Tìm Contact theo số điện thoại và chọn khách tại trường `Tên khách hàng` |
| Không tạo được Lead từ Contact trống | Contact được import từ hệ thống cũ nhưng chưa từng có cơ hội | Chọn Contact tại trường `Tên khách hàng`, nếu vẫn lỗi thì báo CRM Admin |
| Khách đã có Lead nhưng TVV vẫn tạo thêm Lead mới | Chưa kiểm tra module Lead trước khi tạo | Tìm theo số điện thoại trong Lead, nếu đã có thì báo Admin chuyển về đúng người phụ trách |
| Không đổi loại khách hàng sau khi liên hệ | TVV giữ mặc định `Khách hàng` | Xác minh lại vai trò người liên hệ và cập nhật đúng loại |
| Thiếu mã quốc gia khi nhập số điện thoại | Nhập số điện thoại chưa đủ format | Bổ sung mã quốc gia như VN, US |
| Không chấm đúng sao | Chọn thiếu hoặc sai Edupath Tag | Kiểm tra lại 4 tag: Tài chính, Năng lực hồ sơ, Thời điểm, Mục tiêu |
| Không hiện pop-up chuyển cơ hội | Chưa đúng tình trạng `Đã xác minh` hoặc chưa đạt 2 sao | Cập nhật lại tình trạng lead và Edupath Tag |
| TVV tắt pop-up chuyển cơ hội | Lead đã đủ điều kiện nhưng người dùng chưa tạo cơ hội | Mở lại Lead, pop-up sẽ tiếp tục hiển thị và cần nhập thông tin để tạo cơ hội |
| Hệ thống báo lỗi thiếu thông tin chuyển cơ hội | Lead chưa đủ tag `Tài chính` hoặc `Năng lực hồ sơ` | Cập nhật đúng tag còn thiếu nếu đã xác minh được |
| Chuyển cơ hội khi Lead chưa đủ điều kiện | Chưa xác minh hoặc chưa đủ 2 sao | Không chuyển cơ hội, tiếp tục tư vấn hoặc cập nhật tag còn thiếu |
| Ngừng chăm sóc nhưng không có lý do mất | Người dùng quên chọn lý do mất | Cập nhật `Lý do mất` để automation phân loại đúng |
| Automation phân loại không đúng | Tình trạng lead hoặc lý do mất chưa đúng | Kiểm tra lại `Tình trạng lead`, `Lý do mất` và báo CRM Admin nếu vẫn sai |

## CHECKLIST CHO TVV

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Đã mở đúng danh sách Lead được phân quyền |  |  |
| Nếu Lead thuộc VP/nhóm chung, đã lấy Lead về đúng `Nhân viên kinh doanh` |  |  |
| Đã mở Lead cần xử lý |  |  |
| Đã kiểm tra số điện thoại và mã quốc gia trước khi gọi |  |  |
| Đã chọn đúng số VN, US hoặc số quốc tế khi bấm `Gọi` |  |  |
| Nếu chưa liên hệ được, đã gửi `SMS` nếu cần |  |  |
| Đã ghi `Lognote/Ghi chú` kết quả liên hệ |  |  |
| Đã ghi đủ toàn bộ nội dung CSKH sau phiên làm việc |  |  |
| Đã kiểm tra số điện thoại trong module Lead |  |  |
| Đã kiểm tra số điện thoại trong module Cơ hội |  |  |
| Đã kiểm tra số điện thoại trong module Contact |  |  |
| Nếu chưa có Contact, đã nhập tại trường `Tên liên hệ` |  |  |
| Nếu có Contact, đã chọn tại trường `Tên khách hàng` |  |  |
| Lead không bị trùng |  |  |
| Tình trạng ban đầu là Mới |  |  |
| Đã lưu lại thông tin sau khi cập nhật |  |  |
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
| Nếu đủ 2 sao, đã kiểm tra pop-up chuyển cơ hội |  |  |
| Đã nhập nhân viên kinh doanh trong pop-up |  |  |
| Đã nhập đội ngũ kinh doanh trong pop-up |  |  |
| Đã nhập nhu cầu thực tế trong pop-up |  |  |
| Đã nhập chương trình tư vấn trong pop-up |  |  |
| Đã nhập năm chương trình trong pop-up |  |  |
| Đã nhập ngày chốt dự kiến trong pop-up |  |  |
| Đã chuyển cơ hội nếu đủ điều kiện |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Nhận Lead VP về xử lý

Yêu cầu:

1. Vào module `CRM`.
2. Mở menu `Lead`.
3. Tìm Lead có `Nhân viên kinh doanh` là VP hoặc nhóm chung.
4. Tích chọn Lead muốn lấy về xử lý.
5. Chọn một ô đại diện trong cột `Nhân viên kinh doanh`.
6. Cập nhật thành tên TVV phụ trách.
7. Lưu lại thay đổi.

Kết quả cần đạt:

- Lead có người phụ trách rõ ràng.
- TVV biết cách nhận Lead VP/nhóm chung về mình trước khi chăm sóc.

### Bài 2: Liên hệ khách hàng từ Lead

Yêu cầu:

1. Mở Lead đã được phân công.
2. Kiểm tra số điện thoại và mã quốc gia.
3. Nếu khách có nhiều số, xác định đúng số VN, US hoặc số quốc tế cần gọi.
4. Bấm `Gọi` để liên hệ khách hàng.
5. Nếu khách chưa nghe máy, dùng `SMS` để gửi tin nhắn chờ tư vấn nếu phù hợp.
6. Ghi `Lognote/Ghi chú` kết quả liên hệ.
7. Cập nhật thông tin Lead sau khi liên hệ và lưu lại.

Kết quả cần đạt:

- TVV biết gọi đúng số theo mã quốc gia.
- TVV biết dùng SMS trong trường hợp chưa liên hệ được.
- Lịch sử chăm sóc được ghi nhận trên CRM.

### Bài 3: Tạo Lead mới hoàn toàn

Yêu cầu:

1. Kiểm tra số điện thoại trong module `Lead`.
2. Kiểm tra số điện thoại trong module `Cơ hội`.
3. Kiểm tra số điện thoại trong module `Contact`.
4. Nếu chưa có dữ liệu phù hợp trên hệ thống, tạo một Lead mới bằng trường `Tên liên hệ`.
5. Kiểm tra `Loại khách hàng` mặc định là `Khách hàng`.
6. Nhập các trường bắt buộc.
7. Lưu Lead.
8. Kiểm tra tình trạng Lead là `Mới`.
9. Thực hiện lại các bước liên hệ và cập nhật thông tin như bài xử lý Lead mới.

Kết quả cần đạt:

- Lead được tạo thành công khi khách hàng chưa có trên hệ thống.
- Người dùng biết chỉ dùng `Tên liên hệ` khi tạo khách hàng mới hoàn toàn.
- Loại khách hàng mặc định là `Khách hàng`.
- Các trường bắt buộc được nhập đầy đủ.

### Bài 4: Tạo Lead từ Contact đã tồn tại

Yêu cầu:

1. Tìm số điện thoại khách hàng trong module `Contact`.
2. Xác nhận khách hàng đã có Contact trên hệ thống.
3. Vào màn hình tạo Lead mới.
4. Tại trường `Tên khách hàng`, chọn `Tìm kiếm thêm`.
5. Dán số điện thoại khách hàng vào ô tìm kiếm.
6. Chọn đúng Contact của khách hàng.
7. Nhập các thông tin còn thiếu của Lead.
8. Lưu Lead.

Kết quả cần đạt:

- Lead mới được tạo hợp lệ từ Contact đã tồn tại.
- Người dùng không nhập khách hàng đã có vào trường `Tên liên hệ`.
- Lead không bị khóa do tạo trùng Contact.

### Bài 5: Cập nhật loại khách hàng thành Người đại diện

Yêu cầu:

1. Mở Lead đã tạo.
2. Giả định người liên hệ là phụ huynh.
3. Đổi `Loại khách hàng` thành `Người đại diện`.
4. Nhập `Mối quan hệ`.
5. Nhập họ tên và số điện thoại người đại diện.

Kết quả cần đạt:

- CRM ghi nhận đúng người liên hệ là `Người đại diện`.
- Thông tin không bị nhầm với khách hàng chính.

### Bài 6: Đánh giá Edupath Tag và điểm sao

Yêu cầu:

1. Mở Lead đã xác minh.
2. Chọn Edupath Tag theo tình huống giảng viên đưa ra.
3. Kiểm tra mức sao.
4. Xác định Lead có đủ điều kiện chuyển cơ hội hay chưa.

Kết quả cần đạt:

- Người dùng hiểu cách chọn tag.
- Người dùng xác định đúng mức 0 sao, 1 sao, 2 sao hoặc 3 sao.

### Bài 7: Xử lý pop-up chuyển cơ hội

Yêu cầu:

1. Mở Lead đã có `Tình trạng lead` là `Đã xác minh`.
2. Chọn Edupath Tag để Lead đạt tối thiểu 2 sao.
3. Lưu Lead.
4. Kiểm tra pop-up chuyển cơ hội tự động hiển thị.
5. Nhập đầy đủ thông tin trong pop-up.
6. Chọn `Tạo cơ hội`.

Kết quả cần đạt:

- Người dùng hiểu pop-up tự hiện khi Lead đủ điều kiện.
- Người dùng biết phải nhập đầy đủ thông tin trong pop-up trước khi tạo cơ hội.
- Người dùng không tắt pop-up khi Lead đã đủ điều kiện chuyển cơ hội.

### Bài 8: Bấm Convert khi chưa đủ 2 sao

Yêu cầu:

1. Mở một Lead chưa có đủ tag `Tài chính` và `Năng lực hồ sơ`.
2. Bấm nút `Convert to Opportunity`.
3. Đọc bảng lỗi hệ thống hiển thị.
4. Xác định Lead đang thiếu tag nào.
5. Cập nhật lại tag nếu đã xác minh được thông tin.

Kết quả cần đạt:

- Người dùng hiểu Lead chưa đủ 2 sao thì không được chuyển cơ hội.
- Người dùng biết lỗi thường liên quan đến thiếu `Tài chính` hoặc `Năng lực hồ sơ`.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Create Lead and Qualified Lead |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / CRM / Lead Management |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
| Ngày phát hành |  |
