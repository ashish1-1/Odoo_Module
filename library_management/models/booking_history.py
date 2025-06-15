from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, AccessError

from datetime import datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

from datetime import datetime




class BookingHistory(models.Model):
    _name = 'booking.history'
    
    name = fields.Char(string = 'Booking No', required=True, index=True, copy=True, default='New')
    booking_date = fields.Datetime(string='Booking Date',default=datetime.now())
    expiry_date = fields.Datetime(string='Booking Till',required=True)
    status = fields.Selection([('draft', 'Draft'),('pending','Pending'),('approved','Approved'),('returned','Returned')],default="draft", copy=False)
    issued_by = fields.Many2one('res.users',string='Issued By')
    received_by = fields.Many2one('res.users',string='Received By')
    assign_to = fields.Many2one('res.users',string='Assign To',required=True)
    book_id = fields.Many2one('book.books',string='Book',required=True,compute="change_status",store=True,readonly=False,domain="[('availability','=',True)]")
    partner_id = fields.Many2one('res.partner', string='partner',compute="book_history_inherit",store=True)
    total_days = fields.Integer('Days', compute='total_days_compute_field',store=True)
    available_booking_date = fields.Datetime(string='Available booking Date')
    available_expiry_date = fields.Datetime(string='Available Expiry Date')
    
    
    
    
    def unlink(self):
        self.partner_id.write({'book_ids':[(3,self.book_id.id)]})
        return super(BookingHistory, self).unlink()


    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('booking.history')
        data = super(BookingHistory,self).create(vals)
        data.partner_id.write({'book_ids':[(4,data.book_id.id)]})
        # if data and data.status != 'returned'::
        #     data.book_id.availability = False
        return data
    
    
    @api.depends('status')
    def change_status(self):
        for rec in self:
            if rec.status == 'returned':
                rec.book_id.write({"availability": True})
            else:
                rec.book_id.write({"availability": False})

        
            
    @api.depends('booking_date','expiry_date')
    def total_days_compute_field(self):
        for record in self:
            record.total_days = (record.expiry_date - record.booking_date).days
            record.available_booking_date = record.expiry_date + timedelta(days=1)
            record.available_expiry_date = record.expiry_date + timedelta(days=10)


    
    @api.depends('assign_to')
    def book_history_inherit(self):
        for record in self:
            record.partner_id = record.assign_to.partner_id.id


    def validate_approve(self):
        if self.book_id.availability:
            self.status = 'approved'
            self.env['book.books'].sudo().write({'availability':False})
            mail_template = self.env.ref('wk_library_management.mail_template_status_approved')
            mail_template.send_mail(self.id, force_send=True)
        else:
            return {
            'name': 'Detailed Operation',
            'type': 'ir.actions.act_window',
            'res_model': 'book.allocate.slot.wizard',
            'view_mode': 'form',
            'target': 'new'
            }   
    
    def deny_record(self):
        for rec in self:
            # _logger.info(f'=====rec====={rec.read([])}')
            if rec.status == "pending":
                rec.write({'status':'draft'})
            else:
                raise AccessError(f"The Booking No. is not in pending state====>{rec.name}")
            
    def remainder_book(self):
        for rec in self:
            if rec.expiry_date < datetime.now() and rec.status == 'approved':
                mail_template = self.env.ref('wk_library_management.mail_template_remainder_book')
                mail_template.send_mail(self.id, force_send=True)



    def action_reminder(self):
        data = self.env['booking.history'].search([])
        for rec in data:
            if rec.expiry_date < datetime.now() and rec.status == 'approved':
                mail_template = self.env.ref('wk_library_management.mail_template_remainder_book')
                mail_template.send_mail(rec.id, force_send=True)

    def mark_as_returned(self):
        if self.status == "approved":
            self.write({'status':'returned'}) 