# THAO TÁC CHUNG TRÊN CRM: TÌM KIẾM, LOGNOTE, ACTIVITY VÀ THU HỒI TỰ ĐỘNG

## MỤC TIÊU

Tài liệu này hướng dẫn các thao tác dùng chung trên CRM mà TVV cần nắm trước khi xử lý Lead, Cơ hội hoặc Đơn hàng.

Phạm vi gồm 4 nhóm thao tác/quy định:

- Tìm kiếm khách hàng, Lead và Cơ hội trên CRM.
- Ghi nhận `Lognote/Ghi chú` để lưu lịch sử chăm sóc khách hàng.
- Tạo và theo dõi `Activity/Việc cần làm` để giao việc nội bộ.
- Hiểu automation thu hồi Lead/Cơ hội không xử lý đúng hạn.

Đây là các kỹ năng nền tảng, dùng xuyên suốt từ:

```text
Lead
↓
Cơ hội
↓
Đơn hàng
```

## PHẦN 1: TÌM KIẾM KHÁCH HÀNG, LEAD VÀ CƠ HỘI

### Khi nào cần tìm kiếm

TVV cần tìm kiếm trên CRM trong các trường hợp:

- Tìm khách hàng để chăm sóc tiếp.
- Tìm Lead được phân công xử lý.
- Mở lại cơ hội để cập nhật giai đoạn pipeline.
- Kiểm tra khách đã có Contact trên hệ thống chưa.
- Kiểm tra dữ liệu trước khi tạo Lead mới.
- Kiểm tra trường hợp có khả năng trùng dữ liệu.

Tìm kiếm không chỉ dùng để kiểm tra trùng. Đây là thao tác hằng ngày để mở đúng hồ sơ cần xử lý.

### Nguyên tắc chọn đúng trường tìm kiếm

Khi nhập nội dung vào ô tìm kiếm, hệ thống sẽ gợi ý nhiều trường có thể tìm được.

Ví dụ:

- `Tên`.
- `Email`.
- `Điện thoại/di động`.
- `Nhân viên kinh doanh`.
- `Công ty liên quan`.
- `Thẻ`.

TVV phải chọn đúng trường theo nội dung đang tìm.

| Nội dung đang có | Trường nên chọn |
|---|---|
| Số điện thoại | `Điện thoại/di động` |
| Tên khách hàng | `Tên` hoặc trường tên tương ứng của màn hình |
| Email | `Email` |
| Tên nhân viên phụ trách | `Nhân viên kinh doanh` |
| Tên công ty/đối tác liên quan | `Công ty liên quan` nếu có |

Lưu ý:

- Nhập số điện thoại nhưng chọn tìm theo `Tên` thì hệ thống có thể không ra kết quả.
- Nhập email nhưng chọn tìm theo `Điện thoại/di động` thì hệ thống có thể không ra kết quả.
- Nhập tên khách nhưng chọn sai trường thì kết quả có thể thiếu hoặc không đúng.

### Tìm theo số điện thoại

Số điện thoại là dữ liệu chính để nhận diện khách hàng trên CRM.

Cùng một số điện thoại có thể được nhập theo nhiều cách khác nhau:

```text
0345334928
+84 345 334 928
84 345 334 928
345334928
```

Với số Việt Nam, ưu tiên tìm bằng phần số chính:

- Bỏ số `0` đầu nếu có.
- Bỏ `+84` nếu có.
- Bỏ `84` đầu nếu có.
- Bỏ dấu `+`.
- Bỏ khoảng trắng, dấu gạch ngang hoặc ký tự phân cách.

Ví dụ:

| Số khách cung cấp | Số nên dùng để tìm |
|---|---|
| `0345334928` | `345334928` |
| `+84 345 334 928` | `345334928` |
| `84 345 334 928` | `345334928` |
| `+84-345-334-928` | `345334928` |

Với số nước ngoài, có thể tìm bằng số đầy đủ sau khi bỏ dấu `+` và ký tự phân cách, hoặc tìm bằng phần số chính phía sau mã quốc gia.

Ví dụ:

| Số khách cung cấp | Có thể tìm bằng |
|---|---|
| `+1 714-909-7526` | `17149097526` hoặc `7149097526` |
| `+61 412 345 678` | `61412345678` hoặc `412345678` |

### Tìm theo tên

Trong trường hợp không có số điện thoại, TVV có thể tìm theo tên khách hàng.

Các bước:

