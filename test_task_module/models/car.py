from odoo import models, fields



class Car(models.Model):
    _name = 'test.car'

    car_number = fields.Char()
    # carrier_id = fields.Many2one('test.partner')
    max_weight = fields.Float()
    max_volume = fields.Float()
