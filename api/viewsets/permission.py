from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    permission_classes = (IsAuthenticated,)
