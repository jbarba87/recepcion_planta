from datetime import datetime

from odoo import models, fields, api

class recepcion_planta(models.Model):
  _name = 'recepcion.recepcionplanta'
  #_rec_name = "identificacion"
  item = fields.One2many('recepcion.item', 'recepcion_planta_id', string="Items")
  fechaingreso = fields.Date(string ="Fecha de ingreso", default=datetime.now().strftime('%Y-%m-%d'))

  procedencia = fields.Char(size=30)

  responsable = fields.Many2one('res.partner', string = "Responsable")
  sede = fields.Selection([
    ('Ayacucho', 'Ayacucho'),
    ('Cusco', 'Cusco'),
  ], default="Ayacucho", string="Sede")

  total_peso_bruto = fields.Float(string="Peso bruto", compute="calcula_peso_bruto")

  total_peso_bruto_brosab = fields.Float(string="Peso Brosa B", compute="calcula_peso_bruto")
  total_peso_bruto_brosac = fields.Float(string="Peso Brosa C", compute="calcula_peso_bruto")
  total_peso_bruto_surib = fields.Float(string="Peso Suri B", compute="calcula_peso_bruto")
  total_peso_bruto_suric = fields.Float(string="Peso Suri C", compute="calcula_peso_bruto")


  @api.one
  @api.depends('item.pbruto')
  def calcula_peso_bruto(self):
    if self.item is not False:
      acc_brosab = 0
      acc_brosac = 0
      acc_surib = 0
      acc_suric = 0
      for item in self.item:
        if item.categoria == 'Brosa B':
          acc_brosab += item.pbruto
        if item.categoria == 'Brosa C':
          acc_brosac += item.pbruto
        if item.categoria == 'Suri B':
          acc_surib += item.pbruto
        if item.categoria == 'Suri C':
          acc_suric += item.pbruto
      
      self.total_peso_bruto = acc_brosab + acc_brosac + acc_surib + acc_suric
      self.total_peso_bruto_brosab = acc_brosab
      self.total_peso_bruto_brosac = acc_brosac
      self.total_peso_bruto_surib = acc_surib
      self.total_peso_bruto_suric = acc_suric