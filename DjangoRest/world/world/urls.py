from quickstart import views
from django.urls import path,include
from rest_framework import routers


routers = routers.DefaultRouter()   #create a router object
routers.register(r'users',views.UserViewSet)    #register the viewset with the router
routers.register(r'Groups', views.GroupViewSet)  #register the viewset with the router

urlpatterns = [
    path('',include(routers.urls)),  #include the router urls
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))  #include the rest_framework urls
]