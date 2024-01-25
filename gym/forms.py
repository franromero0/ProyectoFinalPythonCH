from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import *
from .models import *

############## Formularios de autenticación ##############

class RegistrarUsuario(UserCreationForm):  #Esto lo podemos usar en las viewa
    first_name = forms.CharField(max_length=100,
                                 label="", 
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Nombre','style': 'font-size: 12px; color: white;'
                                                               }))
    username = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'style': 'font-size: 12px; color: white;'
                                                                        }))
    email = forms.EmailField(
                            required=True,
                             label="",
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail','style': 'font-size: 12px; color: white;'
                                                           }))
    
    password1 = forms.CharField(
                                max_length=100,
                                label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style': 'font-size: 12px; color: white;'}),
                                required=True,
                                help_text="La contraseña debe tener más de 6 carácteres, números y letras",
                                )

    password2 = forms.CharField(max_length=100, 
                                label="", 
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña','style': 'font-size: 12px; color: white;'}), 
                                required=True
                                )
    
    
    class Meta: #Seria una manera de personalizar el formulario
        model = User 
        fields = ["first_name","username", "email", "password1", "password2"] #Son campos por defecto que trae django 
     
    ########################################################################################################### 
        
class AuthenticationFormulario(AuthenticationForm):
    username = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'style': 'font-size: 12px;color: white;'
                                                                        }))
    password = forms.CharField(
                                max_length=100,
                                label="",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style': 'font-size: 12px; color: white;'}),
                                required=True,
                                help_text="La contraseña debe tener más de 6 carácteres, números y letras",
                                )
    
    class Meta: #Seria una manera de personalizar el formulario
        model = User 
        fields = ["username","password1"] #Son campos por defecto que trae django 
      
###########################################################################################################       
      

