    
# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, exceptions, _
from datetime import datetime, timedelta
from odoo.http import request
from odoo import api, fields, models, _

from odoo.exceptions import ValidationError

                
class crm_type_contrat(models.Model):
    _inherit = 'crm.lead'
    
    nom_contrat = fields.Char("Désignation", related="contrat_id.nom_contrat")
    seuil_min_contrat = fields.Float("Seuil minimum", related="contrat_id.seuil_min")
    status_contrat = fields.Selection([
       ('actif', 'Actif'),
       ('inactif', 'Inactif'),
    ], string='Status contrat', related="contrat_id.status_contrat")
    
    active_ferme_contrat = fields.Boolean()

    vrai_contrat = fields.Boolean('vrai', default=True)
    
    @api.onchange('contrat_id')
    def _onchange_status_ferme_contrat(self):
        for r in self:
            if (self.status_contrat) == 'inactif':
                r.active_ferme_contrat = True
            else:
                r.active_ferme_contrat = False
                
                       
    @api.constrains('active_ferme_contrat', 'vrai_contrat', 'nom_contrat')
    def _check_something_status_contrat(self):
        for record in self:
            if record.active_ferme_contrat == record.vrai_contrat:
                raise ValidationError(" le contrat " + str(record.nom_contrat) + " est désactivé")
                
    apport_min = fields.Monetary('Apport initial minimum', 'currency_id', defaul=5000, compute='_apport')
    
 
    #apport minimum
    #@api.onchange('prix_vente', 'seuil_min_contrat')
    #def _apport(self):
     #   for r in self:
      #      r.apport_min = (r.prix_vente*r.seuil_min_contrat)/100             
    