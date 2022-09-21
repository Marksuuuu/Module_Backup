from odoo import fields, models, api


class RejectTypeCodes(models.Model):
    _name = 'reject.types'
    _description = 'Description'

    reject_type = fields.Char(string='Reject Types')
    reject_codes = fields.Char(string='Reject Codes')
