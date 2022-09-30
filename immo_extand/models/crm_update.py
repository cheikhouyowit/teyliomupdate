

# -*- coding: utf-8 -*-
import string
from odoo import models, fields, api, tools, exceptions, _
from datetime import datetime, timedelta
from odoo.http import request
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

                
class crm_update(models.Model):
    _inherit = 'crm.lead'


    #@api.onchange('contrat_type')
    #def _check_contrat_status(self):
     #   for r in self:
      #       if (r.status_contrat) == 'inactif':       
       #          return {
        #            'warning': {
         #           'title': "Type de contrat inactif",
          #          'message': "Veuillez remplacer ce type de contrat svp",
           #        }}            
    
    contrat_projet_ids=fields.Many2many(related='nom_projet_ids.contrat_ids',String='contrat')
    contrat_type = fields.Many2one('lb.contrat',string="Type de contrat", required=True,
                            
                            domain="['&',('status_contrat','=','actif'),('company_id', '=',company_id),('projet_id', '=',nom_projet_ids)]")
    
    seuil_min_contrat = fields.Float("Seuil minimum", related="contrat_type.seuil_min")
    #apport minimum
    
    @api.onchange('prix_vente', 'seuil_min_contrat')
    def _apport(self):
        for r in self:
            r.apport_min = (r.prix_vente*r.seuil_min_contrat)/100      
    #status_related= fields.Selection(related='contrat_type.status_contrat', string='status')

    
    


  
    
