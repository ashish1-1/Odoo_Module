from odoo import _, api, fields, models


class Hobbies(models.Model):
    _name = 'hobbie.hobbies'
    _description = 'Hobbies'


    name = fields.Char(
        string='Hobbies',
        required=True,
    )

    
