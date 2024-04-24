from odoo import models, fields



class Route(models.Model):
    _name = 'test.route'

    route_number = fields.Char()
    # carrier_id = fields.Many2one('res.partner', string='Carrier')
    # carrier_id = fields.Many2one('test.partner', string='Carrier')
    car_id = fields.Many2one('test.car', string='car' )
    # order_ids = fields.Many2many('test.order', string='Orders' )
