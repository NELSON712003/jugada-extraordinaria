"""Ver_Videos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from django.contrib.auth.decorators import login_required

from .views import Home , Ver_Video_Single , Api_Videos_User , Api_Top_Videos , All_Videos_View , Api_All_Videos_Publicos , Api_Busqueda_Videos

urlpatterns = [
	path('home/', login_required( Home.as_view() ) , name="home"),
    path('api_videos/', login_required( Api_Videos_User.as_view() ) ),
    path('api_top_videos/', login_required( Api_Top_Videos.as_view() ) ),
    path('ver_video/<int:id_video>', login_required( Ver_Video_Single.as_view() ) , name='ver_video_single' ),
    path('all_videos_view/', login_required( All_Videos_View.as_view() ) , name='all_videos_view' ),
    path('api_all_videos_public/', login_required( Api_All_Videos_Publicos.as_view() ) , name='api_all_videos_public' ),
    path('api_search_videos_public/', login_required( Api_Busqueda_Videos.as_view() ) , name='api_search_videos_public' ), 
]
