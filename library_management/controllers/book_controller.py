from odoo import http
from odoo.http import request
import base64
import json

import logging
_logger = logging.getLogger(__name__)

class BookData(http.Controller):
    
       @http.route(['/book/'], type="http", auth="public",methods=['GET'], website="True")
       def book_data(self, **post):
           books_data = request.env['book.books'].sudo().search([])
           values = {
                            'records': books_data
                    } 
           return request.render("wk_library_management.book_website_templates", values)
       
       
       @http.route('/book/<model("book.books"):book>', type='http', auth="public", website=True)
       def product_details(self, book):
           values = {'book': book,}
           return request.render('wk_library_management.book_details', values)
       
       
       @http.route('/book/add-book', type='http', auth='public', methods=['POST'] ,website=True,csrf=False)
       def add_book(self, **post):
           
           files = request.httprequest.files.get('image')
           catgory_ids_list = request.httprequest.form.getlist('category_ids')
           post.update({'category_ids':catgory_ids_list})
           
           attachment = files.read()
           post.update({'image':base64.encodebytes(attachment)})
           if 'availability' in post and post['availability'] == 'on':
               post['availability'] = True
           else :
               post['availability'] = False
           request.env['book.books'].create(post)
           return request.redirect('/book')
           
         
           
       @http.route(['/book/addBookJson'], type='json', auth="user", website=True, csrf=False)
       def input_data_processing(self, **kw):
           
        #    data = json.loads(request.httprequest.data)
        #    record_data = data.get('params')

           new_record = request.env["book.books"].create(kw.get('param'))
           return request.env['ir.ui.view']._render_template("wk_library_management.add_book_template", {

            'book': new_record,})
           