from odoo import models, api, fields

class ContractParticipation(models.Model):
    _inherit = "contract.participation"

    # When payment information is set and the sate payment pending, automatically set the contract state to active
    @api.onchange('payment_mode_id', 'payment_date')
    def _on_payment_set(self):
        stage_active  = self.env["contract.participation.stage"].search([('valid', '=', 'True')])
        stage_pending = self.env["contract.participation.stage"].search([('default', '=', 'True')])
        for record in self:
            if record.payment_mode_id.id and record.payment_date and record.stage_id.id == stage_pending.id:
                record.stage_id = stage_active

    crece_activation_date   = fields.Datetime(string='Crece Solar fecha activación')
    crece_deactivation_date = fields.Datetime(string='Crece Solar fecha desactivación')

    crece_active = fields.Boolean(string='Crece Solar activado', compute='_compute_crece_active')
    @api.depends('crece_activation_date', 'crece_deactivation_date')
    def _compute_crece_active(self):
        for record in self:
            record.crece_active = record.crece_activation_date and not record.crece_deactivation_date
