# -*- coding: utf-8 -*-

from collections import defaultdict
from odoo import models, fields, api

class PersonalitzarCompra(models.Model):
    _inherit = 'purchase.order'

    Quantitat = fields.Float()
    TipuPorc = fields.Many2one('tipu_porc.tipu_porc', string="TipuPorc")
    porcsLlista = fields.One2many('porc.porc', 'edicio_compres_id', string='Porc')


    def assign_button_function(self):
        self.add_porc_to_order_lines()

    def add_porc_to_order_lines(self):
        category_qty = defaultdict(float)
        category_price = defaultdict(float)
        category_count = defaultdict(int)

        # Agrupar y sumar las cantidades de productos y precios por categoría
        for porc in self.porcsLlista:
            category_key = (porc.product_id.id, porc.price_unit)  # Usar una tupla como clave de agrupación
            category_qty[category_key] += porc.product_qty
            category_price[category_key] += porc.price_unit
            category_count[category_key] += 1

        existing_lines = self.env['purchase.order.line'].search([('order_id', '=', self.id)])
        existing_category_keys = existing_lines.mapped(lambda x: (x.product_id.id, x.price_unit))

        for category_key, qty in category_qty.items():
            if category_key in existing_category_keys:
                existing_line = existing_lines.filtered(lambda x: (x.product_id.id, x.price_unit) == category_key)
                existing_line.product_qty += qty
                existing_line.price_unit = category_price[category_key] / category_count[category_key]
            else:
                product_vals = {
                    'order_id': self.id,
                    'product_id': category_key[0],
                    'name': self.env['product.product'].browse(category_key[0]).name,
                    'product_qty': qty,
                    'price_unit': category_price[category_key] / category_count[category_key],
                    # 'TipuPorc': category_key[2]  # Pasamos el TipuPorc como valor

                }
                self.env['purchase.order.line'].create(product_vals)
