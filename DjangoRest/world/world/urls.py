"""
URL configuration for world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from quickstart import views

routers = routers.DefaultRouter()   #create a router object
routers.register(r'users',views.UserViewSet)    #register the viewset with the router
routers.register(r'groups',views.GroupViewSet)  #register the viewset with the router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls)),  #include the router urls
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))  #include the rest_framework urls
]