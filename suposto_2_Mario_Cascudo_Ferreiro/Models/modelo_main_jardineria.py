from odoo import models,fields
class ModeloMainJardineria(models.Model):
    _name = 'modelo.main.jardineria'
    _description = 'Datos de un cortacesped'
    nome=fields.Char('Nombre',required = True)
    identificador = fields.Integer('Identificador',required = True)
    anho_fabricacion = fields.Integer('Año de fabricacion',required = True)
    fecha_compra = fields.Date('Fecha de compra',required = True)
    color = fields.Selection([('a','Verde'),('b','Rojo'),('c','Naranja')])
    horas_trabajo = fields.Integer('Horas de trabajo')
    numero_cuchillas = fields.Integer('Numero de cuchillas')
    diametro_cuchillas = fields.Float('Diametro de cuchillas')
    fecha_ultimo_cambio_cuchillas = fields.Date('Fecha del ultimo cambio de cuchillas', required = True)
    tipo_aceite_motor = fields.Selection([('a','5W-30'),('b','5W-40'),('c','10W-30')])
    fecha_ultimo_cambio_aceite = fields.Date('Fecha ultimo cambio de aceite', required = True)
    horas_trabajo_ultimo_cambio_aceite = fields.Integer('Horas de trabajo del ultimo cambio de aceite')
    tipo_ruedas_delanteras = fields.Selection([('a','250 * 90'), ('b','44710-VE0-800ZA')])
    tipo_ruedas_traseras = fields.Selection([('a','42810-VB5-F43ZB'),('b','42710-VE0-800ZA')])
    fecha_ultimo_cambio_ruedas_delanteras = fields.Date('Fecha ultimo cambio ruedas delanteras', required = True)
    fecha_ultimo_cambio_ruedas_traseras = fields.Date('Fecha ultimo cambio ruedas traseras', required = True)
    se_ha_averiado_alguna_vez = fields.Boolean('Ha tenido alguna averia?')
    notas_averias = fields.Char('Notas sobre averias')