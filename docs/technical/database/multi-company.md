# Multi-company (kỹ thuật)

## Mô hình dữ liệu

- Mỗi `res.company` — bản ghi công ty
- Hầu hết model nghiệp vụ có `company_id` hoặc `company_ids`
- User có `company_ids` + `company_id` (công ty hiện tại)

## Record rules

Rule `['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]` lọc dữ liệu theo user.

## Inter-company

Module `sale_purchase_inter_company_rules` — SO bên A tạo PO bên B (cần cấu hình).

## Kế toán

Mỗi công ty có chart of accounts, journal riêng — consolidated reporting cần module/accounting config.

Phía người dùng: [Công ty & chi nhánh](../../cai-dat/cong-ty.md) (tab Chức năng).
