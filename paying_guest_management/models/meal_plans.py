from odoo import fields, models, api

class MealPlans(models.Model):
    _name="meal.plans"
    _description="Meal Plans"


    name = fields.Char(string="Plan Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", required=True)
    available_dishes = fields.Text(string="Available Dishes")
    extras = fields.Text(string="Extras")
    active = fields.Boolean(string="Active", default=True)
