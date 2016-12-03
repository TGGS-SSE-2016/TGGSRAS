from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasBuilding(models.Model):
    _name = 'tggsras.building'
    _inherit = 'tggsras.costcollection'

    @api.depends('company', 'invoicedate')
    def _gen_name(self):
        for r in self:
            my_date = parser.parse(r.invoicedate)
            proper_date_string = my_date.strftime('%Y%m%d')
            r.name = 'INVBUI'+proper_date_string+str(r.company.id)
