# CHƯƠNG 1: TIẾP NHẬN, XỬ LÝ VÀ ĐÁNH GIÁ LEAD

## I. GIỚI THIỆU

### 1. Mục tiêu

Tài liệu này hướng dẫn Người dùng cách nhận Lead mới để xử lý, tạo Lead mới hoàn toàn khi khách chưa có trên hệ thống, cập nhật đúng loại khách hàng sau khi liên hệ, nhập đầy đủ các trường bắt buộc và đánh giá chất lượng Lead trước khi chuyển thành cơ hội.

Mục tiêu chính là giúp Người nhận ghi nhận đúng thông tin khách hàng, xác định đúng khả năng tư vấn và chỉ chuyển cơ hội đối với Lead đạt tiêu chí.


### 2. Sơ đồ tổng quan quy trình Lead

Sơ đồ dưới đây giúp Người dùng nhìn nhanh toàn bộ luồng xử lý Lead: Lead đi vào CRM từ nhiều nguồn, hệ thống kiểm tra trùng, TVV nhận Lead để liên hệ khách hàng, cập nhật thông tin, đánh giá Qualified Lead và chỉ chuyển cơ hội khi đạt điều kiện.

![Sơ đồ quy trình Lead đến Cơ hội](images/04-lead-process/crm-lead-to-opportunity-tree.svg)

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

### 3. Đối tượng sử dụng

| Nhóm người dùng | Vai trò |
|---|---|
| Tư vấn viên | Liên hệ khách, cập nhật thông tin, đánh giá Lead |
| Marketing | Theo dõi chất lượng Lead từ nguồn Marketing |
| Telesale | Xác minh thông tin ban đầu nếu có |
| CRM Admin | Hỗ trợ kiểm tra dữ liệu và cấu hình quy tắc |
| Quản lý | Theo dõi Lead qualified và hiệu quả chuyển đổi |


### 4. Mở trang làm việc với Lead

TVV mở trang làm việc với Lead theo luồng sau:

1. Trên thanh công cụ dọc bên trái, chọn `Việc cần làm`.
2. Trên thanh menu ngang, chọn `CRM`.
3. Trong nhóm `Lead`, chọn `All Leads`.
4. Nếu màn hình đang có bộ lọc như `My New Leads`, bấm dấu `x` để tắt bộ lọc và vào danh sách Lead chính.

![Mở trang làm việc với Lead](images/04-lead-process/mo-trang-lam-viec-lead-all-leads.png)

Trên màn hình danh sách Lead, TVV cần chú ý các cột sau:

- `Nhân viên kinh doanh`: xác định Lead đang thuộc TVV hay đang thuộc VP chung.
- `Tình trạng`: xác định Lead đang ở trạng thái `Mới`, `Liên hệ sau`, `Đã xác minh`, `Ngừng chăm sóc`, ...

Đối với user là TVV, hệ thống chỉ hiển thị:

- Lead của chính TVV.
- Lead của VP/chi nhánh được phân quyền.

Nếu Lead đang thuộc VP chung, TVV cần lấy Lead về mình trước khi xử lý.

![Giao diện làm việc với Leads](images/04-lead-process/chuongI_Muc1_giao-dien-lead.png)

### II. LÀM VIỆC VỚI LEAD

### 1. Lấy Lead VP về xử lý từ giao diện màn hình chính

Khi danh sách Lead có các Lead thuộc VP chung, TVV có thể lấy Lead về mình để xử lý.

Nguyên tắc:

- Có thể lấy Lead từ VP chung ở bất kỳ `Tình trạng` nào, miễn là Lead đó đang nằm tại VP/chi nhánh được phân quyền.
- Sau khi lấy Lead về, TVV trở thành `Nhân viên kinh doanh` phụ trách Lead đó.
- Chỉ lấy những Lead mình thực sự chuẩn bị xử lý, tránh lấy Lead về nhưng không chăm sóc.

Các bước thao tác trên giao diện danh sách Lead:

Bước 1. Tích chọn các Lead muốn lấy về xử lý.
Bước 2. Chọn một ô đại diện trong cột `Nhân viên kinh doanh`.
Bước 3. Gõ đúng tên TVV phụ trách có dấu trong danh sách gợi ý.
Bước 4. Bấm `Xác nhận` để hệ thống cập nhật cùng lúc các Lead đã chọn.
Bước 5. Kiểm tra lại các Lead vừa cập nhật đã hiển thị đúng tên TVV tại cột `Nhân viên kinh doanh`.

