# Phân quyền kỹ thuật

## Ba lớp bảo mật Odoo

| Lớp | File / UI | Mô tả |
|-----|-----------|--------|
| **Groups** | `security.xml` | User thuộc nhóm nào |
| **Access Rights** | `ir.model.access.csv` | CRUD trên model |
| **Record Rules** | `ir.rule` XML | Domain lọc từng dòng |

## ir.model.access.csv

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,base.group_user,1,1,1,0
```

## Record rule ví dụ

Chỉ xem SO của mình:

```xml
<record id="sale_order_personal_rule" model="ir.rule">
    <field name="name">Personal Orders</field>
    <field name="model_id" ref="sale.model_sale_order"/>
    <field name="domain_force">[('user_id','=',user.id)]</field>
    <field name="groups" eval="[(4, ref('sales_team.group_sale_salesman'))]"/>
</record>
```

## sudo() — cẩn trọng

Code `record.sudo()` bỏ qua rules — chỉ dùng khi thật sự cần và đã kiểm tra logic.

Phía nghiệp vụ: [Quyền truy cập](../../cai-dat/quyen-truy-cap.md) (Chức năng).
