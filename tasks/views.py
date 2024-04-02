from django.shortcuts import render, redirect, get_object_or_404 #Renderiza plantillas, redirecciona y busa un objeto o devuelve 404
from django.http import HttpResponse #Respuestas http
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Crea formularios
from django.contrib.auth.models import User #Importa el modelo de usuario
from django.contrib.auth import login, logout, authenticate   #Autenticacion y logout
from django.db import  IntegrityError     #Para manejar errores en la base de datos
from .form import TaskForm     #Importa el formulario para tareas
from .models import Task     #Importa el Modelo de Tarea
from django.utils import timezone     #Fechas y horarios
from django.contrib.auth.decorators import  login_required    #Decorador que verifica si esta autentificado o no

def home(request):
 ##return HttpResponse("Hello world") Respuesta http
 return render(request, "home.html")
 

def signup(request):
    if (request.method == "GET"): ##Envia el formulario al visitar la pagina, esto significa que el usuario hace un GET De la template
     return render(request, "signup.html", {"form": UserCreationForm}) #render devuelve una respuesta http con un template
    else:
        ##Register user
        if ( request.POST["password1"] == request.POST[ "password2"] ):
         try:
          user =  User.objects.create_user(username = request.POST["username"], password = request.POST["password1"])
          user.save()
          return redirect("login")
         except IntegrityError:
          # return HttpResponse("Error creating the account") --> Version vieja
          return render(request, "signup.html", {"form": UserCreationForm, "error" : "Error User already exist."})
        else:
            # return HttpResponse("Password do no match") --> Version vieja
            return render(request, "signup.html", {"form": UserCreationForm, "error" : "Error, password dont match"})
        
def log(request): ##Login
    if  (request.method=='GET'):
     return render(request, "login.html", {"form": AuthenticationForm})   
    else:
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if(user is None):
            return render(request, "login.html", {"form": AuthenticationForm, "error"  : "Username or password incorrect" })
        else:
           login(request, user)
           return  redirect("tasks")
       
@login_required     
def createtask(request): ##Crea una tarea
    if (request.method == "GET"):
     return render(request, "createtask.html", {"form": TaskForm})
    else: 
     try: 
         form = TaskForm(request.POST)
         new_task = form.save(commit = False)
         new_task.user = request.user
         new_task.save()
         return redirect("tasks")
     except:
         return render(request, "createtask.html", {"form": TaskForm, "error":"Error creating task"})
           
            
    
@login_required            
def tasks(request):
    task = Task.objects.filter(user= request.user, datecompleted__isnull = True ) ##Filtra que la propiedad user de la base de datos sea igual al user de donde se hace la request y solo busca las tareas que la fecha de completado sea nula osea, pendientes por hacer
    return render(request, "tasks.html", {"task": task})





@login_required     
def taskdetails(request, id): #Muestra los detalles de la tarea
  if (request.method == "GET"):
     task = get_object_or_404(Task, pk = id, user = request.user)
     form = TaskForm(instance=task)
     return render(request, "details.html", {"task": task, "form": form})
  else:
     try:  
      task = get_object_or_404(Task, pk = id, user = request.user)
      form = TaskForm(request.POST, instance=task)
      form.save()
      return redirect("tasks")
     except ValueError:
      return render(request, "details.html", {"task": task, "form": form, "error": "Error updating the task"})
  
  
  
@login_required             
def taskcomplete(request, id): ##Marcar tarea como echa
    task = get_object_or_404(Task, pk = id, user = request.user )
    if  (request.method == "POST"):
      task.datecompleted = timezone.now()
      task.save()
      return redirect("tasks")
  
@login_required       
def tasks_completed(request):
    task = Task.objects.filter(user= request.user, datecompleted__isnull = False).order_by("-datecompleted") ##Filtra que la propiedad user de la base de datos sea igual al user de donde se hace la request y solo busca las tareas que la fecha de completado sea verdadera osea, echas y la ordena de menor a mayor
    return render(request, "tasks_completed.html", {"task": task})

  
@login_required     
def delete(request, id): ##Eliminar tarea
    task = get_object_or_404(Task, pk = id, user = request.user )
    if  (request.method == "POST"):
      task.delete()
      return redirect("tasks")
  
 
 
@login_required      
def home2(request):
    return render (request, "home2.html")



@login_required     
def exit(request):
    logout(request)
    return redirect("home")    
    