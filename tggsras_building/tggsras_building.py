from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasBuilding(models.Model):
    _name = 'tggsras.building'

    responsible = fields.Many2one(
            'res.users', ondelete='set null', string="Responsible", index=True)
