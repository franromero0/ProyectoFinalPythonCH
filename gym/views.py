from django.shortcuts import render
from .forms import *
from .models import *


# Funciones para la autenticacion
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



############################################################
#                   Vistas de autenticacion                #
############################################################

def inicio_login(request):  #Poner que cuando necesite loguear 
    return render(request, "gym/index_1.html") # Esta vista mostrara el inicio con los botones para registrarse o loguearse 

@login_required
def inicio(request):
    
    return render(request, "gym/index_2.html")


def registro(request):
    if request.method == "POST":
        formulario = RegistrarUsuario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            name = info['first_name']
            formulario.save()
            usuario = info['username']
            pw = info['password1']
            user_actual = authenticate(username=usuario,password=pw)
            if user_actual is not None:
                login(request,user_actual)
                
                return render(request,'registros/create_avatar.html')           
            else:           
                return render(request,"registros/registro_error.html", {'mensaje':"Error los datos no son correctos"})
        else:            
            return render(request,"registros/registro_error.html", {'mensaje':"Error los datos no son correctos"})             
    else:
        formulario = RegistrarUsuario()
    return render(request,"registros/registro.html", {'form':formulario})

@login_required
def update_avatar(request):
    
    if request.method=="POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo_avatar = Avatar(usuario=request.user,imagen=info['imagen']) 
            nuevo_avatar.save()
            name = request.user.first_name
            return render(request,"gym/index_2.html", {'mensaje': f"Bienvenido/a a mi web, {name}"})
    else:
        formulario = AvatarForm()
    return render(request,'registros/add_avatar.html', {"form":formulario})


