from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasBuildingFile(models.Model):
    _name = 'tggsras.building.file'
    _inherit = 'tggsras.file'
