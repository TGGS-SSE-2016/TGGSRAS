from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasSupply(models.Model):
    _name = 'tggsras.supply'
    _inherit = 'tggsras.costcollection'
