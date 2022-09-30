    
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
   
    nom_contrat = fields.Char("Désignation")
    seuil_min = fields.Float("Seuil minimum", requered="1")
    status_contrat = fields.Selection([
       ('actif', 'Actif'),
        ('inactif', 'Inactif'),
    ], string='Status contrat')

    