![Lấy Lead VP về TVV xử lý](images/04-lead-process/lay-lead-vp-ve-tvv.png)

Mục tiêu là đảm bảo Lead có người phụ trách rõ ràng trước khi chăm sóc khách hàng.

### 2. Liên hệ khách hàng từ Lead

Sau khi vào đúng phễu Lead cần xử lý, TVV mở từng Lead để liên hệ khách hàng.

Nếu đi từ `My Dashboard`, TVV vào danh sách `XỬ LÝ LEAD MỚI`, sau đó click vào dòng Lead cần xử lý.

![Mở Lead từ danh sách xử lý Lead mới](images/04-lead-process/mo-lead-tu-dashboard-xu-ly-lead-moi.png)

Khi mở Lead, hệ thống hiển thị màn hình làm việc của Lead. Một số thông tin ban đầu có thể đã được hệ thống tự động đổ về, ví dụ:

- `Loại khách hàng`.
- `VP tư vấn`.
- `Nhu cầu`.
- `Thị trường`.
- `Tình trạng lead`.
- `Nguồn`.

TVV cần kiểm tra lại thông tin trước khi gọi và cập nhật lại nếu phát hiện sai.

Các bước:

1. Mở đúng Lead cần xử lý.
2. Đổi mã quốc gia để kiểm tra số điện thoại đúng không
![Gọi Lead từ hệ thống bằng Stringee](images/04-lead-process/goi-lead-tu-dong-stringee1.png)

3. Thao tác `Gọi` tại dòng số điện thoại cần liên hệ .
![Gọi Lead từ hệ thống bằng Stringee](images/04-lead-process/goi-lead-tu-dong-stringee2.png)


Lưu ý:

- Không gọi nhầm số Việt Nam/Mỹ nếu Lead có nhiều số điện thoại.
- Nếu Lead có nhiều số, phải chọn đúng số theo mã quốc gia cần gọi.

### 3. Cập nhật thông tin sau khi liên hệ

Sau khi liên hệ xử lý với Lead, TVV cần:

1. Xác định `Loại khách hàng`.
2. Cập nhật đúng `Tên liên hệ`, `Title` sau khi đã gọi và biết thông tin về khách hàng.
3. Các thông tin `VP tư vấn`, `Nhu cầu`, `Thị trường`, `Nguồn` giữ nguyên.
4. Nếu giao lại cho người khác xử lý mới thay đổi `Nhân viên kinh doanh`.
5. Cập nhật `Tình trạng lead`.
6. Cập nhật `Edupath Tags` nếu đã xác minh được.
7. Lưu Lead.

![Cập nhật thông tin Lead sau khi liên hệ khách hàng](images/04-lead-process/Lead-cap-nhat-thong-tin-sau-lien-he.png)

Nếu hệ thống báo trùng sau khi lưu hoặc Lead bị khóa, TVV xử lý theo phần `Xử lý Lead trùng hoặc Contact đã có` ở bên dưới.

### 4. Bắt buộc ghi Lognote sau mỗi phiên làm việc

Để dễ dàng nhìn thấy được cả màn hình chi tiết Lead và cả `ghi chú` sử dụng tổ hợp phím `command +`

Sau mỗi phiên làm việc với Lead, TVV bắt buộc ghi lại toàn bộ nội dung CSKH bằng `Ghi chú` trên hệ thống.

![Cập nhật thông tin Lead sau khi liên hệ khách hàng](images/04-lead-process/ghi-chu.png)

Nội dung cần ghi gồm:

- Khách có nghe máy hay không.
- Đã gửi SMS/Zalo hay chưa.
- Khách phản hồi nội dung gì.
- Nội dung tư vấn hoặc thông tin đã xác minh.
- Lý do hẹn liên hệ lại hoặc ngừng chăm sóc nếu có.
- Bước xử lý tiếp theo.

`Ghi chú` là lịch sử chính thức của khách hàng trên CRM. Nếu có tranh chấp, kiểm tra trùng, bàn giao khách hàng hoặc xác minh ai đang xử lý khách, hệ thống chỉ căn cứ vào nội dung đã ghi nhận trên CRM.

### III. XỬ LÝ CHI TIẾT VỚI LEAD

### 1. Vì sao cần cập nhật `Loại khách hàng`?

Mỗi loại khách hàng có cách nhập liệu khác nhau. Nếu chọn sai loại khách hàng, thông tin lưu trên CRM sẽ không đúng với thực tế và có thể ảnh hưởng đến quá trình tư vấn, chăm sóc và báo cáo.

Ví dụ:

