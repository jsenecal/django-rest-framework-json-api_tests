from django.conf.urls import include, url, patterns
from rest_framework.routers import DefaultRouter
from api.viewsets import UserViewSet, GroupViewSet, PermissionViewSet, ContentTypeViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'contenttypes', ContentTypeViewSet)

urlpatterns = router.urls

urlpatterns += patterns(
    '',
    url(r'^drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
)