# -*- coding: utf-8 -*-
# from odoo import http


# class Penalitzacio(http.Controller):
#     @http.route('/penalitzacio/penalitzacio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/penalitzacio/penalitzacio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('penalitzacio.listing', {
#             'root': '/penalitzacio/penalitzacio',
#             'objects': http.request.env['penalitzacio.penalitzacio'].search([]),
#         })

#     @http.route('/penalitzacio/penalitzacio/objects/<model("penalitzacio.penalitzacio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('penalitzacio.object', {
#             'object': obj
#         })

