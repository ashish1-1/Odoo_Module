from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)

class UpdateBookingHistory(models.TransientModel):
    _name = 'update.booking.history.wizard'
    selection_booking_id = fields.Many2one('booking.history',string='Selection Booking')
    booking_date = fields.Datetime(string='Booking Date')
    expiry_date = fields.Datetime(string='Till Date')
    
    
    @api.onchange('selection_booking_id')
    def onchange_selection_booking_id(self):
        self.booking_date = self.selection_booking_id.booking_date 
        self.expiry_date = self.selection_booking_id.expiry_date 
        
    
    def update_change(self):
        self.selection_booking_id.sudo().write({'booking_date':self.booking_date,'expiry_date':self.expiry_date})
