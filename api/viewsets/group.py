from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers.group import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (IsAuthenticated,)

