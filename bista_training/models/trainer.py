# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class trainer(models.Model):
    _name = 'trainer.trainer'
    _description = 'Bista Trainer'

    _rec_name = 'trainer_name'


    trainer_name = fields.Char(compute='_trainer_name', store="True")
    trainer_image = fields.Binary(string="Image")
    trainer_firstname = fields.Char(string="First Name", required=True)
    trainer_lastname = fields.Char(string="Last Name")
    color = fields.Integer('Color Index', default=0)

    #Creating function to add first name and last name:-
    @api.depends('trainer_firstname', 'trainer_lastname')
    def _trainer_name(self):
        for record in self:
            record.trainer_name = str(record.trainer_firstname or '') + ' ' + str(record.trainer_lastname or '')
