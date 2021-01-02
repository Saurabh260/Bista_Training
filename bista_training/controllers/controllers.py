# -*- coding: utf-8 -*-
# from odoo import http


# class BistaTraining(http.Controller):
#     @http.route('/bista/bista/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bista/bista/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bista.listing', {
#             'root': '/bista/bista',
#             'objects': http.request.env['bista.bista'].search([]),
#         })

#     @http.route('/bista/bista/objects/<model("bista.bista"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bista.object', {
#             'object': obj
#         })
