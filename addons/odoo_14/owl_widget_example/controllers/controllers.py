# -*- coding: utf-8 -*-
# from odoo import http


# class OwlWidgetExample(http.Controller):
#     @http.route('/owl_widget_example/owl_widget_example/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_widget_example/owl_widget_example/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_widget_example.listing', {
#             'root': '/owl_widget_example/owl_widget_example',
#             'objects': http.request.env['owl_widget_example.owl_widget_example'].search([]),
#         })

#     @http.route('/owl_widget_example/owl_widget_example/objects/<model("owl_widget_example.owl_widget_example"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_widget_example.object', {
#             'object': obj
#         })
