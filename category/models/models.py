# -*- coding: utf-8 -*-

from odoo import models, fields, api


class category(models.Model):
    _name = 'category.category'
    _description = 'category.category'

    name = fields.Char(string = "Categoria")
    Preu = fields.Float()
