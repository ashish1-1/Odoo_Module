{
    "name":"Paying Guest Management",
    "depends":['account'],
    "data":[
        'security/ir.model.access.csv',
        'views/pg_mgmt_view.xml',
        'views/meal_plans_view.xml',
        'views/menus.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'static/src/js/**/*.js',
    #         'static/src/xml/**/*.xml',
    #     ],
    # },
    "image":"static/description/icon.png",
}