from django.shortcuts import render , redirect
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout


class Login( View ):
	
	def get( self , request ):
		if request.user.is_authenticated:
			#Usuarios ya registrado
			return redirect( 'home' )
		return render( request ,'Login.html')

	def post( self , request ):
		#login user
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is not None:
			login(request, user)
			return redirect( 'home' )
		return render( request ,'Login.html')


class Logout( View ):
	def get( self , request ):
		logout(request) #Deslogueamos al user
		return redirect( 'login' )