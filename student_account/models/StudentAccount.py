from odoo import models, fields, api

class StudentAccount(models.Model):
    _name = 'student.account'
    _description = 'Student Account'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Char(string='Address', required=True)
    city = fields.Char(string='City', required=True)
    state = fields.Char(string='State', required=True)
    zip = fields.Char(string='Zip', required=True)
    country = fields.Char(string='Country', required=True)
    # student_id = fields.Many2one('student.student', string='Student')
