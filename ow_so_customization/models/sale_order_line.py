from odoo import api, fields, models

class OwSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dx_left_up = fields.Char(string='Up',)
    dx_left_down = fields.Char(string='Down',)

    dx_right_up = fields.Char(string='Up',)
    dx_right_down = fields.Char(string='Down',)
    product_uom_qty = fields.Integer(
        string="Quantity",
        compute='_compute_product_uom_qty',
        digits='Product Unit of Measure', default=1.0,
        store=True, readonly=False, required=True, precompute=True)


    def split_diagnose(self, value):
        split_text = value.split(' ')
        return '\n'.join([' '.join(split_text[i:i+4]) for i in range(0, len(split_text), 4)])

    def _prepare_invoice_line(self, **optional_values):
        """Prepare the values to create the new invoice line for a sales order line.

        :param optional_values: any parameter that should be added to the returned invoice line
        :rtype: dict
        """
        res = super(OwSaleOrderLine, self)._prepare_invoice_line(**optional_values)
        if res:
            if self.dx_left_up:
                res.update({'dx_left_up':self.split_diagnose(self.dx_left_up)})
            if self.dx_left_down:
                res.update({'dx_left_down':self.split_diagnose(self.dx_left_down)})
            if self.dx_right_up:
                res.update({'dx_right_up':self.split_diagnose(self.dx_right_up)})
            if self.dx_right_down:
                res.update({'dx_right_down':self.split_diagnose(self.dx_right_down)})
            
        return res