from odoo import fields, models

class StudentInfo(models.Model):
    _name = 'student.info'
    _description = 'Student Information'

    name = fields.Char('Student Name')
    department = fields.Selection([('engineering', 'Engineering'),
                                   ('science', 'Science'),
                                   ('commerce', 'Commerce'),
                                   ('arts', 'Arts')],
                                  'Department')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')
    student_account = fields.Many2one('student.account',  string='Student Account')