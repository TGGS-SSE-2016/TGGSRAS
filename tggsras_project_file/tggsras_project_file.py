from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasProjectFile(models.Model):
    _name = 'tggsras.project.file'
    _inherit = 'tggsras.file'
