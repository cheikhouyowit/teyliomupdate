    
# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, exceptions, _
from datetime import datetime, timedelta
from odoo.http import request
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import re

from datetime import date
from dateutil.relativedelta import relativedelta
_
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo.osv import expression
from odoo.tools import float_compare, pycompat
from odoo.addons import decimal_precision as dp

from odoo.exceptions import ValidationError


class type_Contrat(models.Model):
    _inherit = 'lb.contrat'
    seuil_min = fields.Float("Seuil minimum", requered="1")
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)
    projet_id = fields.Many2one('lb.projet', String='Projet lier')
   

    