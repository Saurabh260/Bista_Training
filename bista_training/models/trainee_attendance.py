# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, _



class trainee_attendance(models.Model):
    _name = 'trainee_attendance.trainee_attendance'
    _description = 'Trainee Attendance'

    _rec_name = 'trainee_attendance_name'
    trainee_attendance_date = fields.Date(string="Date", default=fields.Date.today, readonly=True)
    trainee_attendance_name = fields.Char(compute='_compute_date', string="Name")
    trainee_name = fields.Many2one('bista.bista', string="Trainee")
    login_time = fields.Datetime(string="Login Time")
    logout_time = fields.Datetime(string="Logout Time")
    hours = fields.Float(string="Hours")

    # _defaults = {'login_time': lambda *a: time.strftime('%Y-%m-%d-00-00-00'), }

    # , default = fields.datetime.now().time()
    # training_record = fields.Boolean('Training Record')                    compute='_compute_time',
    @api.depends('trainee_attendance_date')
    def _compute_date(self):
        for record in self:
            record.trainee_attendance_name = 'Training Attendance Record of <' + str(record.trainee_attendance_date or '') +'>'

    # @api.depends('login_time', 'logout_time', 'hours')                       , compute='_compute_time'
    # def _compute_time(self):
    #             if self.login_time and self.logout_time:
    #                 start = datetime.strptime(self.login_time, '%m/%d/%Y %H:%M:%S')
    #                 end = datetime.strptime(self.logout_time, '%m/%d/%Y %H:%M:%S')
    #                 hour = start - end
    #                 self.hours = float(hour.days) * 24 + (float(hour.seconds) / 3600)
    # #                 # hour = re.sub('[^0-9]', '', str(real))
    # #                 # r.hours = (int(hour))# / 100000

    # @api.depends('login_time')
    # def _compute_time(self):
    #     for r in self:
    #         if r.hours and r.login_time:
    #             dt = datetime.datetime.strftime(r.login_time, "%d/%m/%Y %H:%M:%S")
    #             r.hours = dt.strftime("%H:%M:%S")

