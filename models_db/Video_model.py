from datetime import datetime

from django.db import models

from django.contrib.auth.models import User
from .Origen_Video_model import Origen_Video
from .Estados_Video_model import Estado_Video

class Video( models.Model ):
	id = models.AutoField( primary_key=True )
	id_user = models.ForeignKey( User , on_delete= models.CASCADE )
	titulo = models.CharField( max_length=500 )
	direccion = models.CharField( max_length=500 )
	id_origen = models.ForeignKey( Origen_Video , on_delete= models.CASCADE )
	id_estado = models.ForeignKey( Estado_Video , on_delete= models.CASCADE )
	cantidad_reproducciones = models.PositiveIntegerField( default=0 )
	fecha_ingreso = models.DateTimeField( null=True, blank=True )
	imagen = models.ImageField( upload_to='app/static/img' , default='app/static/img/default_image_videos.jpg' )
