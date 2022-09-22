from odoo import fields, models, api


class RejectCodes(models.Model):
    _name = 'reject.codes.types'
    _description = 'Reject Codes'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    reject_type_codes = fields.Char(string="Reject Code", tracking=True)
    reject_type = fields.Char(string="Reject Type Name", tracking=True)



    # reject_type_codes = fields.Selection([
    #  ('BBU', 'BBU'),
    #  ('BU', 'BU'),
    #  ('CHD', 'CHD'),
    #  ('CHO', 'CHO'),
    #  ('COP', 'COP'),
    #  ('CR', 'CR'),
    #  ('CRSC', 'CRSC'),
    #  ('CS', 'CS'),
    #  ('DBP', 'DBP'),
    #  ('DCH', 'DCH'),
    #  ('DCS', 'DCS'),
    #  ('DDB', 'DDB'),
    #  ('DF', 'DF'),
    #  ('DIF', 'DIF'),
    #  ('DiscB', 'DiscB'),
    #  ('DiscL', 'DiscL'),
    #  ('DiscP', 'DiscP'),
    #  ('DLD', 'DLD'),
    #  ('DLDS', 'DLDS'),
    #  ('DTD', 'DTD'),
    #  ('DVCE', 'DVCE'),
    #  ('DVDS', 'DVDS'),
    #  ('DVSD', 'DVSD'),
    #  ('ECB', 'ECB'),
    #  ('ED', 'ED'),
    #  ('EW', 'EW'),
    #  ('FMP', 'FMP'),
    #  ('GenFail', 'GenFail'),
    #  ('IMK', 'IMK'),
    #  ('IS', 'IS'),
    #  ('ISM', 'ISM'),
    #  ('LB', 'LB'),
    #  ('MC', 'MC'),
    #  ('MCAP', 'MCAP'),
    #  ('MisC', 'MisC'),
    #  ('MR', 'MR'),
    #  ('MS', 'MS'),
    #  ('NS', 'NS'),
    #  ('PB', 'PB'),
    #  ('POD', 'POD'),
    #  ('PR', 'PR'),
    #  ('SBL', 'SBL'),
    #  ('SDS', 'SDS'),
    #  ('STBP', 'STBP'),
    #  ('WB', 'WB'),
    #  ('WP', 'WP')], string='Reject Type')
