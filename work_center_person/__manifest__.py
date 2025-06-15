{
    'name': 'Work Center Responsible Person',
    'version': '1.0',
    "sequence": 3,
    'category': 'Manufacturing',
    'summary': 'Automatically assigns a responsible person to work centers in manufacturing orders',
    'depends': ['mrp', 'sale'],
    'data': [
        'views/work_center_view.xml',
    ],
}