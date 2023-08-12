from django.db import models

class Estado_Video( models.Model ):
	id = models.AutoField( primary_key=True )
	nombre = models.CharField( max_length=500 )

	def __str__(self): #lo que se muestra de cada registro
		return ( str(self.id) + " - " + self.nombre )