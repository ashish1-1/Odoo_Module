from odoo import http
from odoo.http import request
from collections import defaultdict


import logging
_logger = logging.getLogger(__name__)

class ResumeData(http.Controller):
    
    @http.route(['/resume/'], type="http", auth="public",methods=['GET'], website="True", csrf=False)
    def resume_data(self, **post):
        if request.env.user.has_group('wk_ashish_varshney_resume_mgt.security_manager_group'):               
            resume_data = request.env['resume.application'].search([])
            values = {
                                'records': resume_data
                        } 
            return request.render("wk_ashish_varshney_resume_mgt.resume_website_templates", values)
        else:
            resume_data = request.env['resume.application'].search([('status','=','published')])
            values = {
                                'records': resume_data
                        } 
            return request.render("wk_ashish_varshney_resume_mgt.resume_website_templates", values)


    @http.route('/resume/<int:id>', type='http', auth="public", website=True)
    def resume_details(self, id):
        resume = request.env['resume.application'].sudo().browse(id)
        skill_dict = {}
        for i in resume.skill_type_skill_ids:
             skill_dict[i.skills_id.name] = i.skill_type_id.name
        res = defaultdict(list)
        
        for key, val in sorted(skill_dict.items()):
            res[val].append(key)
        skills_dict = {}
        
        for key, val in dict(res).items():
            skills_dict[key] = ", ".join(val)

        values = {'resume': resume, 'skill_data':skills_dict,'page_name':'resume_form_view' }
        return request.render('wk_ashish_varshney_resume_mgt.single_resume_template', values)
       
     
       