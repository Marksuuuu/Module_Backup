from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'stock.reject'
    _description = 'Rejected Data'
    _inherit = ['stock.scrap']



