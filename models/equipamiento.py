# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Equipamiento(models.Model):
	_inherit = 'product.template',
	description = fields.Char(default="Modelo de equipamiento hospitalario")
