from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adopt.views import ReviewViewSet

app_name = "adopt"

router = DefaultRouter()
router.register("posts", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    # path("articles.json", views.article_list),
]
