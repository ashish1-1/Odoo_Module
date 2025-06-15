from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)

class AvailableSlotWizard(models.TransientModel):
    _name = 'available.slot.wizard'
    _description = 'Available Slot Wizard'
    
    def _default_available_date(self):
        parent_data = self.env['booking.history'].browse(self._context.get('parent_id'))
        _logger.info(parent_data.read([]))
        books_history_data = self.env['booking.history'].search([('status','=','approved'),('book_id','=',parent_data.book_id.id)])
        return books_history_data.ids
    
    slots_ids = fields.Many2many('booking.history',default=_default_available_date)
    


    def notify_user(self):
        mail_template = self.env.ref('wk_library_management.mail_template_notify_user')
        mail_template.send_mail(self.slots_ids.id, force_send=True)
                        
    
