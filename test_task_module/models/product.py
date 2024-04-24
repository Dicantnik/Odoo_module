from odoo import models, fields



class OrderLine(models.Model):
    _name = 'test.product'
    _inherit = 'test.producttemplate'

    weight = fields.Float()
    volume = fields.Float()


