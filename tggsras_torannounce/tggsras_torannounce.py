from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasTorannounce(models.Model):
    _name = 'tggsras.torannounce'
    _inherit = 'mail.thread'
