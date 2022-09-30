# -*- coding: utf-8 -*-
{
    'name': "immobilier_update_2",

    'summary': """
          Mise a jour module pour ajout de nouvelles fonctionnalites
         """,

    'description': """
        #Tache1 lors de la création du contact le nom du commercial doit venir automatiquement dans le champ "vendeur", il ne doit pas sélectionner, par contre pour le marketing ça sera un choix suivant la liste déroulante
        #Tache2 Le statut du prospect doit changer automatiquement en client au niveau du module contact lorsque sur sa fiche d'opportunité, le montant de l'apport versé est supérieur ou l’égal au montant de l'apport minimum
    """,

    'author': "Moore Senegal",
    'website': "http://www.mooresenegal.sn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/views_contact_update.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