1. Nhập tên khách hàng vào ô tìm kiếm.
2. Chọn gợi ý `Tìm kiếm Tên cho: ...`.
3. Kiểm tra kết quả hiển thị.
4. Đối chiếu thêm email, số điện thoại, nguồn hoặc cơ hội liên quan để tránh mở nhầm người.

Lưu ý:

- Tên khách hàng có thể bị nhập thiếu dấu, sai chính tả hoặc viết tắt.
- Có thể có nhiều khách trùng tên.
- Không kết luận không có dữ liệu chỉ sau một lần tìm theo tên.

### Tìm theo email

Nếu khách cung cấp email, TVV có thể tìm theo email.

Các bước:

1. Nhập email vào ô tìm kiếm.
2. Chọn gợi ý `Tìm kiếm Email cho: ...`.
3. Kiểm tra kết quả hiển thị.
4. Đối chiếu tên khách hàng và số điện thoại nếu có.

Nếu không ra kết quả, thử tìm lại bằng số điện thoại hoặc tên khách hàng.

### Cần tìm ở những module nào

Khi chưa chắc hồ sơ đang nằm ở đâu, TVV nên kiểm tra ở cả 3 nơi:

| Module | Mục đích kiểm tra |
|---|---|
| `Lead` | Tìm Lead mới, Lead đang xử lý hoặc Lead cần cập nhật tình trạng |
| `Cơ hội` | Tìm cơ hội đang theo pipeline để xử lý tiếp giai đoạn |
| `Contact` | Tìm hồ sơ khách hàng, người đại diện hoặc đối tác đã có trên hệ thống |

Không chỉ tìm trong một module rồi kết luận khách chưa có trên CRM.

### Cách tìm trên module Lead

1. Vào `CRM`.
2. Chọn menu `Lead`.
3. Nhập nội dung cần tìm vào ô tìm kiếm.
4. Chọn đúng trường tìm kiếm theo nội dung đang có.
5. Kiểm tra kết quả hiển thị.

Nếu tìm thấy Lead:

- Mở đúng Lead cần xử lý.
- Kiểm tra tình trạng Lead, người phụ trách và ghi chú trao đổi trước đó.
- Nếu Lead thuộc người khác hoặc không đủ quyền xử lý, báo quản lý hoặc CRM Admin kiểm tra.
- Không tạo Lead mới nếu Lead đó đang tồn tại và còn cần xử lý.

### Cách tìm trên module Cơ hội

1. Vào `CRM`.
2. Chọn menu `Bán hàng` hoặc màn hình pipeline cơ hội.
3. Nhập số điện thoại, tên hoặc email vào ô tìm kiếm.
4. Chọn đúng trường tìm kiếm theo gợi ý của hệ thống.
5. Kiểm tra khách có cơ hội đang xử lý hay không.

Nếu tìm thấy cơ hội:

- Mở đúng cơ hội cần xử lý.
- Kiểm tra giai đoạn pipeline hiện tại.
- Cập nhật hoạt động, ghi chú hoặc chuyển giai đoạn theo đúng quy trình.
- Nếu cơ hội thuộc người khác hoặc cần tiếp nhận lại khách, báo quản lý hoặc CRM Admin xử lý theo phân quyền.

### Cách tìm trên module Contact

1. Vào module `Liên hệ` hoặc `Contact`.
2. Nhập số điện thoại, tên hoặc email vào ô tìm kiếm.
3. Chọn đúng trường tìm kiếm theo gợi ý của hệ thống.
4. Kiểm tra đúng khách hàng, người đại diện hoặc đối tác.

Nếu tìm thấy Contact:

- Mở đúng hồ sơ Contact để kiểm tra thông tin khách hàng.
- Kiểm tra các Lead, cơ hội hoặc đơn hàng liên quan nếu có.
- Nếu đang tạo Lead mới cho khách đã có Contact, chọn khách tại trường `Tên khách hàng`.
- Nếu cần tạo cơ hội mới từ Contact, xử lý theo quy trình cơ hội hoặc báo Admin nếu không đủ quyền.

## PHẦN 2: GHI NHẬN LOGNOTE VÀ LỊCH SỬ CHĂM SÓC

### Lognote là gì

`Lognote/Ghi chú` là phần ghi nhận lịch sử chăm sóc khách hàng trên CRM.

Lognote dùng để lưu lại:

