from odoo import api, fields, models
import logging

class OwAccountMove(models.Model):
    _inherit = 'account.move'

    
    ow_sale_order_id = fields.Many2one(
        string='Order',
        comodel_name='sale.order',
    )

    @api.model_create_multi
    def create(self, vals_list):
        invoices = super(OwAccountMove, self).create(vals_list)
        for invoice in invoices:
            if invoice.invoice_origin:
                order_ref = invoice.invoice_origin.split(',')
                sale_order = self.env['sale.order'].search([('name', '=', order_ref[0])], limit=1)
                if sale_order:
                    invoice.ow_sale_order_id = sale_order
        return invoices
    