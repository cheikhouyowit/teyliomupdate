
from lxml import etree

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError
from odoo.tools.safe_eval import safe_eval
from odoo.addons import decimal_precision as dp
class projet_bien(models.Model):
    _inherit = 'lb.projet'
    _rec_name = 'nom_projet'
    
    #nom_projet = fields.Char(string="Nom du projet")
    contrat_ids = fields.Many2many('lb.contrat',string="contrat")
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)
    

    
#class modele_ilot(models.Model):
#    _inherit = 'lb.ilot'
 #   _rec_name = 'name_ilot'
    
    
  #  projet_id = fields.Many2one('lb.projet',String="type de contrat", required=True)


     