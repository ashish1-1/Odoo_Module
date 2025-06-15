{
    'name': 'Restrict Quantity And Duration For MO',
    'version': '1.0.0',
    "sequence": 2,
    'category': 'Manufacturing',
    'summary': 'In this customization we can restrict the first 10 components quantity and first one Duration of workorder',
    'depends': ['mrp'],
    'data': [
        'wizard/mrp_consumption_warning_view.xml',
        'views/mrp_production_views.xml',
        'views/mrp_workorder_view.xml',
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}