- TVV đã trao đổi gì với khách.
- Khách phản hồi gì.
- Khách đang ở bước xử lý nào.
- Vì sao thay đổi tình trạng Lead hoặc giai đoạn cơ hội.
- Vì sao cơ hội bị mất hoặc đơn hàng bị trả lại.
- Ai là người đã xử lý khách ở từng thời điểm.

### Vì sao lognote quan trọng

Lognote là căn cứ để kiểm tra lại lịch sử làm việc với khách hàng khi có vấn đề phát sinh.

Các trường hợp cần xem lại lognote:

- Xác minh thông tin khách hàng cung cấp có chính xác không.
- Kiểm tra TVV đã tư vấn gì cho khách hàng.
- Kiểm tra khách đã được chăm sóc đến bước nào.
- Xác minh lý do khách ngừng chăm sóc hoặc cơ hội bị mất.
- Kiểm tra lịch sử xử lý khi khách chuyển từ Lead sang cơ hội.
- Kiểm tra thông tin khi đơn hàng bị kế toán trả lại.
- Phân xử trường hợp nhiều TVV cùng liên quan đến một khách hàng hoặc cùng bán chung một đơn hàng.

### Nguyên tắc bắt buộc

Mọi ghi nhận chăm sóc khách hàng phải được xử lý qua `Lognote/Ghi chú` trên CRM.

Hệ thống không ghi nhận các trường hợp ghi chú bên ngoài hệ thống làm căn cứ xử lý chính thức.

Ví dụ ghi chú bên ngoài không được xem là căn cứ chính thức:

- Ghi chú riêng trên giấy.
- Tin nhắn cá nhân không được cập nhật lại vào CRM.
- Ghi chú trong file cá nhân.
- Trao đổi miệng nhưng không có lognote.
- Nội dung lưu ở ứng dụng khác nhưng không đưa vào CRM.

Nếu có tranh chấp hoặc cần xác minh, công ty sẽ ưu tiên kiểm tra lịch sử trên CRM.

### Lognote nằm ở đâu

Lognote nằm ở khung trao đổi bên phải hoặc khu vực lịch sử hoạt động của hồ sơ.

TVV có thể thấy các nút chính:

| Nút | Dùng để làm gì |
|---|---|
| `Gửi tin` | Gửi tin/email theo chức năng hệ thống nếu có |
| `Ghi chú` | Ghi nhận lognote nội bộ |
| `Hoạt động` | Tạo hoạt động cần làm, lịch hẹn, cuộc gọi hoặc nhắc việc |

Với nội dung chăm sóc khách hàng, TVV cần dùng `Ghi chú` để ghi lại lịch sử xử lý.

### Khi nào cần ghi lognote

TVV nên ghi lognote sau mỗi lần có thông tin quan trọng liên quan đến khách hàng.

| Tình huống | Nội dung cần ghi |
|---|---|
| Gọi khách lần đầu | Khách nghe máy hay không, nhu cầu ban đầu, thái độ phản hồi |
| Khách không nghe máy | Thời điểm gọi, số lần gọi, kế hoạch gọi lại |
| Khách hẹn gọi lại | Thời gian khách hẹn, nội dung cần trao đổi tiếp |
| Khách cung cấp thông tin mới | Thông tin học tập, tài chính, hồ sơ, mục tiêu, thời điểm |
| Thay đổi tình trạng Lead | Lý do thay đổi tình trạng |
| Ngừng chăm sóc | Lý do mất hoặc lý do không tiếp tục |
| Chuyển cơ hội | Vì sao đủ điều kiện chuyển cơ hội |
| Chuyển giai đoạn pipeline | Nội dung đã tư vấn và lý do chuyển giai đoạn |
| Báo giá/đơn hàng | Nội dung đã gửi, khách phản hồi gì |
| Kế toán trả lại đơn hàng | Lý do trả lại và TVV đã chỉnh gì |
| Có tranh chấp xử lý khách hàng | Toàn bộ mốc trao đổi liên quan đến quyền tiếp tục xử lý khách |

### Cách ghi lognote

1. Mở đúng hồ sơ cần ghi nhận.
2. Chọn tab/nút `Ghi chú`.
3. Nhập nội dung ghi chú nội bộ.
4. Kiểm tra nội dung rõ ràng, đủ ý.
5. Bấm `Ghi nhận`.
6. Kiểm tra ghi chú đã hiển thị trong lịch sử.

### Nội dung lognote nên có

