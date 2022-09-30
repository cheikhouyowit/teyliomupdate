from odoo import fields, api, models



class ContactUpdate(models.Model):
   
    _inherit="res.partner"



    user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)


# salesperson=fields.fields.Char(
#     default=lambda self: self.user.id,
# )



