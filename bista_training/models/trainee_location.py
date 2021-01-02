# For relation to default odoo state and contry master use this link:-
# https://stackoverflow.com/questions/44110307/load-country-state-city-depencency-in-odoo
from odoo import models, fields, api, _


class trainee_loc(models.Model):
    _name = 'trainee.location'
    _description = 'Trainee Location'

    _rec_name = 'loc_name'
    loc_name = fields.Char(string="Location Name", required=True)
    street1 = fields.Char(string="Street 1")
    street2 = fields.Char(string="Street 2")
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict', required=True)
    zip = fields.Char(string="ZIP")

    # Dependent picklist code to show State based on selected Country E.g India -> Gujarat, Maharastra, Rajasthan, etc..
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}
