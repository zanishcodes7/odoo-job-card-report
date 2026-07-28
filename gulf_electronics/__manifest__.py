{
    'name': 'Gulf Electronics Job Cards',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Independent Job Card Management for Gulf Electronics',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/gulf_job_card_views.xml',
        'views/gulf_job_card_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}