from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import import permisiions, viewsets

from world.quickstart.serializers import UserSerializer, GroupSerializer


class