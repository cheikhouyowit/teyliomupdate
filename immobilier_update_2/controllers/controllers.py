# -*- coding: utf-8 -*-
# from odoo import http


# class ImmobilierUpdate2(http.Controller):
#     @http.route('/immobilier_update_2/immobilier_update_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/immobilier_update_2/immobilier_update_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('immobilier_update_2.listing', {
#             'root': '/immobilier_update_2/immobilier_update_2',
#             'objects': http.request.env['immobilier_update_2.immobilier_update_2'].search([]),
#         })

#     @http.route('/immobilier_update_2/immobilier_update_2/objects/<model("immobilier_update_2.immobilier_update_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('immobilier_update_2.object', {
#             'object': obj
#         })
