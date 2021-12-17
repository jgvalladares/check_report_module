# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.mail.wizard.mail_compose_message import _reopen
from odoo.exceptions import UserError
from odoo.tools.misc import get_lang


class CheckReportSend(models.TransientModel):
    _name = 'check_report_gen.send'
    #_inherits = {'mail.compose.message':'composer_id'}
    _description = 'Check Report Send'
    email_from=fields.Char(string="Email from")
    email_to=fields.Char(string="Email to")
    is_email = fields.Boolean('Email')
    invoice_without_email = fields.Text( string='invoice(s) that will not be sent')
    is_print = fields.Boolean('Print')
    printed = fields.Boolean('Is Printed', default=False)
    invoice_ids = fields.Char(string='Invoices')
    subir_archivo=fields.Binary()

   
    
