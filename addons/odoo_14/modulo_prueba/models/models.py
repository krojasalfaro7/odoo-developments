# -*- coding: utf-8 -*-

from odoo import models, fields


class ModuloPrueba(models.Model):
    _name = 'modulo.prueba'
    _description = 'Este es un modulo de prueba'

    name = fields.Char(string="Nombre", required=True)
    value = fields.Integer()
    description = fields.Text()
    apellido = fields.Char(string="Otro paellido")
