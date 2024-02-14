# -*- coding: utf-8 -*-

from odoo import models, fields, api


class porc(models.Model):
    _name = 'porc.porc'
    _description = 'porc.porc'

    product_id = fields.Many2one('product.product', string='Producto', default=lambda self: self._get_default_product(), readonly=True)
    name = fields.Many2one('category.category', string="Categoria")
    Pes = fields.Float()
    price_unit = fields.Float(store=True, string = "Preu")
    edicio_compres_id = fields.Many2one('purchase.order', string='Orden de Compra', invisible=True)
    product_qty = fields.Float(string='Cantidad', default=1, readonly=True)
    Penalitzacio = fields.Many2one('penalitzacio.penalitzacio', invisible=True)
    # TipuPorc = fields.Many2one('tipu_porc.tipu_porc', string="TipuPorc")  # Nuevo campo
    
    # @api.onchange('name', 'Pes', 'TipuPorc')  # Actualizamos el onchange para incluir TipuPorc
    # def _onchange_name(self):
    #     if self.name:
    #         self.price_unit = self.name.Preu * self.Pes

    #         max_weight = self.Penalitzacio.name
    #         min_weight = self.Penalitzacio.MinPes

    #         if self.Pes > max_weight or self.Pes < min_weight:
    #             self.price_unit -= self.price_unit * 0.005
    @api.onchange('name', 'Pes', 'TipuPorc')  # Actualizamos el onchange para incluir TipuPorc
    def _onchange_name(self):
        if self.Pes:
            self.price_unit = self.name.Preu * self.Pes
    def _get_default_product(self):
        porc_product = self.env['product.product'].search([], limit=1)
        return porc_product.id if porc_product else False

