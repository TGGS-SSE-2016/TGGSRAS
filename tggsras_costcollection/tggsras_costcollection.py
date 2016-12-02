from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasCostcollection(models.Model):
    _name = 'tggsras.costcollection'

    company = fields.Many2one(
            'res.partner', ondelete='set null', string="Company", index=True, required=True)

    invoicedate = fields.Date(
        string="Invoice Date", default=fields.Date.today)

    billdate = fields.Date(
        string="Bill Date", default=fields.Date.today)

    cost  = fields.Integer(
        string="Cost(Baht)", help="Fill cost of renting")

    name = fields.Char(string="Name", compute='_gen_name')

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
