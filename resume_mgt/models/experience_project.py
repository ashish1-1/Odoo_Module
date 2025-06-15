from odoo import _, api, fields, models


class ExperienceProject(models.Model):
    _name = 'experience.project'
    _description = 'Experience/Project'

    name = fields.Char(required=True)
    line_type_id = fields.Many2one('hr.resume.line.type', string="Type", required=True)
    job_position = fields.Char(string="Job Position")
    date_start = fields.Date(string="Date Start",required=True)
    date_end = fields.Date(string="Date End")
    duration = fields.Integer(string="Duration", compute="duration_compute_field", store=True)
    description = fields.Text(string="Description")
    no_of_people_involved = fields.Integer(string="No. of people involved") 
    technology_used = fields.Char(string="Technology Used", required=True)
    resume_id = fields.Many2one(string='resume',comodel_name='resume.application',)
    
    
    @api.depends('date_start','date_start')
    def duration_compute_field(self):
        for rec in self:
            if rec.date_start and rec.date_end:
                rec.duration = (rec.date_end - rec.date_start).days
    
    

    
