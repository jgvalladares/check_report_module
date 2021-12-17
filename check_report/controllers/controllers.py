# -*- coding: utf-8 -*-
# from odoo import http


# class CheckReport(http.Controller):
#     @http.route('/check_report/check_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_report/check_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_report.listing', {
#             'root': '/check_report/check_report',
#             'objects': http.request.env['check_report.check_report'].search([]),
#         })

#     @http.route('/check_report/check_report/objects/<model("check_report.check_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_report.object', {
#             'object': obj
#         })
