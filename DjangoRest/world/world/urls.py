from quickstart import views
from quickstart import views
from django.urls import path, include
from rest_framework import routers

# Create a router object
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)    # Register the UserViewSet with the router
router.register(r'groups', views.GroupViewSet)  # Register the GroupViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))  # Include the rest_framework URLs
]
