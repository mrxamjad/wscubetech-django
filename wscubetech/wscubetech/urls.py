"""
URL configuration for wscubetech project.

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
from wscubetech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('user-name/<str:name>/', views.userDetailsByName),
    path('user-id/<int:id>/', views.userDetailsById),
    path('user-slug/<slug:slug>/', views.userDetailsBySlug),
    path('user/<data>/', views.userDetailsByData),
    
    path("", views.home),  # IT will render the index.html file from the templates directory if only simple url getting hitted.
    
    path("home-dynamic/", views.homeDynamic)  # IT will render the index_dynamic.html file from the templates directory with dynamic data if only simple url getting hitted.
         
    
]
