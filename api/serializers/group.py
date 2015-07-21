from django.contrib.auth.models import Group, User
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group

    user_set = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )
