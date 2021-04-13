from odoo import models, fields, api

class item(models.Model):
  _name = 'recepcion.item'

  categoria = fields.Selection([
    ('Brosa B', 'Brosa B'),
    ('Brosa C', 'Brosa C'),
    ('Suri B', 'Suri B'),
    ('Suri C', 'Suri C'),
  ], default="Brosa B", string="Categoria")

  pbruto = fields.Float(string = "Peso Bruto")

  tara = fields.Float(string = "Tara")

  pneto = fields.Float(string = "Peso Neto") 

  embalaje = fields.Selection([
    ('Rafia', 'Rafia'),
    ('Yute', 'Yute'),
  ], default="Yute", string="Embalaje")

  color = fields.Selection([
    ('Blanco', 'Blanco'),
    ('Color', 'Color'),
  ], default="Color", string="Color")

  recepcion_planta_id = fields.Many2one('recepcion.recepcionplanta', string="Recepcion")