from odoo import models,fields
class ModeloMainInheritJardineria(models.Model):
    _inherit = 'modelo.main.jardineria'

    tieneSeguro = fields.Boolean('Tiene seguro',required="True")
    compañiaAseguradora = fields.Selection([('a','allianz'),('b','mapfre'),('c','groupama'),('d','zurich')])
    numeroPoliza = fields.Integer('Numero de póliza', required = False)
    importeSeguro = fields.Float('Importe', required = False)
    dataSeguro = fields.Date('Fecha de seguro', required = False)
    contactoTomador = fields.Char('Contacto de tomador', required = False)

    telefonoContacto = fields.Integer('Teléfono de contacto', required = False)