from django.db import models
from django.contrib.auth.models import User

STATUS = [
	('activo', 'Activo'),
	('inactivo', 'Inactivo'),
	('despedido', 'despedido')
]

class JefeInventario(models.Model):
	usuario = models.ForeignKey(User)
	dni = models.IntegerField()
	telefono = models.IntegerField()
	status = models.CharField(max_length=8, choices=STATUS, default='activo')

	def __unicode__(self):
		return unicode(self.usuario) 		