- Người trực tiếp có nhu cầu du học/ định cư/ dịch vụ là `Khách hàng`.
- Phụ huynh hoặc người liên hệ thay cho học sinh/ khách hàng là `Người đại diện`.
- Đơn vị hoặc cá nhân (agent) giới thiệu khách hàng là `Đối tác` (TVV phải thông qua BM để xử lý).


### 1.1. Loại khách hàng: Khách hàng

Chọn `Loại khách hàng` là `Khách hàng` khi người TVV đang trao đổi là người trực tiếp có nhu cầu du học, định cư hoặc sử dụng dịch vụ.

Trường hợp người liên hệ đang tìm hiểu thay cho người khác nhưng TVV chưa xin được thông tin của khách hàng chính, vẫn tạm thời giữ `Loại khách hàng` là `Khách hàng`. Sau khi xác minh được người có nhu cầu thực tế, TVV cập nhật lại thông tin cho đúng.

![Xác định Loại khách hàng là Khách hàng](images/04-lead-process/xac-dinh-loai-khach-hang-khach-hang.png)

Các bước cần thực hiện:

Bước 1. Kiểm tra trường `Loại khách hàng` và chọn `Khách hàng`.

Bước 2. Kiểm tra đúng `Mã quốc gia` theo số điện thoại của khách.

Bước 3. Cập nhật `Tên liên hệ` theo họ tên khách sau khi trao đổi. Ưu tiên nhập đủ họ và tên.

Bước 4. Cập nhật `Title` theo giới tính của khách.

Bước 5. Nếu trong quá trình tư vấn đã xác định được mục tiêu của khách, cập nhật `Edupath Tags` là `Mục tiêu (Goal)`.

Bước 6. Cập nhật `Tình trạng lead` theo kết quả xử lý thực tế. Nếu đã xác định được mục tiêu của khách và đã gắn `Edupath Tags` là `Mục tiêu (Goal)`, cập nhật `Tình trạng lead` là `Đã xác minh`.

Bước 7. Kiểm tra lại các thông tin đang có trên Lead. Thông tin nào đã đúng thì giữ nguyên, thông tin nào thiếu hoặc sai thì cập nhật lại.

Bước 8. Lưu thông tin Lead.


### 1.2. Loại khách hàng: Người đại diện

Chọn `Loại khách hàng` là `Người đại diện` khi người TVV đang trao đổi không phải khách hàng chính, nhưng là người đại diện tìm hiểu chương trình cho khách hàng chính.

Ví dụ:

- Bố hoặc mẹ của học sinh.
- Người thân liên hệ thay.
- Người bảo hộ.

Để nhìn đầy đủ thông tin trên cùng một màn hình, TVV có thể dùng tổ hợp phím `Command -` để thu nhỏ màn hình. Khi muốn quay lại kích thước ban đầu, dùng `Command +`.

![Xác định Loại khách hàng là Người đại diện](images/04-lead-process/xac-dinh-loai-khach-hang-nguoi-dai-dien.png)

Các bước cần thực hiện:

Bước 1. Chọn `Loại khách hàng` là `Người đại diện`. Khi chọn loại này, thông tin người đại diện sẽ được nhập ở cụm thông tin bên phải.

Bước 2. Chọn đúng `Mối quan hệ` giữa người đại diện và khách hàng chính. Nếu là phụ huynh thì chọn `Bố/Mẹ`; nếu là anh/chị/em hoặc người tìm hiểu giúp thì chọn `Người thân`.

Bước 3. Nhập đầy đủ `Họ và tên` của người đại diện, tức người TVV vừa liên hệ tư vấn và xác định đang tìm hiểu chương trình cho con hoặc người thân. Khi hệ thống hiện hộp `Tạo và chỉnh sửa`, mở hộp này để bổ sung thông tin chi tiết.

Bước 4. Trong hộp `Tạo và chỉnh sửa`, nhập thông tin của người đại diện gồm `Điện thoại`, `Tiêu đề` theo giới tính và `Nguồn`. Trường `Nguồn` cần chọn đúng nguồn đầu vào đang hiển thị trên Lead.

Bước 5. Chọn `Lưu & Đóng` để lưu thông tin người đại diện. Bảng này dùng cho người đại diện được xác định là cá nhân.

Bước 6. Nhập thông tin khách hàng chính ở cụm thông tin bên trái, gồm `Tên liên hệ`, `Title` theo giới tính, `SĐT` và `Mã quốc gia`. Đây là thông tin của người có nhu cầu thực tế, ví dụ con hoặc người thân của người đại diện.

