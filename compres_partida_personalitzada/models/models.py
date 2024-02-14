# -*- coding: utf-8 -*-

from odoo import models, fields, api


class compres_partida_personalitzada(models.Model):
   _inherit = 'purchase.order'
   
   TipusPorc = fields.Many2one('tipu_porc.tipu_porc', string='Tipus Porc')