| Nội dung | Gợi ý |
|---|---|
| Thời điểm trao đổi | Ngày gọi, giờ gọi hoặc mốc thời gian chính |
| Kênh trao đổi | Gọi điện, Zalo, email, gặp trực tiếp, hội thảo |
| Kết quả liên hệ | Nghe máy, không nghe máy, hẹn gọi lại, đã tư vấn |
| Nội dung chính | Khách quan tâm gì, đã tư vấn gì, khách phản hồi gì |
| Bước tiếp theo | Gọi lại, gửi thông tin, tạo hoạt động, chuyển giai đoạn |
| Người liên quan | Nếu có người đại diện, phụ huynh, đối tác hoặc TVV khác |

Ví dụ:

```text
03/06/2026 - Gọi khách qua số 0345xxx928.
Khách quan tâm chương trình EB3 USA, đang tìm hiểu cho năm chương trình 2026.
Đã tư vấn tổng quan điều kiện tài chính và năng lực hồ sơ.
Khách hẹn 05/06 gửi thêm thông tin gia đình và lịch sử làm việc.
Tạo hoạt động gọi lại ngày 05/06/2026.
```

### Lognote trong tranh chấp hoặc bán chung

Trong trường hợp nhiều TVV cùng liên quan đến một khách hàng hoặc cùng bán chung một đơn hàng, lịch sử lognote là căn cứ quan trọng để phân xử.

Nguyên tắc:

- TVV nào có lịch sử chăm sóc rõ ràng trên CRM sẽ có căn cứ xử lý.
- Nội dung không ghi nhận trên CRM có thể không được công nhận.
- Nếu khách chuyển từ TVV này sang TVV khác, cần có lognote thể hiện lý do và thời điểm chuyển.
- Nếu cùng phối hợp bán một đơn hàng, cần ghi rõ vai trò từng người trong lognote.

### Phân biệt Lognote và Hoạt động

| Chức năng | Mục đích |
|---|---|
| `Ghi chú` / Lognote | Ghi lại lịch sử đã xảy ra |
| `Hoạt động` | Tạo việc cần làm trong tương lai |

Ví dụ:

- Đã gọi khách và khách hẹn gọi lại: ghi `Lognote`.
- Cần nhắc gọi lại khách vào ngày mai: tạo `Hoạt động`.

Trong nhiều trường hợp, TVV nên làm cả hai:

1. Ghi lognote nội dung vừa trao đổi.
2. Tạo hoạt động cho bước cần làm tiếp theo.

## PHẦN 3: ACTIVITY / VIỆC CẦN LÀM

### Activity là gì

`Activity/Việc cần làm` là chức năng giao việc, hẹn lịch công việc và theo dõi tiến độ xử lý trên hệ thống.

Activity được dùng để:

- Giao việc nội bộ giữa các cá nhân hoặc phòng ban.
- Tự giao việc cho chính mình để hẹn lịch xử lý.
- Nhắc việc gọi lại khách hàng.
- Nhắc việc kiểm tra hồ sơ, báo giá, đơn hàng.
- Theo dõi task đã xử lý hay chưa.
- Giảm phụ thuộc vào email công việc cho các việc cần xử lý trên CRM.

Activity không thay thế lognote.

| Chức năng | Mục đích |
|---|---|
| `Lognote/Ghi chú` | Ghi lại việc đã xảy ra |
| `Activity/Việc cần làm` | Tạo việc cần làm và theo dõi đã hoàn tất hay chưa |

### Khi nào cần tạo Activity

TVV hoặc các bộ phận liên quan nên tạo Activity khi có một việc cần người khác hoặc chính mình xử lý.

Ví dụ:

- Hẹn gọi lại khách vào ngày cụ thể.
- Giao Admin kiểm tra Lead trùng.
- Giao kế toán kiểm tra đơn hàng.
- Giao team Docs kiểm tra thông tin hồ sơ.
- Nhắc TVV cập nhật lại thông tin khách hàng.
- Nhắc quản lý kiểm tra một tình huống phát sinh.

### My Activities và Created Activities

| Mục | Ý nghĩa | Người cần xem |
|---|---|---|
| `My Activities` | Việc người khác giao cho mình, hoặc việc mình tự giao cho mình để hẹn lịch xử lý | Người nhận việc |
| `Created Activities` | Việc mình đã giao cho người khác | Người giao việc |

`My Activities` giúp người dùng biết hôm nay mình cần xử lý việc gì.

`Created Activities` giúp người giao việc theo dõi task đã được xử lý hay chưa.

### Các trạng thái thường gặp

Activity thường được nhóm theo thời hạn:

