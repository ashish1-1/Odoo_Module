from odoo import _, api, fields, models


class Skills(models.Model):
    _name = 'skill.skills'
    _description = 'Skill'

    name = fields.Char(
        string='Skill',
        required=True,
    )
       
    skill_type_id = fields.Many2one(
        comodel_name='skill.type',
    )
    
    
