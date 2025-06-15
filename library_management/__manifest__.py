{
    'name' : "Odoo Library Management System",
    'version' : '1.0',
    'depends' :['base','mail','website'],
    'author' : 'Webkul Software Pvt. Ltd.',
    'category' : 'Website',
    'description' : 'A library management system is software that is designed to manage all the functions of a library. It helps librarian to maintain the database of new books and the books that are borrowed by members along with their due dates.',
    'website':'www.webkul.com',
    'data' : [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'report/ir_actions_report_templates_book.xml',
        'report/ir_actions_report_book.xml',
        'wizard/book_wizard.xml',
        'wizard/book_slots_wizard.xml',
        'wizard/update_existing_booking_history.xml',
        'wizard/available_slot_wizard.xml',
        'wizard/add_book_wizard.xml',
        'views/books.xml',
        'views/books_categories.xml',
        'views/booking_history.xml',
        'views/res_partner_view.xml',
        'views/menu.xml',
        'views/website_menu.xml',
        'views/book_website_template.xml',
        'data/request_issue_email.xml',
    ],
    'demo': [
        'demo/books_data_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence':0,
    'images':[
        'static/description/icon.png',
        ],
    
    'assets': {
        'web.assets_frontend': [
            'wk_library_management/static/src/css/working.css',
            # 'wk_library_management/static/src/js/script.js',
            'wk_library_management/static/src/js/odoo_script.js'
        ],}
}