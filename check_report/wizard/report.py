# -*- coding: utf-8 -*-

from odoo import models, fields, api
from io import BytesIO
import base64
from odoo.exceptions import UserError

class check_report(models.TransientModel):
    _name = 'check_report_gen'
    _description = 'check_report.check_report'
    
    file_name = fields.Char(string='Nombre del archivo')
    archive = fields.Binary(string="Archivo")

    partner_id = fields.Many2one('res.partner', string="Cliente/Proveedor")
    ref = fields.Many2one('account.payment', string="Número de cheque")
    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string='Date to', default=fields.Date.today)
    check_from = fields.Char(string="Check from")
    check_to = fields.Char(string="Check to")

    report_type = fields.Selection([('1', 'Seleccionar por fecha'), (
        '2', 'Buscar por beneficiario'), ('3', 'Buscar por número de cheque'), ('4', 'Cheques no numerados')], default='1')

    def action_print_report(self):
        appointments = self.env['account.payment'].search(
            [('state', '=', 'posted'), ('payment_method_id.id', '=', '4')])
    def action_get_attachment(self):
        appointments = self.env['account.payment'].search(
            [('state', '=', 'posted'), ('payment_method_id.id', '=', '4')])
        domain = []
        checkFields = ['partner_id', 'date', 'name','amount','check_number']
        # busqueda por fecha
        
        if self.report_type == '1':

            domain=[('date', '>=', self.date_from),
                          ('date', '<=', self.date_to)]

         # busqueda por beneficiario
        if self.report_type == '2':
            
            if self.partner_id.id:
                domain.append(('partner_id', 'in', self.partner_id.ids))
            if self.date_from != '':
                domain.append(('date', '>=', self.date_from))
            if self.date_to != '':
                domain.append(('date', '<=', self.date_to))
           
        if self.report_type == '3':
            if self.partner_id.id:
                domain.append(('partner_id', 'in', self.partner_id.ids))
            if self.check_from != '':
                domain.append(('check_number', '>=', self.check_from))
            if self.check_to != '':
                domain.append(('check_number', '<=', self.check_to))
           
            ##cheques no numerados
        if self.report_type == '4':
            domain.append(('check_number','=',False))

        checkRecords = appointments.search_read(domain, checkFields)

        data = {
            'checkRecords': checkRecords,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'check_from':self.check_from,
            'check_to':self.check_to,
        }
        file_name = 'Check Report.pdf'

        pdf = self.env.ref('check_report.report_custom')._render_qweb_pdf(self.ids,data=data)
  
        
        b64_pdf = base64.b64encode(pdf[0])

        wiz_id = self.env['descargar.hojas'].create({'file_name': file_name, 'archive': b64_pdf})
        return {
            'name': "Descargar Archivo",
            'type': 'ir.actions.act_window',
            'res_model': 'descargar.hojas',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': wiz_id.id,
            'views': [(False, 'form')],
            'target': 'new',
        }
