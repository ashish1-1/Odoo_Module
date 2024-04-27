from odoo import api, fields, models


class VendorForecast(models.Model):
    _name = 'vendor.forecast'
    _description = 'Vendor Forecast'

    
    product_id = fields.Many2one(
        string='Product',
        comodel_name='product.product',
    )
    
    expected_quantity = fields.Integer(
        string='Expected Quantity',
    )
    
    forecast_date = fields.Datetime(
        string='Forecast Date',
    )
    
    
    