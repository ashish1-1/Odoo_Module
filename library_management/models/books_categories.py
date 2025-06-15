from odoo import models, fields

class BookCategories(models.Model):
    _name = 'book.category'
    
    name = fields.Char(string = 'Name', required=True)
    image = fields.Binary(string='Image', attachment=False) 
    description = fields.Text(string='Description')
    parent_id = fields.Many2one('book.category',string='Parent')
    book_count = fields.Float(compute='compute_count')


    
    def get_books(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Books',
            'view_mode': 'tree',
            'res_model': 'book.books',
            'domain': [('category_ids', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_count(self):
        for record in self:
            record.book_count = self.env['book.books'].search_count(
                [('category_ids', '=', self.id)])


    def adding_book(self):
        return {
            'name': 'Add Books',
            'type': 'ir.actions.act_window',
            'res_model': 'add.book.wizard',
            'view_mode': 'form',
            'target': 'new'
        }