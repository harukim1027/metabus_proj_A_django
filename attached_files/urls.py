from django.urls import include, path
from rest_framework.routers import DefaultRouter

from attached_files.views import AttachedFileViewSet

app_name = "attached_file"

router = DefaultRouter()
router.register("attached_file", AttachedFileViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
