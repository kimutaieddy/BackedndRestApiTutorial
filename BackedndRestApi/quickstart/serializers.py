from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
# Output: {'url': 'http://example.com/users/1/', 'username': 'john_doe', 'email': 'john@example.com', 'groups': ['http://example.com/groups/1/']}


# Output: {'url': 'http://example.com/groups/1/', 'name': 'Admins'}

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']