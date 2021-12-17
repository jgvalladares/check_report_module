# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class check_report(models.Model):
#     _name = 'check_report.check_report'
#     _description = 'check_report.check_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):     -> self es tipo diccionario de información
#         for record in self:
#             record.value2 = float(record.value) / 100
