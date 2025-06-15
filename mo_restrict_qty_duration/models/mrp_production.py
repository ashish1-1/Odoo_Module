from odoo import models, api, fields

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.production'

    product_qty = fields.Integer(
        'Quantity To Produce', digits='Product Unit of Measure',
        readonly=False, required=True, tracking=True, precompute=True,
        compute='_compute_product_qty', store=True, copy=True)
    qty_producing = fields.Integer(string="Quantity Producing", digits='Product Unit of Measure', copy=False)
    doctor = fields.Char(string='Doctor')
    patient = fields.Char(string='Patient')

    def _action_generate_consumption_wizard(self, consumption_issues):
        ctx = self.env.context.copy()
        lines = []
        pd_qty_map = dict()
        check = set()
        for order, product_id, consumed_qty, expected_qty in consumption_issues:
            for move in order.move_raw_ids:
                if move.bom_line_id.operation_id.name == 'Allcia' and move.product_id == product_id:
                    pd_qty_map[product_id.id] = move.product_uom_qty
                if move.product_id.id not in check:
                    check.add(move.product_id.id)
            if product_id.id not in check:
                continue
            lines.append((0, 0, {
                'mrp_production_id': order.id,
                'product_id': product_id.id,
                'consumption': order.consumption,
                'product_uom_id': product_id.uom_id.id,
                'product_consumed_qty_uom': consumed_qty,
                'product_expected_qty_uom': pd_qty_map[product_id.id] if pd_qty_map.get(product_id.id) else expected_qty
            }))
        ctx.update({'default_mrp_production_ids': self.ids,
                    'default_mrp_consumption_warning_line_ids': lines,
                    'form_view_ref': False})
        action = self.env["ir.actions.actions"]._for_xml_id("mrp.action_mrp_consumption_warning")
        action['context'] = ctx
        return action

    @api.model_create_multi
    def create(self, vals_list):
        res = super(ManufacturingOrder, self).create(vals_list)
        for line in res.move_raw_ids:
            if line.bom_line_id.operation_id.name == 'Allcia':
                if line.bom_line_id.operation_id.name == 'Allcia':
                    line.product_uom_qty = line.bom_line_id.product_qty
        return res

    @api.onchange('move_raw_ids')
    def _onchange_move_raw_ids(self):
        for line in self.move_raw_ids:
            if line.bom_line_id.operation_id.name == 'Allcia':
                line.product_uom_qty = line.bom_line_id.product_qty