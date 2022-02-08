# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBookCopy(models.Model):
    
    _name = 'library.book.copy'
    _inhert = 'my:library.my_library'
    _description = 'Library Book´s copy'
    
    