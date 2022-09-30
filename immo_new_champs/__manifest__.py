# -*- coding: utf-8 -*-
{
    'name': "immo_new_champs",

    'summary': """
        MAJ Module bien""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Moore Senegal",
    'website': "http://moore.sn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
     'depends': ['base','product','crm', 'immobilier'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
         'views/bien_new.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
