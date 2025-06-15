from odoo import fields, models
from odoo.exceptions import UserError, ValidationError, AccessError

from datetime import datetime
import logging


_logger = logging.getLogger(__name__)

class RequestBookWizard(models.TransientModel):
    _name = 'book.request.wizard'
    _description = 'Request for book'

    book_from = fields.Datetime(string='Book From', default=datetime.now())
    till_date = fields.Datetime(string='Till Date', required=True)
    
    def do_action(self):
        data = self.env['book.books'].browse(self._context.get('active_id'))

        if data.availability:
            context = data._context
            current_id = context.get('uid')
            request = {}
            expy_date = self.till_date
            request['expiry_date'] = expy_date
            request['status'] = 'pending'
            request['book_id'] = data.id
            request['assign_to'] = current_id
            result = self.env['booking.history'].sudo().create(request)
            if result:
                mail_template = self.env.ref('wk_library_management.mail_template_request_issue')
                mail_template.send_mail(result.id, force_send=True)
                return {
                    'type':'ir.actions.act_window',
                    'name':'Booking History',
                    'view_mode':'tree,form', 
                    'res_model':'booking.history',
                }
        else:
            raise AccessError('Book is unavailabel')

        