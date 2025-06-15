from odoo import _, api, fields, models


class Certification(models.Model):
    _name = 'certification.certifications'
    _description = 'Certification'

    name = fields.Char(
        string='Certifications',
        required=True,
    )
    
    resume_id = fields.Many2one(
        comodel_name='resume.application',
    )
    

    
