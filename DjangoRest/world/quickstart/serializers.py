from django.contrib.auth.models import Group,User
from rest_framework import serializers


# The UserSerializer class is similar to the User model, except that it uses the User model and has a different set of fields.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# The GroupSerializer class is similar to the UserSerializer class, except that it uses the Group model and has a different set of fields.
class GroupSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Group
        fields = ('url', 'name')