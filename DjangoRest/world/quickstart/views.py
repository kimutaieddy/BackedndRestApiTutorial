from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import import permisiions, viewsets

from world.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permisiions_classes = [permisiions.IsAuthenticated]