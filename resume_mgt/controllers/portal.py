from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http
import json


import logging
_logger = logging.getLogger(__name__)



class PortalAccount(CustomerPortal):
   def _prepare_home_portal_values(self, counters):
       values = super()._prepare_home_portal_values(counters)
       if 'resume_count' in counters:
            resume_count = request.env['resume.application'].search_count([])
            values['resume_count'] = resume_count
       return values


   @http.route(['/my/resume'], type='http', auth="user", website=True)
   def ResumeListView(self, **kw):
        resume_obj = request.env['resume.application'].search([])
        vals = {'page_name':'resume_list_view','allresume':resume_obj}
        return request.render("wk_ashish_varshney_resume_mgt.wb_resume_list_view_portal",vals)
    
#    @http.route('/resume/<model("resume.application"):resume>', type='http', auth="public", website=True)
#    def resume_details(self, resume):
#        values = {'resume': resume,}
#        return request.render('wk_ashish_varshney_resume_mgt.single_resume_template', values)
   
   @http.route(['/resume/new_resume'], type="http", auth="public", website="True")
   def resume_data(self, **post):
       return request.render("wk_ashish_varshney_resume_mgt.resume_form_website_templates", )

#    @http.route('/resume-form', type='http', auth='public', methods=['POST'] ,website=True,csrf=False)
#    def add_resume(self, **post):
#        keys = ['degree','board','school_college','max_marks','marks_obtained','year']
#        hobbies_ids_list = request.httprequest.form.getlist('hobbies_ids')
#        education_background_id_list = request.httprequest.form.get('education_background_ids').split(",")
#        post.update({'hobbies_ids':hobbies_ids_list})
#        post.update({'education_background_ids':education_background_id_list})
#        [post.pop(key) for key in keys]   
#        request.env['resume.application'].create(post)
#        return request.redirect('/my/resume')
   
   
   @http.route('/resume-form', type='json', auth='public', methods=['POST'] ,website=True,csrf=False)
   def add_resume(self, **post):
       _logger.info(f"\n\n===={post}=====")
       data = post.get('param')
       education_data = post.get('param').get('edcation_ids')
       hobbies_ids = post.get('param').get('hobbies_ids')
       _logger.info(f"========{education_data}=========")
       _logger.info(f"========{post.get('param').get('hobbies_ids')}=========")
       education_data_ids = request.env['education.background'].create(education_data)
       _logger.info(f"======{education_data_ids}====================")
       resume_data = {
           'name': data.get('name'),
           'mobile':data.get('mobile'),
           'linked_info':data.get('linked_info'),
           'hobbies_ids':hobbies_ids,
           'dob':data.get('dob'),
           'email':data.get('email'),
           'father_name':data.get('father_name'),
           'job_postion':data.get('job_postion'),
           'introduction':data.get('introduction'),
           'street':data.get('street'),
           'zip':data.get('zip'),
           'city':data.get('city'),
           'country_id':data.get('country_id'),
           'state_id':data.get('state_id'),
           'education_background_ids':education_data_ids.ids,
       }
       record_id = request.env['resume.application'].create(resume_data)
       
       return json.dumps({
               'id':record_id.id, 
           } )
   
   
   @http.route('/countries', type="json", auth="public", methods=['POST'], website=True)
   def country_state(self, **kw):
    state_name_list =  []
    state_data = request.env['res.country.state'].search([("country_id","=",int(kw.get('param')))])
    for state in state_data:
        state_name_list.append(state.name)
    if state_data:
           return json.dumps({
               'id':state_data.ids, 
               'name' :state_name_list
           } )
   
   
   @http.route('/add/education', type="json", auth="public", methods=['POST'], website=True)
   def add_education(self, **kw):
       new_record_id = request.env["education.background"].create(kw.get('param'))
       if new_record_id:
           return json.dumps({
               'id':new_record_id.id, 
           } )
           