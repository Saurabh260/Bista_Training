from odoo import models, fields, api, _


class designation(models.Model):
    _name = 'trainee.designation'
    _description = 'Designation'

    _rec_name = 'des_name'
    des_name = fields.Char(string="Name", required=True)