from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from quickstart.serializers import UserSerializer, GroupSerializer

# The UserViewSet class is similar to the User model, except that it uses the User model and has a different set of fields.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permisiions_classes = [permissions.IsAuthenticated]

# The GroupViewSet class is similar to the UserViewSet class, except that it uses the Group model and has a different set of fields.

class GroupViewSet(viewsets.ModelViewSet):
    quesryset = Group.objects.all()
    serializer_class = GroupSerializer
    permisiions_classes = [permissions.IsAuthenticated]
