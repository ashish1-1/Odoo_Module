from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

import re


class ResumeApplication(models.Model):
    _name = 'resume.application'
    _description = 'Resume Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name',required=True,)
    responsible_id = fields.Many2one(comodel_name='res.users', string="Responsible", default=lambda self : self.env.uid)
    status = fields.Selection([('draft','Draft'),('new', 'New'), ('submitted', 'Submitted'), ('approved', 'Approved'), ('published', 'Published')], string='Status',default='new', tracking = True)
    
    # Personal data
    mobile = fields.Char(string="Mobile",)
    dob = fields.Date(string='DOB')
    age = fields.Char(string='Age', compute='age_compute_field', store=True)
    email = fields.Char(string='Email',required=True)
    introduction = fields.Text(string="Summary",required=True)
    linked_info = fields.Char(string="Linkedin", required=True)
    job_postion = fields.Char(string="Job Postion", required=True)
    father_name = fields.Char(string="Father's Name",required = True)
    
    # Address
    street = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    country_id = fields.Many2one('res.country',string='Country', ondelete='restrict')
    state_id = fields.Many2one('res.country.state',string="State", ondelete='restrict',)
    
    image = fields.Binary(string="Image")
    
    education_background_ids = fields.One2many(comodel_name='education.background', inverse_name='resume_application_id',)
    skill_ids = fields.One2many(string='Skills', comodel_name='resume.skill', inverse_name='resume_id',)
    experience_project_ids = fields.One2many(string='Experience/Project', comodel_name='experience.project', inverse_name='resume_id',)
    hobbies_ids = fields.Many2many(string='Hobbies', comodel_name='hobbie.hobbies',)
    certification_ids = fields.One2many(comodel_name='certification.certifications',inverse_name='resume_id',)
    achivement_ids = fields.One2many(comodel_name='achivement.achivements',inverse_name='resume_id',)
    skill_type_skill_ids = fields.One2many(comodel_name='skill.type.skills', inverse_name='resume_id',)
    
    
    
    @api.constrains('mobile')
    def mobile_check_(self):
        if not self.mobile.isdigit():
            raise ValidationError("mobile number should be numeric value")
        if not len(self.mobile) == 10 :
            raise ValidationError("mobile number length should be 10")
        

    @api.onchange('state_id')
    def _onchange_field(self):
        self.country_id = self.state_id.country_id
    

    @api.model
    def create(self, vals):
        data =  super(ResumeApplication, self).create(vals)
        data[0]['email'] = vals['email'].lower()
        return data
        

    @api.constrains('email') 
    def _check_(self):  
        email_cnt = self.sudo().search_count([('email','=',self.email), ('id','!=',self.id)])
        if email_cnt>0:
            raise ValidationError("Email must be unique")
        else:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if( not re.fullmatch(regex, self.email)):
                raise ValidationError("Give Valid Email")
            
      
    @api.depends('dob')
    def age_compute_field(self):
        for record in self:
           
            if record.dob:
                days_in_year = 365.2425
                temp_age = int((date.today()-record.dob).days/days_in_year)
                if temp_age < 18:
                    record.age = "0"+"year"
                    raise ValidationError("Give Validate Date of Birth")
                else:
                    if temp_age>= 100:
                        record.age = "0"+"year"
                        raise ValidationError("Give Validate Date of Birth")
                    else:    
                        record.age = f'{temp_age}' +"year"
            else:
                record.age = "0"+"year"
           

    def send_by_email(self):
        self.status = 'submitted'
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
        }
        
    def approved_for_additional_skill(self):
        mail_template = self.env.ref('wk_ashish_varshney_resume_mgt.mail_template_approve_additional_info')
        mail_template.send_mail(self.id, force_send=True)
        self.status = 'approved'

    def resume_published(self):
        self.status = 'published'
    
    def resume_unpublished(self):
        self.status = 'draft'
        
    
        
