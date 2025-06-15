from odoo import api, fields, models
import logging

class OwAccountMove(models.Model):
    _inherit = 'account.move.line'

    
    dx_left_up = fields.Text(string='Up',)
    dx_left_down = fields.Text(string='Down',)

    dx_right_up = fields.Text(string='Up',)
    dx_right_down = fields.Text(string='Down',)

    quantity = fields.Integer(
        string='Quantity',
        compute='_compute_quantity', store=True, readonly=False, precompute=True,
        digits='Product Unit of Measure',
        help="The optional quantity expressed by this line, eg: number of product sold. "
             "The quantity is not a legal requirement but is very useful for some reports.",
    )
    