| Nhóm | Ý nghĩa |
|---|---|
| `Overdue` | Việc đã quá hạn |
| `Today` | Việc đến hạn hôm nay |
| `This Week` | Việc đến hạn trong tuần |
| `This Month` | Việc đến hạn trong tháng |

Người nhận việc cần ưu tiên xử lý task `Overdue` và task đến hạn `Today`.

### Cách tạo Activity

1. Mở đúng hồ sơ cần giao việc, ví dụ Lead, Cơ hội, Contact hoặc Đơn hàng.
2. Chọn `Hoạt động`.
3. Chọn `Loại hoạt động`, ví dụ `Việc cần làm`, cuộc gọi, cuộc họp hoặc loại phù hợp.
4. Nhập `Tóm tắt` ngắn gọn, rõ việc cần làm.
5. Nhập `Ngày đến hạn`.
6. Chọn `Phân công cho`.
7. Nhập nội dung chi tiết ở phần ghi chú nếu cần.
8. Chọn `Lịch trình`.

Khi tạo Activity, cần ghi rõ:

- Việc cần làm là gì.
- Người xử lý là ai.
- Hạn xử lý khi nào.
- Hồ sơ liên quan là Lead, Cơ hội, Contact hay Đơn hàng nào.
- Nếu có bối cảnh quan trọng, ghi thêm trong phần ghi chú.

### Tự giao việc cho chính mình

TVV có thể tạo Activity cho chính mình để nhắc lịch xử lý.

Ví dụ:

- Gọi lại khách vào ngày mai.
- Kiểm tra lại thông tin hồ sơ sau khi khách gửi bổ sung.
- Nhắc gửi báo giá.
- Nhắc follow-up khách sau hội thảo.

Trường hợp này Activity sẽ xuất hiện trong `My Activities`.

### Giao việc cho người khác

Khi cần phòng ban khác hoặc người khác xử lý, TVV tạo Activity và chọn đúng người ở trường `Phân công cho`.

Ví dụ:

```text
Tóm tắt: Kiểm tra đơn hàng SO630
Phân công cho: Kế toán phụ trách
Ngày đến hạn: 09/06/2026
Ghi chú: Khách đã confirm, nhờ kiểm tra thông tin đơn hàng và phản hồi nếu cần TVV chỉnh.
```

Sau khi giao, task sẽ nằm trong `Created Activities` của người giao và `My Activities` của người được giao.

### Cách xử lý Activity được giao

Khi nhận Activity:

1. Vào `Activities`.
2. Chọn `My Activities`.
3. Kiểm tra các task `Overdue`, `Today`, `This Week`.
4. Mở task cần xử lý.
5. Xử lý công việc theo nội dung được giao.
6. Ghi lognote nếu có thông tin quan trọng cần lưu lịch sử.
7. Đánh dấu hoàn tất khi đã xử lý xong.

### Cách theo dõi Activity đã giao

Khi đã giao việc cho người khác:

1. Vào `Activities`.
2. Chọn `Created Activities`.
3. Kiểm tra task đã giao.
4. Xem task còn mở hay đã hoàn tất.
5. Nếu quá hạn, nhắc người được giao xử lý hoặc cập nhật lại thời hạn nếu cần.

Chức năng này giúp quản lý và người giao việc biết task đã được xử lý hay chưa, thay vì phải hỏi lại qua email hoặc tin nhắn rời rạc.

### Nguyên tắc sử dụng Activity

- Không giao việc ngoài hệ thống nếu việc đó cần theo dõi trên CRM.
- Không dùng email thay thế Activity cho các việc cần tracking trạng thái xử lý.
- Tóm tắt phải rõ ràng, tránh ghi quá chung chung.
- Ngày đến hạn phải đúng thời điểm cần xử lý.
- Phân công đúng người chịu trách nhiệm.
- Nếu Activity liên quan đến khách hàng, phải tạo trên đúng hồ sơ khách hàng/cơ hội/đơn hàng.
- Khi xử lý xong, phải đánh dấu hoàn tất.
- Nếu phát sinh nội dung quan trọng trong quá trình xử lý, cần ghi thêm lognote.

## PHẦN 4: AUTOMATION THU HỒI LEAD/CƠ HỘI KHÔNG XỬ LÝ

### Mục tiêu

Hệ thống có workflow tự động thu hồi Lead hoặc Cơ hội nếu không được xử lý trong thời gian quy định.

