# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, _



class trainee_batch(models.Model):
    _name = 'trainee_record.trainee_record'
    _description = 'Trainee Record'

    _rec_name = 'trainee_record_name'
    trainee_record_date = fields.Date(string="Date", default=fields.Date.today, readonly=True)
    trainee_record_name = fields.Char(compute='_compute_batch_date', string="Name")
    trainee_batch = fields.Many2one('trainee_batch.trainee_batch', string="Batch")
    stage_id = fields.Many2one('training_stages.training_stages', string="Stages")
    # login_time = fields.Datetime(string="Login Time")
    # logout_time = fields.Datetime(string="Logout Time")
    # hours = fields.Float(string="Hours", compute='_compute_time')

    # _defaults = {'login_time': lambda *a: time.strftime('%Y-%m-%d-00-00-00'), }

    # , default = fields.datetime.now().time()
    # training_record = fields.Boolean('Training Record')                    compute='_compute_time',
    @api.depends('trainee_record_date')
    def _compute_batch_date(self):
        for record in self:
            record.trainee_record_name = 'Training Record of <' + str(record.trainee_record_date or '') +'>'

    # @api.depends('login_time', 'logout_time', )
    # def _compute_time(self):
    #         for r in self:
    #             if r.hours and r.logout_time:
    #                 start = datetime.datetime.strftime(r.login_time, '%H:%M:%S')
    #                 end = datetime.datetime.strftime(r.logout_time, '%H:%M:%S')
    #                 r.hours = start - end
    #                 # hour = re.sub('[^0-9]', '', str(real))
    #                 # r.hours = (int(hour))# / 100000

    # @api.depends('login_time')
    # def _compute_time(self):
    #     for r in self:
    #         if r.hours and r.login_time:
    #             dt = datetime.datetime.strftime(r.login_time, "%d/%m/%Y %H:%M:%S")
    #             r.hours = dt.strftime("%H:%M:%S")

