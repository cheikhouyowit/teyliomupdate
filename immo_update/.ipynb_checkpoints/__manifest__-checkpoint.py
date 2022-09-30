# -*- coding: utf-8 -*-
{
    'name': "immo_update",

    'summary': """
        Mise a jour model bien et crm """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Moore Senegal",
    'website': "moore.sn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','product','crm', 'immobilier'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/biens_view_update.xml',
        'views/crm_update.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