Bước 7. Cập nhật `Tình trạng lead` và `Edupath Tags` theo kết quả trao đổi thực tế.

Bước 8. Kiểm tra lại toàn bộ thông tin hệ thống đã có sẵn trên Lead, gồm `Nguồn`, `VP tư vấn`, `Nhu cầu`, `Thị trường`, `Người phụ trách`, `Nhóm kinh doanh` và `Chi nhánh`. Thông tin nào đúng thì giữ nguyên, thông tin nào thiếu hoặc sai thì cập nhật lại.

Bước 9. Lưu Lead.

Lưu ý:

- Không nhập người đại diện như khách hàng chính nếu thực tế họ chỉ là người liên hệ thay.
- Cần ghi rõ `Mối quan hệ` để TVV, CSKH và các bộ phận liên quan hiểu đúng vai trò của người đang trao đổi.
- Thông tin người đại diện và thông tin khách hàng chính cần được tách rõ để tránh nhầm người tư vấn, nhầm khách hàng chính hoặc thất lạc nhóm gia đình.


### 2. Đánh giá chất lượng Lead đầu vào

### 2.1. Sơ đồ đánh giá chất lượng Lead

![Sơ đồ đánh giá chất lượng Lead](images/04-lead-process/so-do-danh-gia-qualified.png)

Được thể hiện trên màn hình chi tiết Lead:

![Sơ đồ đánh giá chất lượng Lead](images/04-lead-process/so-do-danh-gia-qualified1.png)

Sau khi gọi Lead, nhắn tin hoặc có bất kỳ thao tác chăm sóc khách hàng nào, TVV cần cập nhật đúng `Tình trạng lead` theo kết quả xử lý thực tế.

Đây là thông tin quan trọng để hệ thống automation đánh giá Lead và để quản lý kiểm tra lịch sử chăm sóc.

#### 2.2. Tình trạng `Mới`

`Mới` là tình trạng mặc định khi Lead vừa đổ về hệ thống hoặc khi TVV vừa nhận Lead từ VP/chung về để chuẩn bị xử lý.

![Lead ở tình trạng Mới](images/04-lead-process/lead-invalid-phone-number.png)

TVV chỉ giữ Lead ở `Mới` khi chưa có thao tác chăm sóc nào với khách hàng.

#### 2.3. Tình trạng `Liên hệ sau`

`Liên hệ sau` dùng khi TVV đã gọi hoặc nhắn tin cho khách nhưng khách chưa nghe máy/chưa phản hồi, và Lead vẫn cần tiếp tục follow-up.

![Cập nhật tình trạng Liên hệ sau](images/04-lead-process/tinh-trang-lien-he-sau-lan-1.png)

Nguyên tắc xử lý:

- Sau lần gọi đầu tiên không nghe máy, cập nhật `Tình trạng lead` là `Liên hệ sau`.
- Nếu số điện thoại đúng định dạng nhưng khi gọi hệ thống báo `thuê bao`, TVV vẫn để `Tình trạng lead` là `Liên hệ sau` để tiếp tục kiểm tra lại.
- TVV thực hiện tối đa 3 cuộc gọi, thời gian thực hiện lại giữa 2 cuộc gọi ở `Tình trạng lead` = `Liên hệ sau` tối đa 24 giờ nếu khách hoàn toàn không nghe máy hoặc báo thuê bao.
- Sau mỗi cuộc gọi không nghe máy hoặc báo thuê bao, TVV bắt buộc ghi `Lognote/Ghi chú` để lưu lịch sử làm việc.
- Nếu có kết bạn Zalo, gửi Zalo hoặc để lại lời nhắn, TVV nên chụp màn hình và đính kèm vào `Lognote/Ghi chú` làm bằng chứng xử lý.

#### 2.3. Tình trạng `Đã Xác Minh`

`Đã Xác Minh` dùng khi TVV đã gọi/gặp được khách hàng và xác nhận được thông tin tư vấn thực tế. Đây là bước bắt đầu đánh giá chất lượng Lead, vì vậy TVV chỉ gắn `Edupath Tags` sau khi đã xác minh được khách hàng.

![Cập nhật tình trạng Đã Xác Minh](images/04-lead-process/tinh-trang-da-xac-minh.png)

Các bước xử lý:

