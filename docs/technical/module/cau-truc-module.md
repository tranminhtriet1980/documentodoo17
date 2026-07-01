# Cấu trúc module (addon)

## Khung thư mục

```
my_module/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── my_model.py
├── views/
│   └── my_model_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
├── data/
│   └── data.xml
└── static/
    └── description/
        └── icon.png
```

## __manifest__.py

```python
{
    'name': 'My Module',
    'version': '17.0.1.0.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'application': False,
}
```

## Model Python (ví dụ)

```python
from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
```

## View XML (ví dụ)

```xml
<record id="view_my_model_tree" model="ir.ui.view">
    <field name="name">my.model.tree</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
        </tree>
    </field>
</record>
```

## Cài module custom

1. Đặt thư mục trong `addons_path`
2. **Apps › Update Apps List**
3. Tìm module → Install

Xem: [Developer mode](developer-mode.md) | [Nâng cấp module](nang-cap-module.md)
