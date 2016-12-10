from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasTorannounceFile(models.Model):
    _name = 'tggsras.torannounce.file'
    _inherit = 'tggsras.file'

    
