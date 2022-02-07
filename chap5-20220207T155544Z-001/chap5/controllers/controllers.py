# -*- coding: utf-8 -*-
# from odoo import http


# class Chap5(http.Controller):
#     @http.route('/chap5/chap5/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chap5/chap5/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chap5.listing', {
#             'root': '/chap5/chap5',
#             'objects': http.request.env['chap5.chap5'].search([]),
#         })

#     @http.route('/chap5/chap5/objects/<model("chap5.chap5"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chap5.object', {
#             'object': obj
#         })
