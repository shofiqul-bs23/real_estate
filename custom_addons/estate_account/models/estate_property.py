from odoo import fields, models, api, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"
    _description = "This is the Inherited model of EstateProperty that can generate invoice ! "

    def set_as_sold(self):
        # print("Is is the Real World ? Or is this a Fantacy?")
        # This is working

        move_type = 'out_invoice'
        journal_id = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()

        self.env['account.move'].create(
            {
                'partner_id': self.buyer_id,
                'move_type': move_type,
                'journal_id': journal_id.id,
             'invoice_line_ids': [
                 Command.create({
                     'name': self.name,
                     'quantity': 1,
                     'price_unit': self.selling_price * 6 / 100
                 }),
                 Command.create({
                     'name':'administrative fees',
                     'quantity': 1,
                     'price_unit' : 100
                 })
             ],
             })
        return super().set_as_sold()
