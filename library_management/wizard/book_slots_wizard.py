from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)

class BookSlotsWizard(models.TransientModel):
    _name = 'book.allocate.slot.wizard'
    # _description = 'ModelName'

    def booking_history_wizard_data(self):
        parent_data = self.env['booking.history'].browse(self._context.get('active_id'))
        books_history_data = self.env['booking.history'].search([('booking_date', '>=', parent_data.booking_date),('expiry_date','<=',parent_data.expiry_date),('id','!=',parent_data.id),('status','=','approved')])

        
        return books_history_data.ids
    
    
    booking_history_ids = fields.Many2many('booking.history',default=booking_history_wizard_data)

    
 
    def request_check_action(self):
        return {
            'name': 'Available Slots',
            'type': 'ir.actions.act_window',
            'res_model': 'available.slot.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context':{'parent_id':self._context.get('active_id')}
            }   