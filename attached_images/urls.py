from django.urls import include, path
from rest_framework.routers import DefaultRouter
from attached_images.views import AttachedImageViewSet

app_name = "attached_images"

router = DefaultRouter()
router.register("images", AttachedImageViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
