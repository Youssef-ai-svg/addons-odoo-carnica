# -*- coding: utf-8 -*-
# from odoo import http


# class TipuPorc(http.Controller):
#     @http.route('/tipu_porc/tipu_porc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tipu_porc/tipu_porc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tipu_porc.listing', {
#             'root': '/tipu_porc/tipu_porc',
#             'objects': http.request.env['tipu_porc.tipu_porc'].search([]),
#         })

#     @http.route('/tipu_porc/tipu_porc/objects/<model("tipu_porc.tipu_porc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tipu_porc.object', {
#             'object': obj
#         })

