from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_pg_room = fields.Boolean(string="Is PG Room", default=False)