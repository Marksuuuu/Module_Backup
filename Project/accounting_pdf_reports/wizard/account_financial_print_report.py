from odoo import fields, models, api


class AccountFinancialReport(models.TransientModel):
    _name = 'account.financial.print.report'
    _inherit = 'account.common.partner.report'
    _description = ''

    Invoice_Date = fields.Datetime()
    name = fields.Char()
    PV = fields.Integer()
    Invoice = fields.Float()
    PO = fields.Integer()
    Amount = fields.Integer()
    Debit = fields.Integer()
    Credit = fields.Integer()
    account_no = fields.Integer()
    amm = fields.Integer()




    # journal_ids = fields.Many2many('account.journal', string='Journals', required=True)
    def print_here(self):
        data = {
            # 'model': 'account.financial.print.report',
            'form_data': self.read()[0]
        }
        return self.env.ref('accounting_pdf_reports.account_financial_print_report_rec').report_action(self,data=data)
