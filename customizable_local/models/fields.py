from odoo import models, fields,api, _
from odoo.exceptions import UserError
import base64
import requests
import datetime
from odoo.exceptions import ValidationError




class InheritProductVariant(models.Model):
    _inherit = 'product.product'

    def create_code(self):
         if not self['own_ref_no']:
            self['own_ref_no']=self.env["ir.sequence"].next_by_code('product.ref.code')
               
        
