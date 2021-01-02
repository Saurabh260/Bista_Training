from odoo import models, fields, api, _


class Topics(models.Model):
    _name = 'training.topics'
    _description = 'Training Topics'

    _rec_name = 'top_name'
    top_name = fields.Char(string="Topics Name", required=True)

    # calling Many2one subjects field from subject models
    subject_name = fields.Many2one('taining.subject', string="Subject", readonly=True,
                                        help='Trainer Field')