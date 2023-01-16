# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPrueba(http.Controller):
#     @http.route('/modulo_prueba/modulo_prueba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_prueba/modulo_prueba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_prueba.listing', {
#             'root': '/modulo_prueba/modulo_prueba',
#             'objects': http.request.env['modulo_prueba.modulo_prueba'].search([]),
#         })

#     @http.route('/modulo_prueba/modulo_prueba/objects/<model("modulo_prueba.modulo_prueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_prueba.object', {
#             'object': obj
#         })
