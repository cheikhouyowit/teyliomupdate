

from lxml import etree

from odoo import api, fields, models, tools, SUPERUSER_ID, _



class modele_acticle(models.Model):
    _inherit = 'product.template'
 
    
    
    ilot_ids = fields.Many2one('lb.ilot', string="Ilot",
            domain="[('projet_id', '=',nom_projet_ids)]")
    phase_ids = fields.Many2one('lb.phase', string="Phase")
    
    
    

    
class modele_ilot(models.Model):
    _name = 'lb.ilot'
    _description = "ilot"
    _rec_name = 'name_ilot'

    name_ilot = fields.Char('Ilot')
    
    status_ilot = fields.Selection([
       ('dispo', 'Disponible pour la vente'),
        ('ferme', 'Fermé'),
    ], string='Etat ilot')
    
    date_debut = fields.Date('Date debut')
    date_fin_ilot = fields.Date('Date fin')
    #by optesis-cheikh tidiane add dependence projet in ilot for crm lead domain
    projet_id = fields.Many2one('lb.projet',String="type de contrat", required=True) 


class modele_phase(models.Model):
    _name = 'lb.phase'
    _description = "Phase"
    _rec_name = 'name_phase'

    name_phase = fields.Char('Phase')
   

