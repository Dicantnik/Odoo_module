# -*- coding: utf-8 -*-
{
    'name': "test_task_module",

    'summary': "",


    'author': "Andry",

    'category': 'Cusomizations',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sales'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/car.xml',
        # 'views/route.xml',
        # 'views/order.xml',
        # 'views/orderline.xml',
        # 'views/product.xml',
        # 'views/respartner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
