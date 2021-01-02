from odoo import models, fields, api, _


class Subjects(models.Model):
    _name = 'training.subjects'
    _description = 'Training Subjects'

    _rec_name = 'sub_name'
    sub_name = fields.Char(string="Name", required=True)
    desc = fields.Html(string="Description")
    sub_topic = fields.One2many('training.topics', 'subject_name', string="Subject Topic",
                                  help='Trainer Field')
    sub_trainer = fields.Many2many('trainer.trainer', string="Trainers",
                                  help='Trainer Field')
    color = fields.Integer('Color Index', default=0)
