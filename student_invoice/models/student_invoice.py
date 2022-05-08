from odoo import models
from odoo import Command
import logging


# _logging = logging.getLogger(SMNT)

class StudentInvoice(models.Model):
    _inherit = 'student.account'

    def action_create_invoice(self):
        for student in self:
            invoice = self.env['account.invoice'].create({
                'partner_id': student.account.id,
                'type': 'out_invoice',
                'account_id': student.account_number,
                'journal_id': self.env['account.journal'].id,
                'invoice_line_ids': [(0, 0, {
                    'product_id': self.env['product.product'].search([('name', '=', 'Student Invoice')], limit=1).id,
                    'quantity': 1,
                    'price_unit': student.balance,
                    'name': student.student_info,
                    'account_id': self.env['student.account'].search([('name', '=', student.student_info)], limit=1).id,
                    'invoice_id': invoice.id,
                })],
            })
