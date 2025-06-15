from odoo import fields, models
import logging

class CsvColumn(models.Model):
    _name = 'column.column'
    _description = 'Excel Columns'

    name = fields.Char(string="Column Name")
    
    instance_id = fields.Many2one(
        string='Instance',
        comodel_name='csv.instance',
    )
    