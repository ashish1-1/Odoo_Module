from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    history_ids = fields.One2many('booking.history', 'partner_id', string='Booking History')
    book_ids = fields.Many2many('book.books',string='Books')
    
    
    
    
    def update_booking(self):
        return {
            'name': 'Update existing active bookings',
            'type': 'ir.actions.act_window',
            'res_model': 'update.booking.history.wizard',
            'view_mode': 'form',
            'target': 'new'
            } 
    