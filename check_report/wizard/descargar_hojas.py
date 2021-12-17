# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class DescargarHojas(models.TransientModel):
    _name = 'descargar.hojas'
    _description = 'Modelo para descargar archivos'

    file_name = fields.Char(string='Nombre del archivo')
    archive = fields.Binary(string="Archivo")
    email_from=fields.Char(string="Email from")
    email_to=fields.Char(string="Email to")
    invoice_without_email = fields.Text( string='Mensaje')
    composer_id = fields.Many2one('mail.compose.message', string='Composer', required=True, ondelete='cascade')
    
    def get_report(self):

        res_ids = self._context.get('active_ids')
        composer = self.env['mail.compose.message'].create({
            'composition_mode': 'comment' if len(res_ids) == 1 else 'mass_mail',
        })
        ir_values = {
       'name': "Customer Report",
       'type': 'binary',
       'datas': self.archive,
       'store_fname': self.archive,
       'mimetype': 'application/x-pdf',
        }
        data_id = self.env['ir.attachment'].create(ir_values)

        mail_content = "Envio reporte"+self.invoice_without_email
        main_content = {
        'subject': "REPORTE DE CHEQUES",
        'author_id': self.env.user.partner_id.id,
        'body': mail_content,
        'email_to': self.email_to,
        'attachment_ids': [(6, 0, [data_id.id])]
                                        
        }
        a=self.composer_id.send_mail(mail_content)
        print(a)
        
