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

    fundowner = fields.Many2one(
        'res.partner', ondelete='set null', string="Researcher Incharge", index=True)

    researcher_incharge_id = fields.Many2one(
        'res.partner', ondelete='set null', string="Researcher Incharge", index=True)

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

    objective = fields.Text(string="Objective",help="Please fill in project objective")
    scope = fields.Text(string="Scope",help="Please fill in project scope")
    description = fields.Text(string="Description",help=" Please fill in project description")
    expected_result = fields.Text(string="Expected Result",help="Please fill in project expected result")

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
        start = self.expect_startdate
        end = self.expect_enddate
        dayDiff = self.calLengthDays(start,end)
        if dayDiff < 0:
            return {
                'warning': {
                    'title': _("Start Date should before End Date"),
                    'message': _("Your date Duration is : "+str(dayDiff)),
                },
            }


    def progress_notify(self, cr, uid, context=None):
        tggsras_project_all = self.pool.get('tggsras.project')
        tggsras_project_progress_all = self.pool.get('tggsras.project.progress')
        #Contains all ids for the model scheduler.demo
        tggsras_project_all_ids = self.pool.get('tggsras.project').search(cr, uid, [])
        tggsras_project_progress_all_ids = self.pool.get('tggsras.project.progress').search(cr, uid, [])

        for tggsras_project_id in tggsras_project_all_ids:
            tggsras_project = tggsras_project_all.browse(cr, uid,tggsras_project_id ,context=context)
            incharge_id = tggsras_project.researcher_incharge_id
            name = tggsras_project.name
            interval_number = tggsras_project.interval_number
            interval_type = tggsras_project.interval_type

            newest_progress = self.search(cr, uid, [('project_id','=',tggsras_project_id)], limit=1, order='id desc')
            lastprogress_date = newest_progress.submitdate
            today = datetime.today()
            dayDiff = self.calLengthDays(lastprogress_date,today)
            if interval_type == 'day':
                if dayDiff > 1:
                    sendMessage(incharge_id,'Report '+name+' Progress Please')
            elif interval_type == 'week':
                if dayDiff > 7:
                    sendMessage(incharge_id,'Report '+name+' Progress Please')

            elif interval_type == 'month':
                if dayDiff > 30:
                    sendMessage(incharge_id,'Report '+name+' Progress Please')
            elif interval_type == 'year':
                if dayDiff > 365:
                    sendMessage(incharge_id,'Report '+name+' Progress Please')
        return None

    def calLengthDays(self,start,end):
        dateFormat='%Y-%m-%d'
        d1 = datetime.strptime(start, dateFormat)
        d2 = datetime.strptime(end, dateFormat)
        dayDiff = (d2-d1).days

        return dayDiff

    def sendMessage(self,incharge_id,msg):
        post_vars = {'subject': "Progress Please",
             'body': msg,
             'partner_ids': [(4, 3)],} # Where "4" adds the ID to the list
                                       # of followers and "3" is the partner
        self.message_post(
        cr, incharge_id, False,
        type="notification",
        subtype="mt_comment",
        context=context,
        **post_vars)
