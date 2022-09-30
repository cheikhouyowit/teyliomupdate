#new funtion by CTD
    
# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, exceptions, _
from datetime import datetime, timedelta
from odoo.http import request
from odoo import api, fields, models, _

from odoo.exceptions import ValidationError

#by CTD   -immo-Extand dependences             
class crm_update(models.Model):
    _inherit = 'crm.lead'  
    


  
    superficie = fields.Float(related='bien.superficie')
    
    phase_ids = fields.Many2one(related='bien.phase_ids')
    
    
    ilot_ids = fields.Many2one('lb.ilot', string='ilot', domain="['&',('status_ilot','=','dispo'),('projet_id', '=',nom_projet_ids)]")
    
    
    status_ilot = fields.Selection([
       ('dispo', 'Disponible pour la vente'),
        ('ferme', 'Fermé'),
    ], string='Etat ilot',related='ilot_ids.status_ilot')
    
    date_debut_ilot = fields.Date('Date debut', related='ilot_ids.date_debut')
    date_fin_ilot = fields.Date('Date fin' , related='ilot_ids.date_fin_ilot') 
    
    active_dispo_ilot = fields.Boolean()

    active_ferme_ilot = fields.Boolean()

    vrai = fields.Boolean('vrai', default=True)
    

    @api.onchange('status_ilot')
    def _onchange_status_dispo(self):
        for r in self:
            if (self.status_ilot) == 'dispo':
                r.active_dispo_ilot = True
            else:
                r.active_dispo_ilot = False

    @api.onchange('etat_du_bien')
    def _onchange_status_ferme(self):
        for r in self:
            if (self.status_ilot) == 'ferme':
                r.active_ferme_ilot = True
            else:
                r.active_ferme_ilot = False
                 
                    
    @api.constrains('active_ferme_ilot', 'vrai')
    def _check_something_status_ilot(self):
        for record in self:
            if record.active_ferme_ilot == record.vrai:
                raise ValidationError("Ce bien n'est pas dispo pour la vente")
                
                
                 
    @api.constrains('date_livraison', 'date_debut_ilot', 'date_fin_ilot')
    def _check_something_date_livraison_debuts(self):
        for record in self:
            if record.bien:
                if record.date_debut_ilot > record.date_livraison:
                    raise ValidationError("la date de livraison doit etre compris entre " + str(record.date_debut_ilot) + " et " + str(record.date_fin_ilot))  

    @api.constrains('date_livraison', 'date_debut_ilot', 'date_fin_ilot')
    def _check_something_date_livraison_fin(self):
        for record in self:
            if record.bien:
                if record.date_livraison > record.date_fin_ilot:
                     raise ValidationError("la date de livraison doit etre compris entre " + str(record.date_debut_ilot) + " et " + str(record.date_fin_ilot))  
