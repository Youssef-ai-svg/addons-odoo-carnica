# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class penalitzacio(models.Model):
    _name = 'penalitzacio.penalitzacio'
    _description = 'penalitzacio.penalitzacio'

    name = fields.Float(string="Max Pes")
    MinPes = fields.Float(string="Min Pes")
    tipusCategoriaObj = fields.Many2one('category.category', string='Categoria')
    tipusporcObj = fields.Many2one('tipu_porc.tipu_porc', string='Tipus porc')
    @api.constrains('name', 'MinPes')
    def _check_min_max_pes(self):
        for rec in self:
            if rec.MinPes > rec.name:
                rec.MinPes = rec.name - 1
                raise ValidationError("El valor mínimo no puede ser mayor que el valor máximo. Se ha ajustado automáticamente.")