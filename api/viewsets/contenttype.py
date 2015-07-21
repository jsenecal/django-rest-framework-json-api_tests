from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import ContentTypeSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    permission_classes = (IsAuthenticated,)

