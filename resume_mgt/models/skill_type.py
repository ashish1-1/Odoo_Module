from odoo import _, api, fields, models


class SkillType(models.Model):
    _name = 'skill.type'
    _description = 'Skill Type'

    name = fields.Char(
        string='Skill Type',
        required=True,
    )
    
    skill_ids = fields.One2many(
        comodel_name='skill.skills',
        inverse_name='skill_type_id',
    )
    
    

    