Mục tiêu của automation này là tránh tình trạng dữ liệu nằm quá lâu ở một TVV nhưng không được chăm sóc, không được cập nhật tình trạng hoặc không có kết quả xử lý rõ ràng.

Đây là quy định chung chạy xuyên suốt Lead và Cơ hội. TVV cần hiểu để chủ động xử lý đúng hạn, ghi lognote đầy đủ và tạo activity follow-up khi cần.

### Thu hồi Lead khi đang ở TVV

Khi Lead đang ở TVV phụ trách, thời gian xử lý tối đa như sau:

| Tình trạng Lead | Thời gian xử lý tối đa | TVV cần làm trước khi quá hạn |
|---|---|---|
| `Mới` | 2 giờ | Mở Lead, liên hệ khách, ghi lognote và cập nhật tình trạng xử lý |
| `Liên hệ sau` | 24 giờ | Follow-up lại khách, ghi lognote và cập nhật kết quả mới |
| `Đã xác minh` | 15 ngày | Chuyển cơ hội nếu đủ điều kiện hoặc cập nhật `Ngừng chăm sóc` kèm lý do |

Nếu quá thời gian trên mà Lead chưa được xử lý đúng, hệ thống tự động thu hồi Lead về VP.

### Thu hồi Cơ hội khi đang ở TVV

Khi Cơ hội đang ở TVV phụ trách, thời gian xử lý tối đa như sau:

| Loại Cơ hội | Thời gian xử lý tối đa | Kết quả cần có trước khi quá hạn |
|---|---|---|
| Cơ hội du học | 60 ngày | Ra đơn hàng hoặc chuyển `Thất bại` kèm lý do |
| Cơ hội dịch vụ | 60 ngày | Ra đơn hàng hoặc chuyển `Thất bại` kèm lý do |
| Cơ hội định cư | 90 ngày | Ra đơn hàng hoặc chuyển `Thất bại` kèm lý do |

Nếu quá thời gian trên mà Cơ hội chưa có kết quả hợp lệ, hệ thống tự động thu hồi Cơ hội về VP.

### Khi Lead/Cơ hội đang ở VP

Khi Lead hoặc Cơ hội đang ở VP, nếu quá 4 giờ không có TVV tiếp cận hoặc nhận về xử lý, hệ thống tự động chuyển về CSKH.

### TVV cần làm gì để không bị thu hồi

- Không để Lead ở tình trạng `Mới` sau khi đã gọi, nhắn tin hoặc có thông tin xử lý.
- Nếu hẹn khách liên hệ lại, cập nhật đúng `Liên hệ sau`, ghi `Lognote/Ghi chú` và tạo activity follow-up nếu cần.
- Nếu Lead đã `Đã xác minh`, phải tiếp tục chăm sóc đúng hạn, chuyển cơ hội nếu đủ điều kiện hoặc cập nhật `Ngừng chăm sóc` kèm lý do.
- Không để Cơ hội đứng lâu ở một stage nếu đã có kết quả mới.
- Nếu khách vẫn đang cân nhắc, phải có `Lognote/Ghi chú` và activity follow-up rõ ràng.
- Nếu khách không tiếp tục, phải chuyển `Thất bại` và chọn đúng lý do.
- Nếu khách đồng ý ký, phải đi tiếp quy trình báo giá/đơn hàng để Cơ hội có kết quả hợp lệ.
- Khi Lead/Cơ hội bị thu hồi, TVV có thể mất quyền xử lý dữ liệu đó và cần trao đổi với quản lý/VP nếu muốn nhận lại.

## LỖI THƯỜNG GẶP

