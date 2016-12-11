from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasProjectProgressFile(models.Model):
    _name = 'tggsras.project.progress.file'
    _inherit = 'tggsras.file'
