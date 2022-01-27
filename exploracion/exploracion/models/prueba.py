 #-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Prueba(models.Model):
    _name = 'exploracion.prueba'
    _description = 'Mision prueba'

    name=fields.Char(string='Identifier', required=True)
    description =fields.Text(string='Especifica los detalles de una misión espacial')
    
    origen = fields.Selection(string='Origen',
                             selection=[('tierra','Tierra')],
                             copy=False, default='tierra')
    
    destino = fields.Selection(string='Destino',
                             selection=[('tierra','Tierra'),
                                        ('sol','Sol'),
                                        ('mercurio','Mercurio'),
                                        ('venus','Venus'),
                                        ('luna','Luna'),
                                        ('marte','Marte'),
                                        ('jupiter','Júpiter'),
                                        ('saturno','Saturno'),
                                        ('urano','Urano'),
                                        ('neptuno','Neptuno'),
                                        ('pluton','Plutón')],
                             copy=False, default='luna')
    
    fecha_lanzamiento  = fields.Date(string='Fecha de Lanzamiento', required=True)
    fecha_retorno      = fields.Date(string='Fecha de Retorno')
    
    nave_id = fields.Many2one(comodel_name='exploracion.nave', string='Nave',
                             ondelete='cascade',
                             required = True)
    
    fligth_price = fields.Float(string = "Precio vuelo comercial")

    length = fields.Float(string='Length', required=True)
    width  = fields.Float(string='Width', required=True)
    heigth  = fields.Float(string='Heigth', required=True)
    m2 = fields.Float(string='m2', Compute=True)

    active = fields.Boolean(string='Active', required=True, default=True)

    @api.depends('lenght','width','height')
    def _value_m2(self):
        for record in self:
            record.m2 = float(record.length*record.width*record.height)
            
        
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100