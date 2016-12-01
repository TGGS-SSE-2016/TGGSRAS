from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasBuilding(models.Model):
    _name = 'tggsras.building'

    company = fields.Many2one(
            'res.partner', ondelete='set null', string="Company", index=True)

    invoicedate = fields.Date(
        string="Invoice Date", default=fields.Date.today)

    billdate = fields.Date(
        string="Bill Date", default=fields.Date.today)

    cost  = fields.Integer(
        string="Cost(Baht)", help="Fill cost of renting")

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
