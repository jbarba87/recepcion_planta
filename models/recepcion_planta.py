

from odoo import models, fields, api

class recepcion_planta(models.Model):
  _name = 'recepcion.recepcionplanta'
  #lista_esquilas = fields.One2many('coop.esquila', 'camelido_id', string="Esquilas")

  item = fields.One2many('recepcion.item', 'recepcion_planta_id', string="Items")
  fechaingreso = fields.Date(string ="Fecha de ingreso")

  responsable = fields.Many2one('res.partner', string = "Responsable")
  sede = fields.Selection([
    ('Ayacucho', 'Ayacucho'),
    ('Cusco', 'Cusco'),
  ], default="Ayacucho", string="Sede")

  