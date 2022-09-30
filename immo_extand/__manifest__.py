# -*- coding: utf-8 -*-
{
    'name': "immo Extand",

    'summary': """crm- immo
        Extenssion de immobilier ,Nouvelle fonctionnalite Optesis-CTD""",

    'description': """
        PROJet immobilier ,contrat type immobilier ,ilot immobilier, crm 
        transforme et ajoute de nouvelle fonction sur la disposition des element,
        les conditions lies entres projet et type de contrat et les dependence
        du societe lier a ce projet ,contrat et ilot..
        gestion des status actif et inactif
    """,

    'author': "Moore Senegal",
    'website': "https://www.moore.sn",

    
    'category': 'uncategorized',
    'version': '0.1',

   
    'depends': ['base','product','crm', 'immobilier','type_contrat','immo_update'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/biens_view_update.xml',
        'views/crm_update.xml',
        'views/type_contrat_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
