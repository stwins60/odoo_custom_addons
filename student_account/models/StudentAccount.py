from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class StudentAccount(models.Model):
    _name = 'student.account'
    _description = 'Student Account'
    # _inherit = 'account.invoice'

    student_info = fields.One2many('student.info', 'student_account', string='Account Name')
    account_number = fields.Char(string='Account Number')
    account_type = fields.Selection(
        [('out-of-pocket', 'Out of Pocket'), ('loans', 'Student Loan')], string='Account Type')
    balance = fields.Float(string='Balance')
    status = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive')], string='Status')
    date_created = fields.Date(string='Date Created')

    @api.constrains('account_number')
    def _check_account_number(self):
        for record in self:
            if record.account_number < 10:
                raise UserError('Account Number must be 10 digits long')

    @api.constrains('balance')
    def _check_account_balance(self):
        for record in self:
            if record.balance < 0:
                raise UserError('Account balance cannot be negative')

    @api.constrains('date_created')
    def _check_date(self):
        for record in self:
            if record.date_created > fields.Date.today():
                raise UserError('Date cannot be in the future')
            elif record.date_created < fields.Date.today() - 30:
                raise UserError('Date cannot be more than 30 days old')
            elif record.date_created < fields.Date.today() - 1826.25:
                raise UserError('Date cannot be more than 5 years old')

    def action_activate_student_account(self):
        self.status = 'inactive'
        if self.status:
            self.status = 'active'
        else:
            raise UserError('Account is already active')

    def action_deactivate_student_account(self):
        self.status = 'active'
        if self.status:
            self.status = 'inactive'
        else:
            raise UserError('Account is already inactive')

    # def action_create_invoice(self):
    #     for student in self:
    #         invoice = self.env['account.invoice'].create({
    #             'partner_id': student.account.id,
    #             'type': 'out_invoice',
    #             'account_id': student.account_number,
    #             'journal_id': self.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,
    #             'invoice_line_ids': [(0, 0, {
    #                 'product_id': self.env['product.product'].search([('name', '=', 'Student Invoice')], limit=1).id,
    #                 'quantity': 1,
    #                 'price_unit': student.balance,
    #                 'name': student.student_info,
    #                 'account_id': self.env['student.account'].search([('name', '=', student.student_info)], limit=1).id,
    #                 'invoice_id': invoice.id,
    #             })],
    #         })