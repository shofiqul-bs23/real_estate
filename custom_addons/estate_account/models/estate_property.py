from odoo import fields, models, api


class EstateProperty(models.Model):
    _inherit = "estate.property"
    _description = "This is the Inherited model of EstateProperty that can generate invoice ! "

    def set_as_sold(self):
        # print("Is is the Real World ? Or is this a Fantacy?")
        # This is working


        move_type = 'out_invoice'
        # journal_id = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        
        self.env['account.move'].create({'partner_id':self.buyer_id, 'move_type':move_type
                                        })
        return super().set_as_sold()
