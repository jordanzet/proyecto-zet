from django.db import models
from django.contrib.auth.models import User

FIDELIDAD = [
	('1', 'compra anual'),
	('2', 'compra mensual'),
	('3', 'compra semanal'),
	('4', 'Regular'),
	('5', 'Fiel'),
	('6', 'Muy Fiel'),
]

class Cliente(models.Model):
	usuario = models.ForeignKey(User)
	ruc = models.IntegerField()
	telefono = models.IntegerField()
	nivel_de_fidelidad = models.CharField(max_length=18, choices=FIDELIDAD, default='4')

	def __unicode__(self):
		return unicode(self.usuario)


