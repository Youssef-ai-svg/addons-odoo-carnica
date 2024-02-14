# -*- coding: utf-8 -*-

from odoo import models, fields

class Cataleg(models.Model):
    _name = 'cataleg.cataleg'
    _description = 'cataleg.cataleg'

    tipuPorcObj = fields.Many2one('tipu_porc.tipu_porc', string='Tipus porc')
    tipusCategoriaObj = fields.Many2one('category.category', string='Categoria')
    Preu = fields.Float()