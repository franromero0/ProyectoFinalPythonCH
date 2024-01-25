"""
URL configuration for proyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from gym import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
###########################################################
####                     PAGES                          ###
###########################################################
    ################ HOME ###################### 
    path('', views.inicio, name="Inicio" ),
    path('inicio/', views.inicio_login, name="Inicio login" ),
    
    ################ AUTENTICACION ###################### 
    path('login/', views.inicio_sesion, name="login"),
    path('signup/', views.registro, name="signup"),
    path('logout/', views.cerrar_sesion, name= "logout"),
    path('edit/profile/', views.update_profile, name= 'edit profile'),
    
    ################ VISTAS GENERALES ######################
    path('outdoor/', views.aire_libre, name="outdoor"), #Imagenes anchas y tiene para acceder a otra página
    path('gym/', views.gym, name="gym"),  # Para imagenes largas pero no tiene como para acceder a info
    path('about/', views.about, name="about"),
    
    
    
    
###########################################################
####                     CRUD                           ###
###########################################################


    ################ CREATE ######################
    path('add/event/', views.add_outdoor, name="newEvent"),# ------> Añadir un evento a futuro
    path('add/gym/', views.add_gym, name="new gym"),
    
    
    ################ READ ###################### 
    path('search/outdoor/', views.search_event, name="search event"),       # ---------> Ver todos los elementos del modelo OutDoor 
    path('search/outdoor/result', views.event_result, name="event result"), # ---------> Búsqueda de eventos de Trekking o Senderismos futuros
    path('search/gym/', views.search_gym, name="search gym"),
    path('search/gym/result/', views.gym_result, name="gym result"),
    path('activity/<int:event_id>/', views.single_outdoor, name= "single outdoor"),
    path('deports/<int:event_id>/', views.single_gym, name="single gym"),
    
    
    
    
   
    
    ################ UPDATE ######################
    
    path('edit/event/<int:event_id>/', views.update_event, name="update event"), #int:event_id para que busque por ID 
    path('edit/gym/<int:event_id>/', views.update_gym, name="update gym"), #int:event_id para que busque por ID
    path('update/avatar/', views.update_avatar, name="update avatar"),     
    
    ################ DELETE ######################  
    
    path('delete/event/<id_event>/', views.event_delete, name='delete event'),
    path('delete/gym/<id_event>/', views.gym_delete, name='delete gym'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)