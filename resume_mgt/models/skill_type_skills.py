from odoo import _, api, fields, models


class SkillTypeSkills(models.Model):
    _name = 'skill.type.skills'
    _description = 'Skill Type Skills'
    
    
    skill_type_id = fields.Many2one(
        string='skill Type',
        comodel_name='skill.type',
    )
    
    
    skills_id = fields.Many2one(
        string='skills',
        comodel_name='skill.skills',
        domain = "[('skill_type_id','=',skill_type_id)]"
    )
    
    skill_progress = fields.Selection(
        string='Skill Progress',
        selection=[('beginner', 'Beginner'), ('elementary', 'Elementary'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')]
    )
    
    skill_level = fields.Integer(compute="level_compute",)
    
    
    resume_id = fields.Many2one(
        string='Resume',
        comodel_name='resume.application',
    )
    

    
    @api.depends('skill_progress')
    def level_compute(self):
        for rec in self:
            if rec.skill_progress == "beginner":
                rec.skill_level = 15
            elif rec.skill_progress == "elementary":
                rec.skill_level = 25
            elif rec.skill_progress == "intermediate":
                rec.skill_level = 50
            elif rec.skill_progress == "advanced":
                rec.skill_level = 75
            else:
                rec.skill_level = 100