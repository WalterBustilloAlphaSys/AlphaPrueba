# -*- coding: utf-8 -*-
# from odoo import http


# class Chap6(http.Controller):
#     @http.route('/chap6/chap6/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chap6/chap6/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chap6.listing', {
#             'root': '/chap6/chap6',
#             'objects': http.request.env['chap6.chap6'].search([]),
#         })

#     @http.route('/chap6/chap6/objects/<model("chap6.chap6"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chap6.object', {
#             'object': obj
#         })
