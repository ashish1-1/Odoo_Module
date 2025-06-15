from odoo import models, fields

class WorkCenter(models.Model):
    _inherit = 'mrp.workcenter'

    person_responsible = fields.Many2one('hr.employee', 'Person Responsible')
