from odoo import _, api, fields, models
from odoo.exceptions import UserError , ValidationError
from datetime import datetime


class EducationBackground(models.Model):
    _name = 'education.background'
    _description = 'Education Background'
    
    board = fields.Char(string='Board',required=True)
    school_college = fields.Char(string='School/College',required=True)
    year = fields.Selection(string='Year', selection='years_selection',required=True, default='select')
    max_marks = fields.Integer(string='Max. Marks')
    marks_obtained = fields.Integer(string='Marks Obtained',)
    percentage_cgpa = fields.Selection(string='Choose Percentage/CGPA', selection=[('percentage', 'Percentage'), ('cgpa', 'CGPA')],default='percentage',)
    degree = fields.Char(string='Class/Courses',required=True)
    percentage_cgpa_val = fields.Float(string='Percentage/CGPA', compute='percentage_cgpa_val_compute_field', store=True)
    resume_application_id = fields.Many2one(string='Education Qualification', comodel_name='resume.application')
    
    
    def years_selection(self):
        year_list = [('select','Select year')]
        for y in range(datetime.now().year-20, datetime.now().year+1):
            year_list.append((str(y), str(y)))
        return year_list
    
    
    @api.onchange('marks_obtained')
    def marks_check_(self):
        for record in self:
            if int(record.marks_obtained) > int(record.max_marks):
                raise ValidationError("Marks Obtained should be less than or equal to Max. Marks")
    
    

    @api.depends('max_marks', 'marks_obtained', 'percentage_cgpa')
    def percentage_cgpa_val_compute_field(self):
        for record in self:
            if record.max_marks:
                if record.percentage_cgpa == 'percentage':
                    record.percentage_cgpa_val = (int(record.marks_obtained)/int(record.max_marks))*100
                else:
                    record.percentage_cgpa_val = ((int(record.marks_obtained)/int(record.max_marks))*100)/9.5
            else:
                record.percentage_cgpa_val = 0 
            
    