| Lỗi | Hậu quả | Cách xử lý |
|---|---|---|
| Nhập số điện thoại nhưng không ra kết quả | Đang chọn nhầm trường `Tên` hoặc trường khác | Chọn lại `Điện thoại/di động` |
| Nhập tên nhưng không ra kết quả | Đang chọn nhầm `Điện thoại/di động` hoặc tên bị sai chính tả | Chọn lại `Tên`, thử tìm bằng email hoặc số điện thoại |
| Nhập email nhưng không ra kết quả | Đang chọn nhầm trường tìm kiếm | Chọn lại `Email` |
| Chỉ tìm trong Lead rồi tạo mới | Khách có thể đang nằm trong Contact hoặc Cơ hội | Tìm đủ cả Lead, Cơ hội, Contact |
| Không ghi lognote sau khi tư vấn | Không có căn cứ xác minh lịch sử chăm sóc | Ghi lại ngay sau mỗi lần trao đổi quan trọng |
| Chỉ ghi chú bên ngoài CRM | Không được xem là căn cứ chính thức trên hệ thống | Cập nhật lại vào lognote CRM |
| Ghi lognote quá ngắn | Người khác không hiểu khách đã được xử lý tới đâu | Ghi đủ bối cảnh, kết quả và bước tiếp theo |
| Không ghi khi chuyển người phụ trách | Dễ phát sinh tranh chấp giữa TVV | Ghi rõ lý do chuyển, thời điểm và người tiếp nhận |
| Không tạo Activity cho việc cần theo dõi | Người nhận không có task trên hệ thống, quản lý khó kiểm tra tiến độ | Tạo Activity trên đúng hồ sơ và phân công đúng người |
| Giao việc sai người | Task không được xử lý đúng phòng ban | Kiểm tra lại trường `Phân công cho` trước khi lưu |
| Không đánh dấu hoàn tất | Task vẫn còn mở dù đã xử lý xong | Đánh dấu hoàn tất sau khi xử lý |
| Chỉ gửi email giao việc | Hệ thống không tracking được trạng thái xử lý | Dùng Activity cho các việc cần theo dõi nội bộ |
| Lead bị thu hồi về VP | TVV không xử lý Lead đúng thời gian quy định | Kiểm tra lại lognote/activity, trao đổi quản lý/VP nếu cần nhận lại |
| Cơ hội bị thu hồi về VP | Cơ hội không ra đơn hàng hoặc thất bại đúng thời hạn | Kiểm tra lại tiến độ xử lý, lognote, activity và báo quản lý nếu cần |
| Lead/Cơ hội ở VP bị chuyển về CSKH | Quá 4 giờ không có TVV tiếp cận hoặc nhận về xử lý | VP/TVV cần theo dõi danh sách chờ xử lý và nhận dữ liệu kịp thời |

## CHECKLIST CHO TVV

| Nội dung kiểm tra | Đã kiểm tra | Ghi chú |
|---|---|---|
| Đã xác định đang tìm theo tên, email hay số điện thoại |  |  |
| Đã chọn đúng trường tìm kiếm theo gợi ý của hệ thống |  |  |
| Đã tìm đúng module cần xử lý: Lead, Cơ hội hoặc Contact |  |  |
| Đã mở đúng hồ sơ cần xử lý |  |  |
| Nếu chuẩn bị tạo mới, đã kiểm tra không có dữ liệu trùng |  |  |
| Đã ghi lognote sau trao đổi quan trọng với khách |  |  |
| Nội dung lognote có thời điểm, kết quả và bước tiếp theo |  |  |
| Nếu có chuyển người phụ trách, đã ghi rõ lý do |  |  |
| Nếu có tranh chấp/bán chung, đã ghi rõ vai trò từng người |  |  |
| Nếu có việc cần theo dõi, đã tạo Activity |  |  |
| Activity có tóm tắt, hạn xử lý và người phụ trách rõ ràng |  |  |
| Đã kiểm tra `My Activities` để xử lý task được giao |  |  |
| Đã kiểm tra `Created Activities` để theo dõi task mình giao |  |  |
| Activity đã xử lý xong đã được đánh dấu hoàn tất |  |  |
| Đã kiểm tra Lead/Cơ hội có sắp quá hạn thu hồi hay không |  |  |
| Lead `Mới` đã được xử lý trong tối đa 2 giờ |  |  |
| Lead `Liên hệ sau` đã được follow-up trong tối đa 24 giờ |  |  |
| Lead `Đã xác minh` đã được chuyển cơ hội hoặc ngừng chăm sóc trong tối đa 15 ngày |  |  |
| Cơ hội du học/dịch vụ đã có kết quả trong tối đa 60 ngày |  |  |
| Cơ hội định cư đã có kết quả trong tối đa 90 ngày |  |  |

## BÀI THỰC HÀNH TRAINING

### Bài 1: Chọn đúng trường tìm kiếm

Yêu cầu:

1. Nhập một số điện thoại vào ô tìm kiếm.
2. Chọn `Điện thoại/di động`.
3. Nhập một tên khách hàng vào ô tìm kiếm.
4. Chọn `Tên`.
5. Nhập một email vào ô tìm kiếm.
6. Chọn `Email`.

Kết quả cần đạt:

- Người dùng hiểu nhập nội dung nào thì phải chọn đúng trường tìm kiếm tương ứng.
- Người dùng biết nhập số điện thoại mà chọn `Tên` thì có thể không ra kết quả.