1. Sau khi đã tư vấn/gặp được khách, nhập đúng `Tên liên hệ` và giới tính.
3. Gắn `Edupath Tags` để đánh giá tiềm năng cơ hội của Lead. Chỉ sử dụng `Tag` đánh giá ở bước đã xác minh khách hàng.
4. Cập nhật `Tình trạng lead` thành `Đã Xác Minh`.
5. Cập nhật `Edupath Tags` là `Mục tiêu (Goal)`, tiếp tục đánh giá thêm.
6. Nhập `Ghi chú` nội dung đã trao đổi với khách hàng: nhu cầu, thời điểm, mục tiêu, tài chính hoặc năng lực hồ sơ nếu đã khai thác được.
7. Bấm `Lưu`.

Lưu ý:

- Không gắn `Edupath Tags` khi chưa gặp hoặc chưa xác minh được khách hàng.
- `Ghi chú` cần đủ rõ để người khác đọc lại hiểu khách đã trao đổi gì và vì sao Lead được đánh giá như vậy.


#### 2.4. Tình trạng `Ngừng chăm sóc`.

1. Ở lần gọi cuối cùng của `Tình trạng lead`: `Liên hệ sau`, nếu khách vẫn không nghe máy, TVV cập nhật:

- `Tình trạng lead`: `Ngừng chăm sóc`.
- `Lý do`: `Không nghe máy`.
- `Lognote/Ghi chú`: ghi rõ đây là lần gọi thứ 3 và là lần chuyển tình trạng từ `Liên hệ sau` sang `Ngừng chăm sóc`.

![Chuyển từ Liên hệ sau sang Ngừng chăm sóc khi gọi lần 3 không nghe máy](images/04-lead-process/tinh-trang-lien-he-sau-lan-3-ngung-cham-soc.png)

2. Trường hợp khi TVV đã gọi được khách tuỳ vào từng tình huống cụ thể nếu không thể tiếp tục tư vấn cho khách hàng đó thì TVV cập nhật `Ngừng chăm sóc` và chọn đúng `Lý do mất`.

Ví dụ: 

![Cập nhật tình trạng Ngừng chăm sóc khi chưa tư vấn được khách hàng](images/04-lead-process/tinh-trang-ngung-cham-soc-chua-tu-van.png)

Các bước xử lý:

Bước 1: Cập nhật `Tình trạng lead` là `Ngừng chăm sóc`.
Bước 2: Chọn đúng `Lý do` theo nội dung khách phản hồi:
   - `Không có nhu cầu`: khách báo không có nhu cầu ngay từ đầu hoặc không muốn tìm hiểu tiếp.
   - `Chọn đơn vị khác`: khách đã làm việc/chọn đơn vị tư vấn khác.
   - `Tài chính không phù hợp`: Khách hiện chưa có tài chính, tài chính chưa đủ.
   - `Đã tư vấn không phản hồi`: sau khi tư vấn xong liên hệ lại khách không còn nghe máy.
   - `Không phù hợp điều kiện`: khách không đủ các điều kiện tham gia chương trình hoặc chương trình khách mong muốn không có.
   - `Thời gian chưa phù hợp`: khách chỉ muốn tư vấn trước chưa có điều kiện đi tại thời điểm này hoặc thời gian dự kiến khách mong muốn còn quá xa.
   - `Lý lịch tư pháp`: khách có tiền án, tị nạn, bất hợp pháp.
   - `Mục tiêu du học khác`: khách có các nhu cầu du học khác ngoài các thị trường và ngành hiện có của công ty.
   - `Không phù hợp độ tuổi`: Khách còn quá nhỏ hoặc quá tuổi tham gia chương trình.
   - `Xuất khẩu lao động`: khách chỉ muốn đi xuất khẩu lao động không phải đi định cư làm việc (sau khi đã tư vấn kỹ về chương trình).
   - `Năng lực đảng viên`: khách hiện là Đảng viên.
   - `Tìm hiểu cho biết`: khách chỉ mong muốn tìm hiểu cho biết hoặc sau khi đã tư vấn đầy đủ thông tin thì báo lại không còn nhu cầu nữa.
Bước 3: Ghi `Lognote/Ghi chú` ngắn gọn nội dung trao đổi. Ví dụ: "Gọi được khách, khách báo đã chọn đơn vị khác, không tiếp tục tư vấn."
Bước 4: Bấm `Lưu` để hệ thống ghi nhận tình trạng và lý do mất.


#### 2.5. Tình trạng `Close`

`Close` dùng khi Lead là dữ liệu rác hoặc số điện thoại không hợp lệ, ví dụ sai số, thiếu số, không có tín hiệu, số điện thoại không có thực hoặc hệ thống báo `invalid phone number`.

Nếu số điện thoại đúng định dạng nhưng khi gọi báo `không có tín hiệu` hoặc xác định là `số điện thoại không có thực`, TVV cập nhật `Tình trạng lead` là `Close` và gửi Activity cho CS kiểm tra lại dữ liệu.

