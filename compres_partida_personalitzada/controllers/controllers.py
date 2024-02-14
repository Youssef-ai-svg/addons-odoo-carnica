# -*- coding: utf-8 -*-
# from odoo import http


# class CompresPartidaPersonalitzada(http.Controller):
#     @http.route('/compres_partida_personalitzada/compres_partida_personalitzada', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compres_partida_personalitzada/compres_partida_personalitzada/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('compres_partida_personalitzada.listing', {
#             'root': '/compres_partida_personalitzada/compres_partida_personalitzada',
#             'objects': http.request.env['compres_partida_personalitzada.compres_partida_personalitzada'].search([]),
#         })

#     @http.route('/compres_partida_personalitzada/compres_partida_personalitzada/objects/<model("compres_partida_personalitzada.compres_partida_personalitzada"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compres_partida_personalitzada.object', {
#             'object': obj
#         })

