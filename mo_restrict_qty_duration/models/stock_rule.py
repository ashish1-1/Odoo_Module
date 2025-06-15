from odoo import models, api, fields

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, bom):
        res = super(StockRule, self)._prepare_mo_vals(product_id, product_qty, product_uom, location_dest_id, name, origin, company_id, values, bom)
        if res:
            sale_id = self.env['sale.order'].search([('name','=', origin)], limit=1)
            res.update({
                'doctor':sale_id.doctor,
                'patient':sale_id.patient
            })
        return res