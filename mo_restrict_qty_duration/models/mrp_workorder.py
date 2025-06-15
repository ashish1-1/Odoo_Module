from odoo import models,api, fields

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.workorder'

    qty_production = fields.Integer('Original Production Quantity', readonly=True, related='production_id.product_qty')
    delegated_to_id = fields.Many2one(
        string='Delegated To',
        comodel_name='hr.employee',
    )

    def _get_duration_expected(self, alternative_workcenter=False, ratio=1):
        self.ensure_one()
        first_work_order = self.production_id.workorder_ids[0]
        if self == first_work_order and self.qty_production > 1:
            return self.operation_id.time_cycle
        return super(ManufacturingOrder,self)._get_duration_expected(alternative_workcenter, ratio)

    @api.model
    def unlink(self):
        for work_order in self:
            manufacturing_order = work_order.production_id

            components = self.env['stock.move'].search([
                ('raw_material_production_id', '=', manufacturing_order.id),
                ('operation_id', '=', work_order.operation_id.id)
            ])

            if components:
                components.unlink()

        return super(ManufacturingOrder, self).unlink()