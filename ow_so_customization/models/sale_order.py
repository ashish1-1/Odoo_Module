from odoo import api, fields, models

class OwSaleOrder(models.Model):
    _inherit = 'sale.order'

    doctor = fields.Char(string='Doctor',)
    patient = fields.Char(string='Patient',)

    dx_left_up = fields.Text(string='Up',compute="compute_extra_field")
    dx_left_down = fields.Text(string='Down',compute="compute_extra_field")

    dx_right_up = fields.Text(string='Up',compute="compute_extra_field")
    dx_right_down = fields.Text(string='Down',compute="compute_extra_field")
    

    ow_product_id = fields.Text(string='Product',compute="compute_extra_field")
    ow_product_uom_qty = fields.Text(string='Quantity',compute="compute_extra_field")
    ow_price_unit = fields.Text(string='Price',compute="compute_extra_field")

    def split_diagnose(self, value):
        if not value:
            return ''
        split_text = value.split(' ')
        return '\n'.join([' '.join(split_text[i:i+4]) for i in range(0, len(split_text), 4)])

    
    @api.depends('order_line')
    def compute_extra_field(self):
        for rec in self:
            prod, qty, price, dx_left_up, dx_left_down, dx_right_up, dx_right_down = '', '', '', '', '', '', ''
            for line in rec.order_line:
                prod += str(line.product_id.name) + "\n"
                qty += str(line.product_uom_qty) + "\n"
                price += str(line.price_unit) + "\n"
                dx_left_up += self.split_diagnose(line.dx_left_up) + "\n"
                dx_left_down += self.split_diagnose(line.dx_left_down) + "\n"
                dx_right_up += self.split_diagnose(line.dx_right_up) + "\n"
                dx_right_down += self.split_diagnose(line.dx_right_down) + "\n"
            rec.ow_product_id = prod
            rec.ow_product_uom_qty = qty
            rec.ow_price_unit = price
            rec.dx_left_up = dx_left_up
            rec.dx_left_down = dx_left_down
            rec.dx_right_up = dx_right_up
            rec.dx_right_down = dx_right_down