![Cập nhật tình trạng Close và giao Activity cho CS kiểm tra số điện thoại](images/04-lead-process/tinh-trang-close-gui-cs-kiem-tra-sdt.png)

Các bước xử lý ban đầu:

1. Chọn đúng `Mã quốc gia` để hệ thống kiểm tra số điện thoại. Ví dụ: `VN`, `US`, `AU`, `CA`, `JP`.
2. Nếu hệ thống báo số điện thoại không hợp lệ, cập nhật `Tình trạng lead` là `Close`.
3. Tạo `Activity/Hoạt động` giao cho `CS Quỳnh Phạm` kiểm tra lại số điện thoại. Cách tạo Activity xem lại tài liệu training `Activity`.
4. Kiểm tra phần chatter để chắc chắn Activity đã được gửi và hiển thị trên Lead.

Sau khi CS kiểm tra, có 2 tình huống:

**Tình huống 1: CS xác nhận số điện thoại vẫn sai**

Nếu CS kiểm tra và xác nhận số điện thoại vẫn sai, Lead này được xem là Lead rác.

![CS xác nhận số điện thoại vẫn sai](images/04-lead-process/tinh-trang-close-cs-tra-ve-sdt-sai.png)

TVV xử lý như sau:

- Giữ nguyên `Tình trạng lead` là `Close`.
- Không cần tiếp tục chăm sóc Lead này.
- Bấm `Lưu` nếu có thay đổi cần lưu lại.
- Không chuyển sang tình trạng khác nếu chưa có số điện thoại đúng để liên hệ khách.

**Tình huống 2: CS cập nhật lại số điện thoại đúng và gửi Activity cho TVV xử lý lại**

Nếu CS tìm được số điện thoại đúng, CS sẽ cập nhật lại số trên Lead và gửi một Activity mới để TVV vào xử lý lại.

TVV cần kiểm tra Activity hằng ngày để không bỏ sót các task CS gửi trả về.

![CS cập nhật lại số điện thoại đúng và TVV xử lý lại Lead](images/04-lead-process/tinh-trang-close-cs-cap-nhat-sdt-dung.png)

Các bước TVV xử lý lại:

1. Mở Activity được CS gửi về và kiểm tra số điện thoại đã hết báo `invalid phone number`.
2. Bấm `Gọi` để gọi lại khách hàng. Nếu số có đổ chuông hoặc liên hệ được, đây là số có thật.
3. Thay đổi `Tình trạng lead` sang tình trạng phù hợp, không giữ `Close` nữa. Ví dụ: `Liên hệ sau` nếu gọi có chuông nhưng khách chưa nghe máy.
4. Bấm `Hoàn tất` trên Activity đã được CS giao.
5. Khi hệ thống hiện pop-up hoàn tất Activity, để lại ghi chú kết quả xử lý.
6. Bấm `Hoàn tất Activity`.
7. Bấm `Lưu` Lead để lưu lại thông tin mới nhất.

Lưu ý:

- `Close` chỉ dùng khi dữ liệu không thể xử lý tiếp tại thời điểm đó.
- Nếu CS đã cập nhật lại số điện thoại đúng, TVV phải xử lý lại Lead theo kết quả liên hệ thực tế.
- Không để Lead tiếp tục ở `Close` nếu số điện thoại đã được xác minh là đúng và có thể gọi lại khách.


## IV. ĐÁNH GIÁ TIỀM NĂNG CHUYỂN CƠ HỘI CỦA LEAD

### 1. Mục tiêu

Đánh giá Lead sau khi đã gặp khách hàng giúp xác định Lead có đủ chất lượng để chuyển thành cơ hội hay chưa.

Hệ thống sử dụng `Edupath Tag` để đánh giá số sao. Tiêu chí chuyển cơ hội phụ thuộc chính xác vào số sao ở tình trạng xác minh của Lead.

Khi Lead đủ điều kiện, hệ thống automation sẽ tự động hiển thị pop-up chuyển cơ hội. Đây vẫn là thao tác mở để TVV nhập thông tin cơ hội trước khi tạo cơ hội chính thức.

### 2. Quy tắc đánh giá tiềm năng sao

![Sơ đồ đánh giá sao](images/04-lead-process/danh-gia-sao.png)

