"""
URL configuration for aquatech_web project.

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
from django.urls import path, include
from user import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("signupaccounts/", views.signupaccounts, name="signupaccounts"),
    path("home/", views.home),
    path("servicios/", views.servicios),
    path("tienda/", views.tienda),
    path("carrito/", views.carrito),
    path("logout/", views.logoutaccount, name="logoutaccount"),
    path("login/", views.loginaccount, name="loginaccount"),
    path("usuario/", views.usuario, name="usuario"),
    path("chat/", views.chat, name="chat"),
]
