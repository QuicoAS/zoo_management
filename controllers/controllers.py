# -*- coding: utf-8 -*-
# from odoo import http


# class ZooManagement(http.Controller):
#     @http.route('/zoo_management/zoo_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoo_management/zoo_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoo_management.listing', {
#             'root': '/zoo_management/zoo_management',
#             'objects': http.request.env['zoo_management.zoo_management'].search([]),
#         })

#     @http.route('/zoo_management/zoo_management/objects/<model("zoo_management.zoo_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoo_management.object', {
#             'object': obj
#         })

