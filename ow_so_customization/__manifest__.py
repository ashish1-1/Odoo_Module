{
    'name': 'Sale Order Customization',
    'version': '1.0.0',
    "sequence": 2,
    'summary': 'In this customization we have added the some extra fields in the sale order',
    'depends': ['sale_management', 'base','l10n_account_customer_statements'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/sales_report_view.xml',
        'views/sale_order_view.xml',
        'views/report_invoice.xml',
        'report/sales_report_template.xml',
        'report/ow_sales_report.xml',
        'report/customer_statement_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ow_so_customization/static/src/js/*.js',
            'ow_so_customization/static/src/xml/*.xml',
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
