from odoo import models, fields
class ModeloMain(models.Model):
    _name = 'modelo.main'
    _description = 'Modelo principal del Módulo'
    NombreAlumno = fields.Char('Nombre',required = True)
    ApellidosAlumno = fields.Char('Apellidos',required = True)
    FechaNacimientoAlumno = fields.Date('Fecha de nacimiento',required = True)
    FechaMatriculacionAlumno = fields.Date('Fecha de martriculacion',required = True)
    FinalizoPrimerAño = fields.Boolean('Finalizó el primer año',required = True)
    FinalizoSegundoAño = fields.Boolean('Finalizó el segundo año',required = True)
    FinalizoCurso = fields.Boolean('Finalizó el curso',required = True)