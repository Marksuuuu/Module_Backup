from odoo import fields, models, api


class StockRejectedType(models.Model):
    _name = 'stock.rejected.type'
    _description = 'Stock Rejected Type'

    reject_for_types = fields.Char(string='Rejected Types')
