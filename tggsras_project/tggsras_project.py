from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasProject(models.Model):
    _name = 'tggsras.project'
    _inherit = 'mail.thread'

    name = fields.Char(string="Name", required=True,help="Fill your project name")

    interval_number = fields.Integer(string="Interval Number", help="Fill in progress interval number")

    interval_type = fields.Selection([
        ('day', "Day"),
        ('week', "Week"),
        ('month', "Month"),
        ('year', "Year"),
    ])

    progress_id = fields.One2many('tggsras.project.progress','project_id', string="Progress")

    customer = fields.Char(string="Customer Name",
                           required=True, help="Fill your customer name", )

    fundowner = fields.Many2one(
        'res.users', ondelete='set null', string="Fund Owner", index=True)

    expect_startdate = fields.Date(
        string="Start Date", default=fields.Date.today)

    expect_enddate = fields.Date(
        string="Stop Duration", default=fields.Date.today)

    estimated_income = fields.Float(
        string="Estimated Income", help="Fill your estimated income")

    estimated_expense = fields.Float(
        string="Estimated Expense", help="Fill your estimated expense")

    tor = fields.Many2many(
                            string="TOR file",
                            comodel_name='tggsras.project.file',
                            relation='tggsras_project_file_rel',
                            column1='project_id',
                            column2='project_file_id')

    contract = fields.Many2many(
                            string="Contract file",
                            comodel_name='tggsras.project.file',
                            relation='tggsras_project_file_rel',
                            column1='project_id',
                            column2='project_file_id')

    permission = fields.Many2many(
                            string="Permission file",
                            comodel_name='tggsras.project.file',
                            relation='tggsras_project_file_rel',
                            column1='project_id',
                            column2='project_file_id')

    project_proposal = fields.Many2many(
                            string="Project Proposal file",
                            comodel_name='tggsras.project.file',
                            relation='tggsras_project_file_rel',
                            column1='project_id',
                            column2='project_file_id')

    # tor = fields.Binary(string="TOR file",help="Upload TOR file here")
    #
    # tor_filename = fields.Char(string="TOR file name")
    #
    # contract = fields.Binary(string="Contract file",help="Upload Contract file here")
    #
    # contract_filename = fields.Char(string="Contract file name")
    #
    # permission = fields.Binary(string="Permission file",help="Upload Contract file here")
    #
    # permission_filename = fields.Char(string="Permission file name")
    #
    # project_proposal = fields.Binary(string="Project Proposal file",help="Upload Project Proposal file here")
    #
    # project_proposal_filename = fields.Char(string="Proposal file name")

    objective = fields.Text()
    scope = fields.Text()
    description = fields.Text()
    expected_result = fields.Text()

    state = fields.Selection([
        ('draft', "Draft"),
        ('tor', "TOR"),
        ('accept', "accept"),
        ('contract', "Contract"),
        ('operation', "Operation"),
        ('progress', "Progress"),
        ('finish', "Finish"),
    ])

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The name of the project should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The project name must be unique"),
     ]

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_tor(self):
        self.state = 'tor'

    @api.multi
    def action_accept(self):
        self.state = 'accept'

    @api.multi
    def action_contract(self):
        self.state = 'contract'

    @api.multi
    def action_operation(self):
        self.state = 'operation'

    @api.multi
    def action_progress(self):
        self.state = 'progress'

    @api.multi
    def action_finish(self):
        self.state = 'finish'

    @api.onchange('expect_startdate', 'expect_enddate')
    def _startdate_before(self):
        fmt = '%Y-%m-%d'
        start = self.expect_startdate
        end = self.expect_enddate
        d1 = datetime.strptime(start, fmt)
        d2 = datetime.strptime(end, fmt)
        dayDiff = (d2-d1).days
        if dayDiff < 0:
            return {
                'warning': {
                    'title': _("Start Date should before End Date"),
                    'message': _("Your date Duration is : "+str(dayDiff)),
                },
            }
