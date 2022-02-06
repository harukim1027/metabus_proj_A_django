from django.urls import path, include
from rest_framework.routers import DefaultRouter
from streetanimal import views
from streetanimal.views import AnimalViewSet


app_name = 'streetanimal'

router = DefaultRouter()
router.register("animal", AnimalViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

