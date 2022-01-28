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

    length = fields.Float(string='Length', compute='_length')
    width  = fields.Float(string='Width', compute='_width')
    heigth  = fields.Float(string='Heigth', compute='_heigth')
    m2 = fields.Float(string='m2', compute='_total_m2')

    active = fields.Boolean(string='Active', required=True, default=True)

    @api.depends('nave_id')
    def _total_m2(self):
        for record in self:
            if record.nave_id:
                for nave in record.nave_id:
                    record.m2 = nave.length*nave.width*nave.heigth
            else:
                record.m2 = 0

    @api.depends('nave_id')
    def _length_m2(self):
        for record in self:
            if record.nave_id:
                for nave in record.nave_id:
                    record.length = nave.length
            else:
                record.length = 0
                
    @api.depends('nave_id')
    def _total(self):
        for record in self:
            if record.nave_id:
                for nave in record.nave_id:
                    record.width = nave.width
            else:
                record.width = 0
                
    @api.depends('nave_id')
    def _total_m2(self):
        for record in self:
            if record.nave_id:
                for nave in record.nave_id:
                    record.height = nave.heigth
            else:
                record.heigth = 0
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100