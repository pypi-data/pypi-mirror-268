from odoo import models, api, fields

class Partner(models.Model):
    _inherit = "res.partner"

    interest_ids = fields.Many2many('res.partner.interest', column1='partner_id',
                                    column2='category_id', string='Interests')
