from odoo import fields, models
import logging

class MessageWizard(models.TransientModel):
    _name = 'ow.message.wizard'
    _description = 'Odoo Waves Message Wizard'

    message = fields.Char(string='Message')

    def wizard_message(self,message):
        message_wizard = self.env['ow.message.wizard'].create({'message': message})
        return {
        'name': 'Message',
        'view_mode': 'form',
        'res_model': 'ow.message.wizard',
        'view_id': False,
        'type': 'ir.actions.act_window',
        'res_id': message_wizard.id,
        'target': 'new',
    }

    def action_ok(self):
        return {'type': 'ir.actions.act_window_close'}