# -*- coding: utf-8 -*-
# from odoo import http


# class TypeContrat(http.Controller):
#     @http.route('/type_contrat/type_contrat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/type_contrat/type_contrat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('type_contrat.listing', {
#             'root': '/type_contrat/type_contrat',
#             'objects': http.request.env['type_contrat.type_contrat'].search([]),
#         })

#     @http.route('/type_contrat/type_contrat/objects/<model("type_contrat.type_contrat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('type_contrat.object', {
#             'object': obj
#         })
