from odoo import _, api, fields, models


class ModelName(models.Model):
    _name = 'resume.skill'
    _description = 'ModelName'


    
    name = fields.Many2one(string='Skills', comodel_name='hr.skill')
    skill_type_id = fields.Many2one(string='Skill Type', comodel_name='hr.skill.type', )
    skill_level_id = fields.Many2one(string='Skill Progress', comodel_name='hr.skill.level',)
    level_progress = fields.Integer(string="Progress", compute="progress_level_compute_field")
    resume_id = fields.Many2one(string='resume', comodel_name='resume.application',)
    
    
    @api.depends('skill_level_id')
    def progress_level_compute_field(self):
        for rec in self:
            rec.level_progress = rec.skill_level_id.level_progress
    
    
    
    

    