| Mức sao | Điều kiện Edupath Tag | Ý nghĩa |
|---|---|---|
| 0 sao | Chỉ có `Mục tiêu (Goal)` | Lead có mục tiêu và nhu cầu cho chương trình quan tâm |
| 1 sao | Có `Mục tiêu (Goal)` và `Tài chính (Finance)` hoặc `Năng lực hồ sơ` | Lead có một trong hai tiêu chí quan trọng |
| 2 sao | Có cả `Mục tiêu (Goal)` và `Tài chính (Finance)` và `Năng lực hồ sơ` | Lead đủ điều kiện tốt để chuyển cơ hội |
| 3 sao | Có đủ 4 tiêu chí: `Mục tiêu (Goal)`, `Tài chính (Finance)`, `Năng lực hồ sơ`, `Thời điểm (Timeline)` | Đánh giá ở cơ hội đủ điều kiện chuyển đơn hàng (Sử dụng ở giai đoạn cơ hội) |

Ví dụ: khi TVV khai thác thêm thông tin và cập nhật `Edupath Tags`, hệ thống tự động ghi nhận lịch sử thay đổi trong `Lognote/Ghi chú` và cập nhật lại mức sao của Lead.

![Sơ đồ đánh giá sao](images/04-lead-process/danh-gia-sao0.png)

![Sơ đồ đánh giá sao](images/04-lead-process/danh-gia-sao1.png)

### 3. Điều kiện hiện pop-up thông tin cơ hội

Pop-up chuyển cơ hội chỉ hiển thị khi Lead thỏa cả hai điều kiện:

1. `Tình trạng lead` là `Đã xác minh`.
2. `Mức độ ưu tiên` đạt từ `2 sao` trở lên.

Với Lead đạt `2 sao`, cần có đủ các tag:

- `Mục tiêu (Goal)`
- `Tài chính (Finance)`
- `Năng lực hồ sơ`

![Sơ đồ đánh giá sao](images/04-lead-process/danh-gia-sao2.png)

Nếu Lead không đúng tình trạng hoặc chưa đạt đủ 2 sao, hệ thống sẽ không cho chuyển cơ hội.

Khi Lead đã đúng tình trạng `Đã Xác Minh` và đạt đủ `2 sao`, sau khi bấm `Lưu`, hệ thống sẽ hiện pop-up chuyển cơ hội để TVV nhập thông tin cơ hội.


### 4. Thao tác khi pop-up chuyển cơ hội hiển thị

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

![Pop-up chuyển cơ hội khi Lead đủ điều kiện 2 sao](images/04-lead-process/ket-qua-lead.png)

![Giao diện Cơ hội](images/04-lead-process/ket-qua-lead1.png)


Lưu ý về `Năm chương trình`:

- `Năm chương trình` được tính theo năm kinh doanh của công ty, không chỉ theo năm dương lịch.
- Ví dụ giai đoạn `09/2025 - 08/2026` được ghi nhận là `Năm chương trình` `2026`.
- Người dùng cần chọn đúng năm chương trình vì thông tin này sẽ đi theo cơ hội, báo giá và báo cáo kinh doanh.

Lưu ý về `Nhu cầu thực tế`, `Chương trình tư vấn` và `Thị trường`:

- Ba thông tin này cần khớp với bảng giá sản phẩm. tìm kiếm trong mục Bảng giá sản phẩm.
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
| Thiếu tag `Tài chính (Finance)` | Xác minh lại khả năng tài chính của khách và cập nhật tag nếu đúng |
| Thiếu tag `Năng lực hồ sơ` | Xác minh lại điều kiện hoặc hồ sơ của khách và cập nhật tag nếu đúng |

Sau khi cập nhật đúng thông tin, nếu Lead đạt điều kiện, hệ thống sẽ tự động hiện pop-up chuyển cơ hội.

![Lỗi thiếu thông tin khi chuyển cơ hội ](images/04-lead-process/ket-qua-lead-loi.png)


## V. TVV tự TẠO LEAD THEO NGUỒN TVV

### 1. Khi nào tạo Lead nguồn TVV

- Khách gọi trực tiếp cho TVV.
- Khách nhắn tin riêng.
- Khách được giới thiệu trực tiếp.

### 2. Kiểm tra thông tin trước khi tạo Lead

Kiểm tra thông tin trùng khách hàng trước khi tạo Lead (xem lại Chương I - Mục II)

### 3. Tạo Lead mới 

### 3.1 Các bước tạo Lead mới nguồn TVV

Lead do TVV chủ động tìm kiếm đều đến từ việc đã có tư vấn trước nên đây là Lead sau tư vấn được cập nhật lên hệ thống không phải là Lead mới

