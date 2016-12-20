from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasTorannounce(models.Model):
    _name = 'tggsras.torannounce'
    _inherit = 'mail.thread'

    name = fields.Char(string="Name", required=True,
                       help="Fill your project name")

    fundowner = fields.Many2one(
        'res.users', ondelete='set null', string="Fund Owner", index=True)

    poster = fields.Many2many(
                            string="Signed Invoice file",
                            comodel_name='tggsras.torannounce.file',
                            relation='tggsras_torannounce_file_rel',
                            column1='torannounce_id',
                            column2='torannounce_file_id')

    description = fields.Text()


    duedate = fields.Date(
        string="Due Date", default=fields.Date.today)

    def torannounce_notify(self, cr, uid, context=None):
        return None
