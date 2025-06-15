from odoo import models, fields

class MrpConsumptionWarningLine(models.TransientModel):
    _inherit = 'mrp.consumption.warning.line'

    product_expected_qty_uom = fields.Float("To Consume", digits=(16, 3), readonly=True)
    product_consumed_qty_uom = fields.Float("Consumed", digits=(16, 3), readonly=True)

class MrpProductionSplit(models.TransientModel):
    _inherit = 'mrp.production.split'

    product_qty = fields.Integer(related='production_id.product_qty')

class MrpProductionSplitLine(models.TransientModel):
    _inherit = 'mrp.production.split.line'

    quantity = fields.Integer('Quantity To Produce', digits='Product Unit of Measure', required=True)