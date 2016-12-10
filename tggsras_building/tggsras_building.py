from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasBuilding(models.Model):
    _name = 'tggsras.building'
    _inherit = 'tggsras.costcollection'

    signedinvoice = fields.Many2many(
                            string="Signed Invoice file"
                            comodel_name='tggsras.building.file',
                            relation='tggsras_building_file_rel',
                            column1='building_id',
                            column2='building_file_id')


    signedbill = fields.Many2many(
                            string="Signed Bill file"
                            comodel_name='tggsras.building.file',
                            relation='tggsras_building_file_rel',
                            column1='building_id',
                            column2='building_file_id')


    @api.depends('company', 'invoicedate')
    def _gen_name(self):
        for r in self:
            my_date = parser.parse(r.invoicedate)
            proper_date_string = my_date.strftime('%Y%m%d')
            r.name = 'INVBUI'+proper_date_string+str(r.company.id)
