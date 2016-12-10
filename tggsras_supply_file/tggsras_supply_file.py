from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasSupplyFile(models.Model):
    _name = 'tggsras.Supply.File'
    _inherit = 'tggsras.file'
