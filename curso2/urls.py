"""
URL configuration for curso2 project.

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
from  tasks import views ##Importamos las vistas de la otra app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = "home" ),
    path("home/", views.home, name = "home" ),
    path("home2/", views.home2, name = "home2" ),
    path("signup/", views.signup, name = "signup" ),
    path("login/", views.log, name = "login" ),
    path("tasks/", views.tasks, name = "tasks" ),
    path("tasks_completed/", views.tasks_completed, name = "tasks_completed" ),
    path("logout/", views.exit, name = "logout" ),
    path("tasks/create/", views.createtask, name = "createtask" ),
    path("tasks/<int:id>/", views.taskdetails, name = "task_details" ),
    path("tasks/<int:id>/complete", views.taskcomplete, name = "task_complete" ),
    path("tasks/<int:id>/delete", views.delete, name = "delete" ),
   
]
