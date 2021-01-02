# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import pytz
from odoo.exceptions import ValidationError, AccessError

class HrEmployeePrivate(models.Model):
        # _name = "hr.employee"
        _inherit = "hr.employee"

        is_trainee = fields.Boolean('Trainee')
