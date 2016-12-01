from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasBuilding(models.Model):
    _name = 'tggsras.building'
    _inherit = 'tggsras.costcollection'
