{
    'name': 'Student Account',
    'version': '0.1',
    'category': 'Accounting',
    'description': """
        This module is used to create student account.
    """,
    'author': 'Odoo SA',
    'website': 'https://www.odoo.com/',
    'depends': ['base', 'account', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_account_view.xml',
        'views/student_info.xml',
        # 'views/student_account_sequence.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}