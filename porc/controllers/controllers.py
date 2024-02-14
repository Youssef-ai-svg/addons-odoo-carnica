# -*- coding: utf-8 -*-
# from odoo import http


# class Porc(http.Controller):
#     @http.route('/porc/porc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/porc/porc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('porc.listing', {
#             'root': '/porc/porc',
#             'objects': http.request.env['porc.porc'].search([]),
#         })

#     @http.route('/porc/porc/objects/<model("porc.porc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('porc.object', {
#             'object': obj
#         })

