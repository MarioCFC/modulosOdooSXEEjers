from odoo import models,fields
class ModeloMainInheritJardineria(models.Model):
    _inherit = 'modelo.main.jardineria'
    compañiaAseguradora = fields.Selection([('a','allianz'),('b','mapfre'),('c','groupama'),('d','zurich')])
    numeroPoliza = fields.Integer('Numero de póliza', required = True)
    importeSeguro = fields.Float('Importe', required = True)
    dataSeguro = fields.Date('Fecha de seguro', required = True)
    contactoTomador = fields.Char('Contacto de tomador', required = True)
