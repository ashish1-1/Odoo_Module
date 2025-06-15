from odoo import _, api, fields, models


class Achivement(models.Model):
    _name = 'achivement.achivements'
    _description = 'Achivement'

    name = fields.Char(
        string='Achivements',
        required=True
    )
    
    resume_id = fields.Many2one(
        comodel_name='resume.application',
    )
    