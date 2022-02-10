# -*- coding: utf-8 -*-
from odoo import models, fields
class ModeloProba(models.Model):
	_name = 'modelo.proba'
	_description = 'Modelo de proba'
	name = fields.Char('Description', required=True)
	is_done = fields.Boolean('Proba Feita?')
	num_proba = fields.Integer('Numero de proba?')