class EditarUsuario(UserCreationForm): 
                                        first_name = forms.CharField(required=False,
                                                                max_length=100,label="Nombre",
                                                                widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre', 'style': 'font-size: 12px; color: white;'
                                                                                                        }))
                                        
                                        email = forms.EmailField(required=False,label="Correo electronico",widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su email', 'style': 'font-size: 12px; color: white;'}))
                                        password1 = forms.CharField(required=False,max_length=100, label="Ingrese la contraseña", widget=forms.PasswordInput(attrs={'placeholder': '********', 'style':'color: white;}'}))
                                        password2 = forms.CharField(required=False,max_length=100, label="Confirme la contraseña", widget=forms.PasswordInput(attrs={'placeholder': '********', 'style':'color: white;}'}))
                                        
                                        class Meta:
                                            model = User 
                                            fields = [ "first_name", "email", "password1", "password2"] 
                                    
                                    

                                  
############## Avatar form ##############

class AvatarForm(forms.ModelForm): #Creo mi modelo para las imagenes

    class Meta:
        model = Avatar
        fields = ['imagen']

   
      
############## OutDoor Model Forms ##############        

class OutDoorForm(forms.ModelForm):
    
    titulo_evento = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ej. Arco de piedra - Mina clavero', 'style': 'font-size: 12px; color: white;'
                                                                        }),
                            help_text="Ingrese el titulo y la imagen de la publicacion del evento: ")
    deport = forms.CharField(max_length=100,
                                 label="", 
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Deporte','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Ingresa si es trekking/senderismo/montañismo:")
    
    lugar_salida = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Punto de partida', 'style': 'font-size: 12px; color: white;'
                                                                        }),
                            help_text="Donde iniciará el evento:")
    short_description = forms.CharField(
                            max_length=200,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Descripción corta que se previsualizará', 'style': 'font-size: 12px; color: white;'
                                                                        }))
    description = forms.CharField(
                            max_length=1100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Descripción del evento detallada', 'style': 'font-size: 12px; color: white;'
                                                                        }))
    
    date = forms.DateField(help_text="Fecha del evento",widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
                model = OutDoor
                fields = ['titulo_evento','image', 'deport','lugar_salida','short_description','description','date']

########################################################################################################### 

class UpdateOutDoorForm(forms.ModelForm):
    
    titulo_evento = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Ej. Arco de piedra - Mina clavero', 'style': 'font-size: 12px; color: white;'
                                                                        }),
                            help_text="Ingrese el titulo  de la publicacion del evento: ")
    deport = forms.CharField(max_length=100,
                                 label="", 
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Deporte','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Ingresa si es trekking/senderismo/montañismo:")
    
    lugar_salida = forms.CharField(
                            max_length=100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Punto de partida', 'style': 'font-size: 12px; color: white;'
                                                                        }),
                            help_text="Donde iniciará el evento:")
    short_description = forms.CharField(
                            max_length=200,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Descripción corta que se previsualizará', 'style': 'font-size: 12px; color: white;'
                                                                        }))
    description = forms.CharField(
                            max_length=1100,label="",
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Descripción del evento detallada', 'style': 'font-size: 12px; color: white;'
                                                                        }))
    
    date = forms.DateField(help_text="Fecha del evento",widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(required=False,widget=forms.HiddenInput())
    class Meta:
                model = OutDoor
                fields = ['titulo_evento','deport','lugar_salida','short_description','description','image','date']



############## Gym Model Forms ##############       
 
class GymForm(forms.ModelForm):
    activity = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Título. Ej. Kick Boxing or Musculación','style': 'font-size: 12px; color: white;'
                                                               }),
                               
                                help_text="¿Que actividad nueva quiere registrar? ¡Agregale una imagen!")
    description  = forms.CharField(max_length=1000,
                                   required=False, 
                                   widget=forms.TextInput(attrs={'placeholder': 'Se previsualizará en la portada','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Descripcion de la actividad/deporte")
    days = forms.CharField(max_length=200, 
                           required=True, 
                           widget=forms.TextInput(attrs={'placeholder': 'formato: Lunes, Miercoles y Viernes ','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Días que se brindará")
    hour = forms.CharField(max_length=200,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder':'Formato: de 6 p.m a 9 p.m o 17hs a 20hs', 'style': 'font-size: 12px; color: white;'}))
    prof = forms.CharField(max_length= 100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre del profesor(solamente nombre)','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Ingrese el nombre del profesor de la clase")  
    place = forms.CharField(max_length= 100,
                            required=False,
                             
                            widget=forms.TextInput(attrs={'placeholder':'Ej. Salón Cardio','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="En qué parte del gimnasio se brindará")
    
    class Meta: 
        model = Gym
        fields = ['activity','image','description','days','prof','place']


########################################################################################################### 


class UpdateGymForm(forms.ModelForm):
    activity = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Título. Ej. Kick Boxing or Musculación','style': 'font-size: 12px; color: white;'
                                                               }),
                               
                                help_text="¿Que actividad nueva quiere registrar?")
    description  = forms.CharField(max_length=1000,
                                   required=False, 
                                   widget=forms.TextInput(attrs={'placeholder': 'Se previsualizará en la portada','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Descripcion de la actividad/deporte")
    days = forms.CharField(max_length=200, 
                           required=True, 
                           widget=forms.TextInput(attrs={'placeholder': 'formato: Lunes, Miercoles y Viernes ','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Días que se brindará")
    hour = forms.CharField(max_length=200,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder':'Formato: de 6 p.m a 9 p.m o 17hs a 20hs', 'style': 'font-size: 12px; color: white;'}),
                           help_text="Horarios")
    prof = forms.CharField(max_length= 100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre del profesor(solamente nombre)','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="Ingrese el nombre del profesor de la clase")  
    place = forms.CharField(max_length= 100,
                            required=False,
                             
                            widget=forms.TextInput(attrs={'placeholder':'Ej. Salón Cardio','style': 'font-size: 12px; color: white;'
                                                               }),
                                 help_text="En qué parte del gimnasio se brindará")
    image = forms.ImageField(required=False,widget=forms.HiddenInput(),label=None)
    
    class Meta: 
        model = Gym
        fields = ['activity','image','description','days','prof','place']
        
        


