{
    'name' : "Resume Management System",
    'version' : '1.0',
    'depends' :['base','website','mail'],
    'author' : 'Webkul Software Pvt. Ltd.',
    'category' : 'Human Resourse',
    'description' : 'Resume Management System',
    'data' : [
        'security/resume_security.xml',
        'security/ir.model.access.csv',
        'report/ir_action_resume_report_template.xml',
        'report/ir_action_resume_report.xml',
        'views/resume_application_view.xml',
        'views/menu.xml',
        'views/website_menu.xml',
        'views/resume_website_template.xml',
        'views/resume_form_template.xml',
        'data/approved_email.xml',
        'views/portal_view.xml',
        'demo/resume_demo_data.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence':0,
    'images':[
        
        ],
    
   'assets': {
        'web.assets_frontend': [
            'wk_ashish_varshney_resume_mgt/static/src/js/odoo_script.js'
        ],}
}