from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attached_images.views import ImagesViewSet

app_name = "attached_image"

router = DefaultRouter()
router.register("images", ImagesViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
