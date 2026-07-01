# Khai thác lead (Lead Mining)

**Lead Mining** cho phép tìm và tạo lead mới dựa trên tiêu chí (quốc gia, ngành, quy mô công ty…) thông qua dịch vụ IAP của Odoo (thường cần **Enterprise** và credit).

## Cấu hình

1. Vào **CRM › Cấu hình › Cài đặt**
2. Tìm mục **Lead Mining** (Khai thác lead)
3. Bật tính năng và **Lưu**

!!! note "Ghi chú"
    Cần cấu hình **Email Alias** hoặc quyền IAP nếu công ty bạn dùng dịch vụ trả phí theo credit Odoo.

## Tạo lead qua Lead Mining

1. **CRM › Leads** (hoặc menu **Lead Mining** nếu hiển thị)
2. Chọn **Lead Mining** / **Generate Leads**
3. Thiết lập tiêu chí:
   - **Countries** — quốc gia
   - **Industries** — ngành
   - **Company size** — quy mô
   - Số lượng lead cần
4. Xác nhận — hệ thống tạo lead và gán cho team/salesperson

## Chi tiết sau khi tạo

- Lead mới xuất hiện trong danh sách với nguồn **Lead Mining**
- Kiểm tra trùng lặp với khách hàng hiện có trước khi convert
- Cập nhật pipeline stage phù hợp

## Lưu ý pháp lý & dữ liệu

- Tuân thủ quy định **spam / GDPR / NĐ 13** khi liên hệ khách hàng mới
- Chỉ dùng cho mục đích B2B phù hợp với chính sách công ty

!!! warning "Credit IAP"
    Mỗi lần khai thác có thể tiêu tốn credit. Kiểm tra với admin trước khi chạy số lượng lớn.

Xem thêm: [Leads](leads.md) | [Pipeline](pipeline.md)
