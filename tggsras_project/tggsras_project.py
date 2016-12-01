from datetime import datetime, timedelta
from openerp import models, fields, api, exceptions, _


class TggsrasProject(models.Model):
    _name = 'tggsras.project'

    name = fields.Char(string="Name", required=True,
                       help="Fill your project name", )
    customer = fields.Char(string="Customer Name",
                           required=True, help="Fill your customer name", )
    responsible = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    expect_startdate = fields.Date(
        string="Start Date", default=fields.Date.today)
    expect_enddate = fields.Date(
        string="Stop Duration", default=fields.Date.today)
    estimated_income = fields.Float(
        string="Estimated Income", help="Fill your estimated income")
    estimated_expense = fields.Float(
        string="Estimated Expense", help="Fill your estimated expense")

    tor = fields.Binary(string="TOR file",help="Upload TOR file here")

    tor_filename = fields.Char(string="TOR file name")

    contract = fields.Binary(string="Contract file",help="Upload Contract file here")

    contract_filename = fields.Char(string="Contract file name")

    permission = fields.Binary(string="Permission file",help="Upload Contract file here")

    permission_filename = fields.Char(string="Permission file name")

    project_proposal = fields.Binary(string="Project Proposal file",help="Upload Project Proposal file here")

    project_proposal_filename = fields.Char(string="Proposal file name")

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
