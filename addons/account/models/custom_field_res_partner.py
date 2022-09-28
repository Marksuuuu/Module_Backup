from odoo import fields, models, api


class CustomFieldResPartner(models.Model):
    _inherit = 'res.partner'

    contact_person = fields.Char('Contact Person', required=True)
    position = fields.Char('Position', required=True)
    permit_no = fields.Integer('Permit Number')
