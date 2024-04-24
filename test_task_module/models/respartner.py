from odoo import models, fields



class ResPartner(models.Model):
    _name = 'test.partner'
    _inherit = 'res.partner'

    partner_group = fields.Selection(
        default = 'client',
        selection=[('client', 'Client'),('supplier', 'Supplier'),
                   ('carrier', 'Carrier')] )