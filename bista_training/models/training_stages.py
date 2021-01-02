# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class training_stages(models.Model):
    _name = 'training_stages.training_stages'
    _description = 'Trainer Stages'

    _rec_name = 'training_stages_name'
    training_stages_name = fields.Char(string="Name")
    training_batch = fields.Boolean('Batch')
    training_record = fields.Boolean('Training Record')

    # def action_stages(self):             , compute='action_stages'
    #     for rec in self:
    #         if rec.training_batch == True:
    #             stages = {
    #                 'states': rec.training_stages_name,
    #             }
    #             self.states = self.env['trainee_batch.trainee_batch'].create(stages)