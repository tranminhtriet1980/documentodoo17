# 5. Kiểm kê (Điều chỉnh tồn kho)

Kiểm kê dùng để **đưa tồn trên hệ thống khớp với tồn đếm thực tế**. Chức năng này dùng **Điều chỉnh tồn kho chuẩn của Odoo** — module `edupath_stock` **không** thêm/sửa gì ở đây, nên **không** đi qua quy trình phê duyệt nhập/xuất của Edupath.

## Kiểm kê định kỳ

1. **Tồn kho › Vận hành › Điều chỉnh tồn kho** (Inventory Adjustments / Physical Inventory).
2. Lọc theo **Vị trí**, **Sản phẩm** (hoặc **Nhóm sản phẩm**) cần đếm.
3. Nhập **Số lượng đã đếm** (Counted Quantity) cho từng dòng.
4. Bấm **Áp dụng** (Apply) — hệ thống tạo **dòng điều chỉnh** đưa tồn về đúng số đếm.

!!! note "Không qua duyệt KTT / 6 bước"
    Điều chỉnh tồn kho tạo **di chuyển điều chỉnh riêng** (từ/đến vị trí ảo *Inventory adjustment*), **không** phải phiếu nhập (Receipt) hay phiếu xuất (Delivery). Vì vậy nó **không** chịu bước *Gửi KTT phê duyệt* hay quy trình xuất 6 bước — và cũng **không bị chặn** bởi kiểm tra tồn khả dụng. Hãy giới hạn quyền điều chỉnh cho đúng người.

!!! warning "Quyền"
    Điều chỉnh tồn thường cần nhóm **Quản lý Tồn kho** (Inventory Manager). Cân nhắc kỹ trước khi cho phép vì thao tác này thay đổi tồn **trực tiếp**.

## Lô / Serial khi kiểm kê

Nếu sản phẩm theo dõi **Lô/Serial**, đếm và điều chỉnh **theo từng lô** để tồn theo lô luôn chính xác (phục vụ truy xuất). Báo cáo tồn kho Edupath cũng tách tồn theo lô, nên số kiểm kê theo lô mới khớp báo cáo.

## Đối chiếu sau kiểm kê

- Dùng **[Báo cáo tồn kho](ton-kho.md#bao-cao-ton-kho-chot-theo-ky)** (chốt theo ngày) để so tồn hệ thống với biên bản đếm.
- Dùng **Báo cáo nhập/xuất kho** trong kỳ để tìm nguyên nhân lệch.

## Nguyên nhân lệch thường gặp

| Nguyên nhân | Cách xử lý |
|-------------|-----------|
| Phiếu nhập **chưa được KTT duyệt & Validate** | Hoàn tất duyệt nhập rồi Validate (xem [Nhập kho](nhap-kho.md)) |
| Phiếu xuất **chưa đủ 6 bước / chưa Validate** | Hoàn tất quy trình xuất rồi Validate (xem [Xuất kho](xuat-kho.md)) |
| Nhầm **vị trí** hoặc **lô/serial** | Kiểm tra vị trí nguồn/đích, đếm lại theo lô |
| Hư hỏng / mất mát chưa ghi nhận | Điều chỉnh tồn kèm ghi chú lý do |

Xem lại: [4. Tồn kho](ton-kho.md) · [Tổng quan Kho](index.md)
