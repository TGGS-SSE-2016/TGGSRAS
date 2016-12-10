from datetime import datetime, timedelta
from dateutil import parser
from openerp import models, fields, api, exceptions, _


class TggsrasProjectProgress(models.Model):
    _name = 'tggsras.project.progress'
    _inherit = 'mail.thread'

    project_id = fields.many2one('tggsras.project', ondelete='cascade', string="Project Name", index=True)
    description = fields.Text()
    duedate = fields.Date(string="Due Date", default=fields.Date.today)
    progress_file = fields.many2many(
        string="Progress file"
        comodel_name='tggsras.project.progress.file',
        relation='tggsras_project_progress_file_rel',
        column1='project_progress_id',
        column2='project_progress_file_id')
    state = fields.Selection([
        ('draft', "Draft"),
        ('send', "Send"),
        ('approved', "Approved"),
    ])