### Bài 2: Tìm khách hàng để xử lý tiếp

Yêu cầu:

1. Tìm số đã chuẩn hóa trong module `Lead`.
2. Tìm tiếp trong module `Cơ hội`.
3. Tìm tiếp trong module `Contact`.
4. Nếu tìm thấy Lead, mở Lead và kiểm tra tình trạng.
5. Nếu tìm thấy cơ hội, mở cơ hội và kiểm tra giai đoạn pipeline.
6. Nếu tìm thấy Contact, mở Contact và kiểm tra thông tin liên quan.

Kết quả cần đạt:

- Người dùng biết tìm đúng Lead, cơ hội hoặc Contact để xử lý tiếp.
- Người dùng biết tìm đủ Lead, Cơ hội và Contact trước khi tạo Lead mới nếu mục tiêu là tạo mới.

### Bài 3: Ghi lognote sau cuộc gọi

Yêu cầu:

1. Mở một Lead hoặc cơ hội.
2. Chọn `Ghi chú`.
3. Ghi nội dung cuộc gọi với khách.
4. Bấm `Ghi nhận`.
5. Kiểm tra lognote đã xuất hiện trong lịch sử.

Kết quả cần đạt:

- Người dùng biết cách ghi lognote đúng vị trí.
- Người dùng hiểu lognote là lịch sử chăm sóc chính thức.

### Bài 4: Phân biệt lognote và hoạt động

Yêu cầu:

1. Ghi lognote nội dung khách vừa trao đổi.
2. Tạo hoạt động gọi lại cho ngày tiếp theo.

Kết quả cần đạt:

- Người dùng hiểu `Ghi chú` là lịch sử đã xảy ra.
- Người dùng hiểu `Hoạt động` là việc cần làm tiếp theo.

### Bài 5: Tạo Activity giao việc

Yêu cầu:

1. Mở một Lead, Cơ hội hoặc Đơn hàng.
2. Chọn `Hoạt động`.
3. Chọn loại hoạt động phù hợp.
4. Nhập tóm tắt việc cần làm.
5. Chọn ngày đến hạn.
6. Chọn người được phân công.
7. Lưu Activity.

Kết quả cần đạt:

- Người dùng biết tạo Activity để giao việc nội bộ.
- Người dùng hiểu Activity thay thế việc giao việc rời rạc qua email khi cần tracking trên CRM.

### Bài 6: Kiểm tra My Activities và Created Activities

Yêu cầu:

1. Vào menu `Activities`.
2. Mở `My Activities`.
3. Kiểm tra việc được giao hoặc việc tự giao cho mình.
4. Mở `Created Activities`.
5. Kiểm tra việc mình đã giao cho người khác.
6. Đánh dấu hoàn tất một Activity đã xử lý xong.

Kết quả cần đạt:

- Người dùng hiểu `My Activities` là việc cần mình xử lý.
- Người dùng hiểu `Created Activities` là việc mình đã giao và cần theo dõi.

### Bài 7: Nhận biết Lead/Cơ hội sắp bị thu hồi

Yêu cầu:

1. Kiểm tra một Lead đang ở tình trạng `Mới`.
2. Xác định Lead đó đã được xử lý trong 2 giờ hay chưa.
3. Kiểm tra một Lead đang ở tình trạng `Liên hệ sau`.
4. Xác định Lead đó đã được follow-up trong 24 giờ hay chưa.
5. Kiểm tra một Cơ hội du học/dịch vụ và xác định có đang quá 60 ngày xử lý hay không.
6. Kiểm tra một Cơ hội định cư và xác định có đang quá 90 ngày xử lý hay không.
7. Ghi lognote hoặc tạo activity follow-up nếu còn cần xử lý tiếp.

Kết quả cần đạt:

- Người dùng hiểu thời hạn xử lý Lead và Cơ hội.
- Người dùng biết cập nhật tình trạng, ghi lognote và tạo activity trước khi dữ liệu bị thu hồi.
- Người dùng hiểu dữ liệu quá hạn có thể tự động về VP hoặc CSKH.

## DOCUMENT CONTROL

| Thuộc tính | Giá trị |
|---|---|
| Tài liệu | Common CRM Operations Guide |
| Phiên bản | 1.0 |
| Nhóm tài liệu | Functional / CRM |
| Người phụ trách | CRM Admin / Training Team |
| Trạng thái | Draft |
