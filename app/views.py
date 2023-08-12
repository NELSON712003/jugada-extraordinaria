import os

from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.views import View
from django.core import serializers

from models_db.Video_model import Video
from models_db.Origen_Video_model import Origen_Video
from models_db.Estados_Video_model import Estado_Video

class Home( View ):

	def get( self , request ):
		return render( request , 'home.html')

class Api_Videos_User( View ):

	def get( self , request ):
		request_data = request.GET.dict()
		
		all_videos_user = Video.objects.filter( id_user=request.user.id ).select_related("id_origen","id_user","id_estado")
		all_videos_user = all_videos_user[int(request_data["limite_inferior"]):int(request_data["limite_superior"])]
		
		#--Serializador -->>
		videos_user = []
		for video in all_videos_user:

			videos_user.append( {
				"id_video": video.id,
				"username": video.id_user.username,
				"titulo": video.titulo ,
				"direccion": video.direccion,
				"cantidad_reproducciones":video.cantidad_reproducciones,
				"fecha_ingreso":video.fecha_ingreso,
				"Origen_Video":{
								"nombre":video.id_origen.nombre 
								},
				"Estado_Video":{"nombre":video.id_estado.nombre},
				"imagen": request.build_absolute_uri( video.imagen.url )
			} )
		#----------------->>

		return JsonResponse( {"videos_user": videos_user } )
	
class Api_Top_Videos( View ):

	def get( self , request ):
		request_data = request.GET.dict()

		all_videos_public_users = Video.objects.filter( id_estado__nombre="Publico" ).select_related("id_origen","id_user","id_estado").order_by('-cantidad_reproducciones')
		all_videos_public_users = all_videos_public_users[int(request_data["limite_inferior"]):int(request_data["limite_superior"])]
		
		#--Serializador -->>
		top_videos = []
		for video_public in all_videos_public_users:
			top_videos.append( {
				"id_video": video_public.id,
				"username": video_public.id_user.username,
				"titulo": video_public.titulo , "direccion": video_public.direccion,
				"cantidad_reproducciones": video_public.cantidad_reproducciones,
				"fecha_ingreso": video_public.fecha_ingreso,
				"Origen_Video":{
								"nombre": video_public.id_origen.nombre
								},
				"Estado_Video":{"nombre": video_public.id_estado.nombre},
				"imagen": request.build_absolute_uri( video_public.imagen.url )
			} )
		#----------------->>

		return JsonResponse( {"top_videos": top_videos } )

class Api_All_Videos_Publicos( View ):

	def get( self , request ):
		request_data = request.GET.dict()

		all_videos_public_users = Video.objects.filter( id_estado__nombre="Publico" ).order_by('-cantidad_reproducciones')
		#all_videos_public_users = all_videos_public_users[ int(request_data["limite_inferior"]) : int(request_data["limite_superior"]) ]
		
		#--Serializador -->>
		all_videos = []
		for video_public in all_videos_public_users:
			all_videos.append( {
				"id_video": video_public.id,
				"username": video_public.id_user.username,
				"titulo": video_public.titulo , "direccion": video_public.direccion,
				"cantidad_reproducciones": video_public.cantidad_reproducciones,
				"fecha_ingreso": video_public.fecha_ingreso,
				"Origen_Video":{
								"nombre": video_public.id_origen.nombre
								},
				"Estado_Video":{"nombre": video_public.id_estado.nombre},
				"imagen": request.build_absolute_uri( video_public.imagen.url )
			} )
		#----------------->>

		return JsonResponse( {"all_videos": all_videos } )

class Api_Busqueda_Videos( View ):
	def get ( self , request ):
		request_data = request.GET.dict()
		print( request_data["nombre_video_search"] )
		all_videos_search_public = Video.objects.filter( titulo__startswith=request_data["nombre_video_search"] )
		#all_videos_public_users = all_videos_public_users[ int(request_data["limite_inferior"]) : int(request_data["limite_superior"]) ]
		
		#--Serializador -->>
		all_videos = []
		for video_public in all_videos_search_public:
			all_videos.append( {
				"id_video": video_public.id,
				"username": video_public.id_user.username,
				"titulo": video_public.titulo , "direccion": video_public.direccion,
				"cantidad_reproducciones": video_public.cantidad_reproducciones,
				"fecha_ingreso": video_public.fecha_ingreso,
				"Origen_Video":{
								"nombre": video_public.id_origen.nombre
								},
				"Estado_Video":{"nombre": video_public.id_estado.nombre},
				"imagen": request.build_absolute_uri( video_public.imagen.url )
			} )
		#----------------->>

		return JsonResponse( {"search_videos": all_videos } )


class Ver_Video_Single( View ):
	
	def get( self , request , id_video ):
		
		video = Video.objects.filter( id=id_video ).select_related("id_origen","id_user","id_estado")
		

		if len( video ) > 0:
			video = video[0]
			
			#----------------------------->>>>>>>>>>>>>>>>>
			# Aumentamos +1 a la cantidad de reproducciones del video
			video.cantidad_reproducciones += 1
			video.save()
			#----------------------------->>>>>>>>>>>>>>>>>

			if ( video.id_estado.nombre == "Publico" ) or ( video.id_estado.nombre == "Privado" and video.id_user.id == request.user.id ):
				#Permitimos el acceso a cualquier usuario o solo al usuario al que le pertenece (privado)
				data_video = {
					"id_video": video.id,
					"username": video.id_user.username,
					"titulo": video.titulo ,
					"direccion": video.direccion,
					"cantidad_reproducciones":video.cantidad_reproducciones,
					"fecha_ingreso":video.fecha_ingreso,
					"Origen_Video":{
									"nombre":video.id_origen.nombre
									},
					"Estado_Video":{"nombre":video.id_estado.nombre},
				}

				return render( request , 'single.html' , data_video )

		return redirect('home') #Redireccionamos al inicio



class All_Videos_View( View ):

	def get( self , request ):
		return render( request , 'all_videos.html')