# -*- coding: utf-8 -*-
# from odoo import http


# class PersonalitzarCompra(http.Controller):
#     @http.route('/personalitzar_compra/personalitzar_compra', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/personalitzar_compra/personalitzar_compra/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('personalitzar_compra.listing', {
#             'root': '/personalitzar_compra/personalitzar_compra',
#             'objects': http.request.env['personalitzar_compra.personalitzar_compra'].search([]),
#         })

#     @http.route('/personalitzar_compra/personalitzar_compra/objects/<model("personalitzar_compra.personalitzar_compra"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('personalitzar_compra.object', {
#             'object': obj
#         })

