from django.db import models

class Origen_Video( models.Model ):
	id = models.AutoField( primary_key=True )
	nombre = models.CharField( max_length=500 )	
	estructura_html = models.CharField( max_length=700 , blank=True )

	def __str__(self): #lo que se muestra de cada registro
		return ( str(self.id) + " - " + self.nombre )