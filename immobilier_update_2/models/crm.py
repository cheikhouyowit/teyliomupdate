from odoo import fields, api, models, _

class CrmUpdate(models.Model):
    _inherit = 'crm.lead'

    @api.onchange('etat')
    def onchange_prospect_partner(self):
        for i in self:
            if i.etat == 'reserve':
                i.partner_id.prospect = False
            else:
                i.partner_id.prospect = True


 

