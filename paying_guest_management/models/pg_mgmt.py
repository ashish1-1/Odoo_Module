from odoo import api, fields, models


class PayingGuestManagement(models.Model):
    _name = 'pg.mgmt'
    _description = 'Paying Guest Management'

    _rec_name = 'customer_id'
    # _order = 'name ASC'

    
    customer_id = fields.Many2one(string='Customer',comodel_name='res.partner',required=True)
    email = fields.Char(string='Email',related='customer_id.email')
    phone = fields.Char(string='Phone',related='customer_id.phone')
    image = fields.Image(max_width=256, max_height=256, related='customer_id.image_1920')
    aadhar_number = fields.Char(string='Aadhar Number')
    
    upload_file = fields.Binary(string='Upload File',)
    

    meal_plans_id = fields.Many2one(string='Meal Plans',comodel_name='meal.plans')

    duration = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ], string="Duration", default="monthly",required=True)

    meal_times = fields.Selection([
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('all_meals', 'All Meals')
    ], string="Meal Times", default="all_meals",required=True)

    # start_date = fields.Date(string="Start Date")
    # end_date = fields.Date(string="End Date")

    meal_type = fields.Selection([
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('mixed', 'Mixed')
    ], string="Meal Type", default="veg",required=True)

    payment_term_id = fields.Many2one(string='Payment Terms',comodel_name='account.payment.term')

    discount = fields.Float(string="Discount (%)")
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('online', 'Online'),
        ('card', 'Card')
    ], string="Payment Method",default="online",required=True)

    
    

    
