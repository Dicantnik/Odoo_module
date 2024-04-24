from odoo import models, fields



class OrderLine(models.Model):
    _name = 'test.orderline'

    order_id = fields.Many2one('test.order', string='Order')
    product_id = fields.Many2one('test.product', string='Product')
    price = fields.Float()
    count = fields.Float()
    cost = fields.Float()
