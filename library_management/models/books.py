from odoo.exceptions import UserError, ValidationError, AccessError
from odoo import models, fields, api
from datetime import datetime,timedelta
import logging

from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class Books(models.Model):
    _name = 'book.books'
    # _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Char(string = 'Name', required=True)
    image = fields.Binary(string='Image', attachment=False) 
    isbn = fields.Char(string='ISBN', required=True)
    description = fields.Text(string='Description')
    no_of_copies = fields.Integer(string='Copies')
    availability = fields.Boolean(string='Availability',default=False)
    author_ids = fields.Many2many('res.partner',string='Authors')
    responsible = fields.Many2one('res.users',string='Responsible',)
    category_ids = fields.Many2many('book.category', string='Category')
    history_ids = fields.One2many('booking.history', 'book_id', string='Booking History')
    active = fields.Boolean(string="Active",default=True)

    
    @api.constrains('isbn') 
    def _check_(self):
        isbn_cnt = self.search_count([('isbn','=',self.isbn), ('id','!=',self.id)])
        if isbn_cnt>0:
            raise ValidationError("ISBN must be unique")



    def request_issue_button(self):
        
        return {
            'name': 'Detailed Operation',
            'type': 'ir.actions.act_window',
            'res_model': 'book.request.wizard',
            'view_mode': 'form',
            'target': 'new'
        }

    def download_books_detail(self):
        return {
            'name': 'Generate Book Details',
            'type': 'ir.actions.report',
            'model': 'book.books',
            'binding_model_id':'model_book_books',
            'report_type':'qweb-pdf',
            'report_name':'wk_library_management.report_template_book_detail',
            'report_name':'wk_library_management.report_template_book_detail'
        }
        

        
        
            



        
    