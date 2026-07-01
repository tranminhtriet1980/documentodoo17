# Đơn bán (Sales Order)

Sau khi TVV **Confirm** báo giá, trạng thái chuyển **Đơn bán hàng** — cơ hội CRM tự **Thành công**. Quy trình báo giá đầy đủ: [Báo giá, đơn bán hàng và hợp đồng](../crm/bao-gia-don-hang.md) (CRM VAN).

## Trạng thái liên quan

| Trạng thái | Mô tả |
|------------|--------|
| **Quotation / Báo giá** | Nháp hoặc đã gửi email |
| **Sales Order / Đơn bán hàng** | Đã **Confirm** — khách đồng ý |
| **Locked** | Khóa chỉnh sửa (tùy workflow) |

## Sau khi Confirm

1. Kiểm tra đơn: khách, sản phẩm, chương trình, VP tư vấn.
2. **Kế toán** hoàn tất hợp đồng trên hệ thống → cập nhật **KPI** TVV (theo ngày đóng tiền).
3. Team **Docs** nhận hồ sơ từ thông tin **Other Info** trên đơn.

## Giao hàng (nếu bật Kho)

- Smart button **Delivery** — phiếu giao
- **Validate** picking khi xuất kho thực tế

## Thanh toán & hóa đơn

- **Create Invoice** — tạo hóa đơn (đặt cọc, giao một phần, cuối kỳ…)
- Xem [Hóa đơn khách hàng](hoa-don.md)

## Hủy đơn

- **Cancel** báo giá (trước Confirm) → cơ hội **Thất bại** (automation).
- Hủy **đơn bán** sau Confirm → **kế toán** xử lý; KPI: hủy hoàn tiền = mất điểm, không hoàn tiền = giữ điểm (xem [Báo giá & đơn hàng](../crm/bao-gia-don-hang.md)).

!!! warning "Sửa đơn đã xác nhận"
    Khách **đổi sản phẩm sau khi ký** → không sửa tay đơn cũ; tạo **cơ hội + đơn mới**, kế toán hủy đơn cũ.

!!! warning "Đơn bị kế toán trả lại"
    Thường thiếu thông tin tab **Other Info** (Docs) hoặc sai Discount/Promotion — sửa trên CRM và ghi **Lognote**.

Xem: [Báo giá & quy trình Confirm](../crm/bao-gia-don-hang.md) | [Pipeline CRM](../crm/pipeline.md)
