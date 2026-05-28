from odoo import fields, models

class CancelWizard(models.TransientModel):
    _name = "estate.cancel.wizard"
    _description = "Cancel Property Wizard"

    reason = fields.Char(string="Reason for Cancellation", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    def action_confirm_cancel(self):
        # We access the property record linked to this wizard
        self.property_id.state = 'canceled'
        # Log the reason (we could add a 'cancellation_reason' field to the property later!)
        print(f"Property {self.property_id.name} canceled. Reason: {self.reason}")
        return True