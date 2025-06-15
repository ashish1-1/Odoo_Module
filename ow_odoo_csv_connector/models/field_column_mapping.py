from odoo import fields, models, api

class FieldColumnMapping(models.Model):
    _name = 'field.column.mapping'
    _description = 'Fields Column Mapping'

    
    instance_id = fields.Many2one(
        string='instance',
        comodel_name='csv.instance',
    )
    
    sequence = fields.Integer(string="Sequence", default=10)
    
    model_id = fields.Many2one(
        string='Model',
        comodel_name='ir.model',
        related='instance_id.model_id',
    )
    
    
    field_id = fields.Many2one(
        string='Field',
        comodel_name='ir.model.fields',
        domain="[('model_id', '=',model_id)]"
    )

    excel_column_id = fields.Many2one(string='Excel Column', comodel_name='column.column',
    domain="[('instance_id','=',instance_id)]"
    
    )

    