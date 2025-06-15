from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)

class AddBook(models.TransientModel):
    _name = 'add.book.wizard'
    _description = 'Add Book'
    
    

    book_ids = fields.Many2many('book.books',string='Books')


    def push(self):
        for rec in self.book_ids:
            rec.write({'category_ids':[(4,category_id) for category_id in self._context.get('active_ids')]})
       
        
        
            
            

