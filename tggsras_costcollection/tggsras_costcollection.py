from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasCostcollection(models.Model):
    _name = 'tggsras.costcollection'
    _inherit = 'mail.thread'

    company = fields.Many2one(
            'res.partner', ondelete='set null', string="Company", index=True, required=True)

    invoicedate = fields.Date(
        string="Invoice Date", default=fields.Date.today)

    invoicemonth = fields.Integer(string="Month",compute='_get_month')

    billdate = fields.Date(
        string="Bill Date", default=fields.Date.today)

    cost  = fields.Integer(
        string="Cost(Baht)", help="Fill cost of renting")

    name = fields.Char(string="Name", compute='_gen_name', store=True)

    # signedinvoice = fields.Binary(string="Signed Invoice file",help="Upload signed invoice file here")
    #
    # signedinvoice_filename = fields.Char(string="Signed Invoice file name")
    #
    # signedbill = fields.Binary(string="Signed Bill file",help="Upload signed bill file here")
    #
    # signed_bill_filename = fields.Char(string="Signed Bill file name")

    state = fields.Selection([
        ('invoice', "Invoice"),
        ('send', "Send"),
        ('paid', "Paid"),
        ('bill', "Bill"),
        ('close', "close"),
    ])


    @api.multi
    def action_invoice(self):
        self.state = 'invoice'

    @api.multi
    def action_send(self):
        self.state = 'send'

    @api.multi
    def action_paid(self):
        self.state = 'paid'

    @api.multi
    def action_bill(self):
        self.state = 'bill'

    @api.multi
    def action_close(self):
        self.state = 'close'

    @api.depends('company', 'invoicedate')
    def _gen_name(self):
        for r in self:
            my_date = parser.parse(r.invoicedate)
            proper_date_string = my_date.strftime('%Y%m%d')
            r.name = proper_date_string+str(r.company.id)
    def _get_month(self):
        for r in self:
            fmt = '%Y-%m-%d'
            d = datetime.strptime(r.invoicedate, fmt)
            r.invoicemonth = d.month

    @api.constrains('name','company','invoicemonth')
    def _check_unique_name(self):
        for r in self:
            name_check = len(self.search([('name', '=', r.name)]))
            company_check = len(self.search([('company', '=', r.company.id)]))
            month_check = len(self.search([('invoicemonth','=', r.invoicemonth)]))
            if (name_check > 1) and (company_check > 1) and (month_check > 1):
                raise exceptions.ValidationError("Company/Name/Month already exists and violates unique field constraint")
