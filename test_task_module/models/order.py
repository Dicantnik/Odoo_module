from odoo import models, fields



class Order(models.Model):
    _name = 'test.order'

    name = fields.Char()
    order_date = fields.Date(default=fields.Date.today,)
    client_id = fields.Many2one('test.partner', string='Client')
    supplier_id = fields.Many2one('test.partner', string='Supplier')
    order_cost = fields.Float()
    order_weight = fields.Float()
    order_volume = fields.Float()
    order_line_ids = fields.One2many('test.orderline', 'order_id', string='OrderLine')
