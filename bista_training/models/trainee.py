# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class bista_training(models.Model):
    _name = 'bista_training.bista_training'
    _description = 'Bista Training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _inherit = {'hr.employee': 'employed_id'}

    image = fields.Binary(string="Image", tracking=True)
    name = fields.Char(compute='_compute_name', store="True", tracking=True)
    firstname = fields.Char(string="First Name", required=True)
    lastname = fields.Char(string="Last Name")
    seq_name = fields.Char(string='Trainee ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('ID'))
    email = fields.Char("Email", required=1, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=1)
    dob = fields.Date(string="Date Of Birth", help="Date of Birth")
    doj = fields.Date(string="Date Of Joining", help="Date of Joining", tracking=True)
    # linking field of designation in trainee model
    trainee_des = fields.Many2one('trainee.designation', string="Designation",
                                  help='Designation Field', tracking=True)
    trainee_loc = fields.Many2one('trainee.location',string="Location",
                                  help='Location Field', tracking=True)
    employee_id = fields.Many2one('hr.employee', string="Employee")

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
        ('4', 'Extreme High')], string='Priority',
        index=True)


#creating different state for status bar:-
    state = fields.Selection([('new', 'New'),
                              ('training', 'Training'),
                              ('rejected', 'Rejected'),
                              ('employed', 'Employed')],
                             string="Status", tracking=True, default='new')


 # Function for Dupicate Method :-
    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     default = dict(default or {})
    #     default.update(
    #         name=_("%s (copy)") % (self.name or ''))
    #     return super(bista, self).copy(default)
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            email=_("%s (copy)") % (self.email or ''))
        return super(bista_training, self).copy(default)


#defining action function for training button:-
    def confirm(self):
        for rec in self:
            rec.state = "training"

#defining action function for rejected button:-
    def action_rejected(self):
        for rec in self:
            rec.state = "rejected"

 #defining action function for employed button:-
    def action_employed(self):
        for rec in self:
            #when we press employed button the data get added into hr.employee
            employee_details = {
                'name': rec.name,
                'image_1920': rec.image,
                'is_trainee': True
            }
            employee = self.env['hr.employee'].create(employee_details)
            rec.employee_id = employee
            rec.state = "employed"
            # employee.create(employee_details)



 #Creating function to add first name and last name:-
    @api.depends('firstname', 'lastname')
    def _compute_name(self):
        for record in self:
            record.name = str(record.firstname or '') + ' ' +  str(record.lastname or '')


 #Creating function for unique sequence number
 #where fields is 'seq_name' and also mention in the views:-
    @api.model
    def create(self, vals):
        if vals.get('seq_name', _('New')) == _('New'):
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('bista_training.seq') or _('New')
        result = super(bista_training, self).create(vals)
        return result

 #Creating unique 'Email id' using sql constraints:-
    _sql_constraints = [
        ('email_uniq',
         'unique(email)',
         'Email Id should be unique')
    ]

 # #Creating unique 'Name' using function constraints
 #    @api.constrains('name')
 #    def check_name(self):
 #        for record in self:
 #            obj = self.search([('name', '=', record.name), ('id', '!=', record.id)])
 #            if obj:
 #                raise ValidationError(_('Name Already exist'))



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