def inicio_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationFormulario(request, data = request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = info['username']
            pw = info['password']
            user_actual = authenticate(username=usuario,password=pw)
            
            if user_actual is not None:
                login(request,user_actual)
                return render(request, "gym/index_2.html", {"mensaje": f"Hola de nuevo, {usuario}"})
            else:
                return render(request,'gym/index_2.html', {",mensaje": f"Error al iniciar sesión {usuario}"})
    else: 
        formulario = AuthenticationFormulario()
    return render(request,"registros/inicio_sesion.html", {'form': formulario})


@login_required
def update_profile(request):
    usuario_actual = request.user   #Vemos cual ese el usuario actual --> request.user vemos el usuario que actualemente esta registrado
    if request.method == "POST": #Click en el boton editar
        formulario = EditarUsuario(request.POST) #Tengo la informacion   Podemos usar UserCreationForm tmb pero ese es personalizado
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            usuario_actual.first_name = info["first_name"]
             #Del dict info buscamos lo que escribio en cada campo y reemplazamos el que ya existe con el .first_name por ejemplo (es el nombre de los campos del form o DB)
            usuario_actual.email = info["email"]
            usuario_actual.save()
             
            return render(request,"gym/index_2.html")
    
    else:
        formulario = EditarUsuario(initial={"first_name":usuario_actual.first_name,"email":usuario_actual.email, "username":usuario_actual.username})
    return render(request,'registros/update_profile.html',{"form":formulario})

    

@login_required
def cerrar_sesion(request): #Manera de cerrar sesion, debe estar vinculado la URL con el boton
    logout(request)
    return render(request, "gym/index_1.html")





############################################################
#                         PAGES                            #
############################################################

# About, un poco sobre mí y la empresa
@login_required
def about(request):
    return render(request, 'gym/Aabout.html')



############################################################
#Agregar actividad al aire libre que se mostrará en la page#   -----> CREATE
############################################################

@login_required
def add_outdoor(request):
    if request.method == "POST":
        formulario = OutDoorForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo_evento = OutDoor(deport=info["deport"],lugar_salida=info["lugar_salida"],titulo_evento=info["titulo_evento"],description=info["description"],image=info['image'],date=info["date"],short_description=info["short_description"])
            nuevo_evento.save()
            actividades = OutDoor.objects.all()            
            return render(request,"gym/Aaire_libre.html",{'events':actividades})
    else:
        formulario = OutDoorForm()
               
    return render(request, "gym/add_outdoor.html", {"form":formulario} )



@login_required
def add_gym(request):
    if request.method == "POST":
        formulario = GymForm(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nuevo_evento = Gym(activity=info["activity"],image=info["image"],description=info["description"],days=info["days"],hour=info['hour'],prof=info["prof"],place=info["place"])
            nuevo_evento.save() 
            actividades = Gym.objects.all()           
            return render(request,"gym/Agimnasio.html",{'events':actividades})
    else:
        formulario = GymForm()        
    return render(request, "gym/add_gym.html", {"form":formulario} )


#############################################################
# Editar actividad al aire libre que se mostrará en la page #  -----> UPDATE
#############################################################

@login_required
def update_event(request,event_id):
        event = OutDoor.objects.get(id=event_id)
        if request.method == "POST":
            formulario= UpdateOutDoorForm(request.POST, request.FILES)
            if formulario.is_valid():
                info = formulario.cleaned_data #Para tenerlos en clase dict
                
                #Actualizar info de la serie escogida
                event.titulo_evento = info["titulo_evento"]
                event.deport = info["deport"]
                event.lugar_salida = info["lugar_salida"]
                event.description = info["description"]
                event.short_description = info["short_description"]
                event.image = event.image
                event.date = info["date"]
                event.save()
                actividades = OutDoor.objects.all()           
                return render(request,"gym/Aaire_libre.html",{'events':actividades})
                
        else: 

            formulario = UpdateOutDoorForm(initial={"titulo_evento":event.titulo_evento,
                                                "deport":event.deport,
                                                "lugar_salida":event.lugar_salida,
                                                "description":event.description,
                                                "short_description":event.short_description,
                                                "date":event.date}) #Para que venga con info precargada al actualizar
        return render(request, "gym/update_outdoor.html",{'form': formulario})
    

@login_required
def update_gym(request,event_id):
        event = Gym.objects.get(id=event_id)
        if request.method == "POST":
            formulario= UpdateGymForm(request.POST, request.FILES)
            if formulario.is_valid():
                info = formulario.cleaned_data #Para tenerlos en clase dict
                
                #Actualizar info de la serie escogida
                event.activity = info["activity"]
                
                event.description = info["description"]
                event.days = info["days"]
                event.hour = info["hour"]
                event.prof = info['prof']
                event.place = info["place"]
                event.image = event.image
                event.save()
                actividades = Gym.objects.all()           
                return render(request,"gym/Agimnasio.html",{'events':actividades})
        else: 

            formulario = UpdateGymForm(initial= {"activity":event.activity,
                                                "place":event.place,
                                                "description":event.description,
                                                "days":event.days,
                                                "hour":event.hour,
                                                "prof":event.prof} )
        return render(request, "gym/update_gym.html",{'form': formulario})
    
    
#############################################################
# Buscar y ver actividad al aire libre que se mostrará en la page #  ----> READ
#############################################################

# Vista que devolverá los eventos cargados en los modelos 
@login_required
def aire_libre(request):
    actividades = OutDoor.objects.all()
    return render(request, 'gym/Aaire_libre.html', {'events':actividades})

@login_required
def single_outdoor(request,event_id):
    actividad = OutDoor.objects.get(id=event_id)
    return render(request, f"actividades/ver_outdoor.html", {"actividad": actividad})

    


# Vista que devolverá las actividades del gym cargados en los modelos 
@login_required
def gym(request):
    actividades = Gym.objects.all()
    return render(request, 'gym/Agimnasio.html', {'events':actividades})

@login_required
def single_gym(request,event_id):
    actividad = Gym.objects.get(id=event_id)
    return render(request, f"actividades/ver_gym.html", {"actividad": actividad})



@login_required
def search_event(request):
    return render(request, "busquedas/eventos.html")

@login_required
def event_result(request):
    if request.method == "GET" and "busqueda_evento_nombre" in request.GET:
        busqueda = request.GET["busqueda_evento_nombre"]
        eventos = OutDoor.objects.filter(
            titulo_evento__icontains=busqueda,
            
        )
        return render(request, "busquedas/resultados_eventos.html", {"events": eventos})
    elif request.method == "GET" and "busqueda_evento_id" in request.GET:
        busqueda = request.GET["busqueda_evento_id"]
        eventos = OutDoor.objects.filter(
            id__icontains=busqueda,
            
        )
        return render(request, "busquedas/resultados_eventos.html", {"events": eventos})
        
    elif request.method == "GET" and "busqueda_evento_deport" in request.GET:
         busqueda = request.GET["busqueda_evento_deport"]
         eventos = OutDoor.objects.filter(
            deport__icontains=busqueda,
            
        )
         return render(request, "busquedas/resultados_eventos.html", {"events": eventos})  
    else:
        return render(request, "busquedas/eventos.html")


@login_required
def search_gym(request):
    return render(request, "busquedas/gimnasio.html")

@login_required
def gym_result(request):
    if request.method == "GET" and "busqueda_gym_nombre" in request.GET:
        busqueda = request.GET["busqueda_gym_nombre"]
        eventos = Gym.objects.filter(
            activity__icontains=busqueda,
            
        )
        return render(request, "busquedas/resultados_gimnasio.html", {"events": eventos})
    elif request.method == "GET" and "busqueda_gym_profesor" in request.GET:
        busqueda = request.GET["busqueda_gym_profesor"]
        eventos = Gym.objects.filter(
            prof__icontains=busqueda,
            
        )
        return render(request, "busquedas/resultados_gimnasio.html", {"events": eventos})
        
    elif request.method == "GET" and "busqueda_gym_id" in request.GET:
         busqueda = request.GET["busqueda_gym_id"]
         eventos = Gym.objects.filter(
            id__icontains=busqueda,
            
        )
         return render(request, "busquedas/resultados_gimnasio.html", {"events": eventos})  
    else:
        return render(request, "busquedas/gimnasio.html")


#############################################################
#                       DELETE                              #
#############################################################
def event_delete(request, id_event):
     evento = OutDoor.objects.get(id=id_event)     #----------> Borrar actividad OutDoor
     evento.delete() # Eliminando
     actividades = OutDoor.objects.all() 
     return render(request, 'gym/Aaire_libre.html', {'events':actividades})
 
def gym_delete(request, id_event):
     evento = Gym.objects.get(id=id_event)  #----------> Borrar actividad Gym
     evento.delete() # Eliminando 
     actividades = Gym.objects.all()
     return render(request, 'gym/Agimnasio.html', {'events':actividades})
     
   




    
        
         
 