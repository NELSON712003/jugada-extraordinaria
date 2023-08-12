from django.contrib import admin

from .Origen_Video_model import Origen_Video
from .Video_model import Video
from .Estados_Video_model import Estado_Video


def imagen(self, obj):
	return format_html('<img src="{}" />'.format( obj.image.url ))

#image_tag.short_description = 'Image'


@admin.register( Origen_Video )
class Origen_VideoAdmin(admin.ModelAdmin):
	list_display = ( "id" ,"nombre", "estructura_html")


@admin.register( Estado_Video )
class Estado_VideoAdmin(admin.ModelAdmin):
	list_display = ( "id","nombre", )


@admin.register( Video )
class VideoAdmin(admin.ModelAdmin):
	list_display = ( 'id','id_user','titulo','direccion','id_origen','id_estado', 'imagen' , 'cantidad_reproducciones' , 'fecha_ingreso' )
	#fields = ( 'id_user','titulo','direccion','id_origen','id_estado','imagen' )
	fields = ( 'titulo','direccion','id_origen','id_estado','imagen' ) #Ahora el id_user se ingresa en save_model

	def save_model(self, request, obj , form , change ): #Sobreescritura de metodo guardado
		obj.id_user = request.user
		super( VideoAdmin , self).save_model( request, obj, form, change )

	def get_queryset(self, request ): #Sobreescritura de metodo mostrar lista de objetos
		if request.user.is_superuser:
			return Video.objects.all()
		return Video.objects.filter( id_user=request.user )