from odoo import models, fields, api

class item(models.Model):
  _name = 'recepcion.item'


  @api.one
  @api.depends('pbruto', 'tara')
  def calcula_pesoneto(self):
    if self.pbruto and self.tara is not False:
      self.pneto = self.pbruto - self.tara


  @api.one
  @api.depends('pneto')
  def calcula_peso_libra(self):
    self.pneto_libras = self.pneto*2.2046

  categoria = fields.Selection([
    ('Brosa B', 'Brosa B'),
    ('Brosa C', 'Brosa C'),
    ('Suri B', 'Suri B'),
    ('Suri C', 'Suri C'),
  ], default="Brosa B", string="Categoria")

  pbruto = fields.Float(string = "Peso Bruto")

  tara = fields.Float(string = "Tara")

  pneto = fields.Float(string = "Peso Neto", compute="calcula_pesoneto") 

  pneto_libras = fields.Float(string = "Peso Neto (lb)", compute="calcula_peso_libra") 

  embalaje = fields.Selection([
    ('Rafia', 'Rafia'),
    ('Yute', 'Yute'),
  ], default="Yute", string="Embalaje")

  color = fields.Selection([
    ('Blanco', 'Blanco'),
    ('Color', 'Color'),
  ], default="Color", string="Color")

  recepcion_planta_id = fields.Many2one('recepcion.recepcionplanta', string="Recepcion")