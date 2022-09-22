from odoo import fields, models, api


class DataUpload(models.Model):
    _name = 'data.upload.here'
    _description = 'Data Upload Module'

    name = fields.Char(string='Uploader')
    title = fields.Char(string='Item Name', required=True)
    file = fields.Binary(string='File Uploaded')
