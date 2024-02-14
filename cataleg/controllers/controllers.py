# -*- coding: utf-8 -*-
# from odoo import http


# class Cataleg(http.Controller):
#     @http.route('/cataleg/cataleg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cataleg/cataleg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cataleg.listing', {
#             'root': '/cataleg/cataleg',
#             'objects': http.request.env['cataleg.cataleg'].search([]),
#         })

#     @http.route('/cataleg/cataleg/objects/<model("cataleg.cataleg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cataleg.object', {
#             'object': obj
#         })

