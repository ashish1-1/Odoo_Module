from odoo import api, fields, models
from odoo.exceptions import UserError
import logging
class AddCategory(models.TransientModel):
    _name = 'sales.report'
    _description = 'Sale Report'
    
    from_date = fields.Datetime(
        string='From',
    )

    to_date = fields.Datetime(
        string='To',
    )

    client = fields.Many2one(
        string='Client',
        comodel_name='res.partner',
    )

    def get_sales_report(self):
        if self.client and self.from_date and self.to_date:
            data = self.env['sale.order'].search([('partner_id','=', self.client.id),('date_order','>=', self.from_date), ('date_order','<=', self.to_date)])

        if not data:
            raise UserError("No sale order found to download the report")
        total_amount = sum(order.amount_total for order in data)
        return self.env.ref('ow_so_customization.action_report_sales').with_context(total_amount=total_amount).report_action(data)
    
