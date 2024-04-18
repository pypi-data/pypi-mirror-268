from odoo import models, api, fields

class AccountAllocation(models.Model):
    _inherit = 'account.allocation'

    state = fields.Selection(
        selection_add=[
            ('reinversion_iva', 'Reinversión IVA'),
            ('crece_acumulado', 'Crece Solar - acumulado'),
            ('crece_reinvertido', 'Crece Solar - reinvertido')
        ]
    )