1. Trên thanh công cụ dọc bên trái, chọn `Việc cần làm`.
2. Trên thanh menu ngang, chọn `CRM`.
3. Chọn menu `All Leads`.
4. Chọn `Mới`.
5. Nhập đúng các bước tạo Lead
6. Lưu Lead.

![Tạo Lead mới nguồn TVV tự tìm kiếm](images/04-lead-process/Lead-moi-tvv.png)

![Tạo Lead mới nguồn TVV tự tìm kiếm](images/04-lead-process/Lead-moi-tvv1.png)

Nếu sau khi lưu bị báo trùng, TVV không tạo lại nhiều lần. TVV kiểm tra Contact đã có trên hệ thống chưa hoặc báo CRM Admin xử lý.

### 3.2 Tạo Lead mới bị trùng

Lead tạo ra bị trùng sẽ được phát hiện theo 2 cách sau:

- Nếu đang nhập thông tin Lead xuất hiện Nút `Similar Lead`.
- Nếu không nhìn thấy và tiếp tục `Lưu` hoàn thành sẽ xuất hiện `Hộp báo lỗi`.

![Tạo Lead mới nguồn TVV tự tìm kiếm](images/04-lead-process/Lead-moi-tvv2.png)

Khi gặp tất cả các tình huống trùng của Lead báo về cho Admin Hệ thống để xử lý.


## VI. BÀI THỰC HÀNH TRAINING

### Bài 1: Nhận Lead VP về xử lý

Yêu cầu:

1. Trên thanh công cụ dọc bên trái, chọn `Việc cần làm`.
2. Trên thanh menu ngang, chọn `CRM`.
3. Mở menu `Lead`.
4. Tìm Lead có `Nhân viên kinh doanh` là VP của TVV.
5. Tích chọn Lead muốn lấy về xử lý.
6. Chọn một ô đại diện trong cột `Nhân viên kinh doanh`.
7. Cập nhật thành tên TVV phụ trách.
8. Lưu lại thay đổi.

Kết quả cần đạt:

- Lead có người phụ trách rõ ràng.
- TVV biết cách nhận Lead VP/nhóm chung về mình trước khi chăm sóc.

### Bài 2: Liên hệ khách hàng từ Lead

Yêu cầu:

1. Mở Lead đã được phân công.
2. Kiểm tra số điện thoại và mã quốc gia.
3. Nếu khách có nhiều số, xác định đúng số VN, US hoặc số quốc tế cần gọi.
4. Bấm `Gọi` để liên hệ khách hàng.
5. Nếu khách chưa nghe máy, cập nhật tình trạng và `Ghi chú` kết quả liên hệ.
6. Lưu lại.

Kết quả cần đạt:

- TVV biết gọi đúng số theo mã quốc gia.
- Lịch sử chăm sóc được ghi nhận trên CRM.

### Bài 3: Tạo Lead mới hoàn toàn

Yêu cầu:

1. Kiểm tra số điện thoại trong module `Lead`.
2. Kiểm tra số điện thoại trong module `Cơ hội`.
3. Kiểm tra số điện thoại trong module `Contact`.
5. Xác định `Loại khách hàng`.
6. Nhập các trường bắt buộc.
7. Lưu Lead.

Kết quả cần đạt:

- Lead được tạo thành công khi khách hàng chưa có trên hệ thống.
- Người dùng biết chỉ dùng `Tên liên hệ` khi tạo khách hàng mới hoàn toàn.
- Các trường bắt buộc được nhập đầy đủ.

### Bài 4: Tạo Lead từ Contact đã tồn tại

Yêu cầu:

1. Tạo giả định bằng 1 sdt đã tồn tại trên hệ thống.
2. Nhập các thông tin còn thiếu của Lead.
3. Xác định các lỗi trùng xuất hiện
4. Liên hệ về Admin hệ thống.

Kết quả cần đạt:

- Biết được Lead đã tồn tại báo trùng.
- Báo về Admin để xử lý kết quả

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
2. Chọn Edupath Tag theo tình huống đánh giá tiềm năng cơ hội đưa ra.
3. Kiểm tra mức sao.
4. Xác định Lead có đủ điều kiện chuyển cơ hội hay chưa.

Kết quả cần đạt:

- Người dùng hiểu cách chọn tag.
- Người dùng xác định đúng mức 0 sao, 1 sao, 2 sao hoặc 3 sao.

### Bài 7: Xử lý pop-up chuyển cơ hội

Yêu cầu:

1. Mở Lead đã có `Tình trạng lead` là `Đã xác minh`.
2. Chọn Edupath Tag để Lead đạt 2 sao.
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
