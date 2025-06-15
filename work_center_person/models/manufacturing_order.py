from odoo import models, api

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def create(self, vals):
        res = super(ManufacturingOrder, self).create(vals)
        for workorder in res.workorder_ids:
            workorder.employee_assigned_ids = workorder.workcenter_id.person_responsible
        return res
