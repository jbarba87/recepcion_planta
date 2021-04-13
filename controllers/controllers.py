# -*- coding: utf-8 -*-
from odoo import http

# class Recepcion(http.Controller):
#     @http.route('/recepcion/recepcion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recepcion/recepcion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recepcion.listing', {
#             'root': '/recepcion/recepcion',
#             'objects': http.request.env['recepcion.recepcion'].search([]),
#         })

#     @http.route('/recepcion/recepcion/objects/<model("recepcion.recepcion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recepcion.object', {
#             'object': obj
#         })