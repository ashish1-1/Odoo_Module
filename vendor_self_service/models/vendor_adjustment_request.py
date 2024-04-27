from odoo import api, fields, models


class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'

    
    order_id = fields.Many2one(
        string='Order\'s',
        comodel_name='sale.order',
    )
    
    adjustment_detail = fields.Text(
        string='Adjustment Detail',
    )
    
    comment = fields.Text(
        string='Comment',
    )
    
    
    
    
    