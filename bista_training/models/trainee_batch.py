# -*- coding: utf-8 -*-
from odoo import models, fields, api, _



class trainee_batch(models.Model):
    _name = 'trainee_batch.trainee_batch'
    _description = 'Trainee Batch'

    _rec_name = 'trainee_batch_name'
    trainee_batch_name = fields.Char(string="Batch Name")
    trainee_start_date = fields.Date(string="Start Date")
    trainee_end_date = fields.Date(string="End Date")
    trainee_batch_location = fields.Many2one('trainee.location', string="Trainee Location")
    trainee_names = fields.One2many('trainee_batch2.trainee_batch2', 'batch2_id', string="Trainees",
                                  help='Trainee Names')
    trainer_names = fields.One2many('trainer_batch2.trainer_batch2', 'co_model2', string="Trainers",
                                  help='Trainer Names')
    training_topics = fields.Many2many('training.topics', string="Trainers",
                                   help='Trainer Field')
    batch_stages = fields.Many2one('training_stages.training_stages', string="Stages")
    # # creating different state for status bar:-
    states = fields.Selection([('start', 'Start'),
                              ('end', 'End')],
                              string="Status", default='start')


    #         # rec.employee_id = employee

class trainee_batch_line(models.Model):
    _name = 'trainee_batch2.trainee_batch2'
    _description = 'Trainee Batch Line'

    traine_name_line = fields.Many2one('bista.bista', string='Name')
    # co_model = fields.Many2one('trainee_batch.trainee_batch', string='Co-Model')
    batch2_id = fields.Many2one('trainee_batch.trainee_batch', string='Co-Model')


class trainer_batch_line(models.Model):
    _name = 'trainer_batch2.trainer_batch2'
    _description = 'Trainer Batch Line'

    trainer_name_line = fields.Many2one('trainer.trainer', string='Name')
    co_model2 = fields.Many2one('trainee_batch.trainee_batch', string='Co-Model2')


