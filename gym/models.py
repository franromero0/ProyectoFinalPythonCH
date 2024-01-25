from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model): #Creo mi modelo para las imagenes
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Va a estar vinculada a un usuario en particular
    imagen = models.ImageField(upload_to="avatares", null=True,blank=True) #Propiedades por si puede estar vacia



class OutDoor(models.Model):  #Este modelo albergará los eventos futuros
    def __str__(self):
        return f"{self.titulo_evento} -- {self.date}"
    titulo_evento = models.CharField(max_length=100)
    deport = models.CharField(max_length= 100)
    lugar_salida = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=1100)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="portadasOutDoor",null=True,blank=True)
    date = models.DateField()
    


class Gym(models.Model):
    activity = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portadasGym",null=True,blank=True)
    description  = models.CharField(max_length=1000)
    days = models.CharField(max_length=200)
    hour = models.CharField(max_length=200)
    prof = models.CharField(max_length= 100)  #Pueden ser uno o más 
    place = models.CharField(max_length= 100)  #Indicará en que salón del gimnasio está la actividad
    # Estos modelos alberganarán las actividades que se realizan en el gym principal
    # Algunos pueden ser: titulo_actividad, precio, días, lugar(salon del gym), profesores, descripcion
  
  
  
  
  
  
    
    
"""class OldOutDoor(models.Model): #Este modelo esta destinado a guardar algunos eventos exitosos 
    deport = models.CharField(max_length= 100)
    lugar_salida = models.CharField(max_length=100,null=True,blank=True)
    lugar_evento = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=1100)
    image = models.ImageField(null=True,blank=True)
    date = models.DateField()"""
 

    
    