from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasFile(models.Model):
    _name = 'tggsras.file'

    name = fields.Char(string="File Name",help="Fill your file name", )

    filedata = fields.Binary(string="File data",help="Upload file here")

    @api.one
    def deleteFile(self):
        self.unlink()
