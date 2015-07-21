from django.contrib.auth.models import User
from rest_framework import serializers
from api.serializers import GroupSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # extra_kwargs = {'password': {'write_only': True}}
        exclude = ['password']
        depth = 1

        user_permissions = serializers.HyperlinkedIdentityField(
            read_only=True,
            view_name='permission-detail'
        )

        groups = GroupSerializer()