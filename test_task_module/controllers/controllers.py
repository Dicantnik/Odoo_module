# -*- coding: utf-8 -*-
# from odoo import http


# class TestTaskModule(http.Controller):
#     @http.route('/test_task_module/test_task_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_task_module/test_task_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_task_module.listing', {
#             'root': '/test_task_module/test_task_module',
#             'objects': http.request.env['test_task_module.test_task_module'].search([]),
#         })

#     @http.route('/test_task_module/test_task_module/objects/<model("test_task_module.test_task_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_task_module.object', {
#             'object': obj
#         })
