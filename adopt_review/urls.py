from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adopt_review.views import ReviewViewSet

app_name = "adopt_review"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    # path("articles.json", views.article_list),
]
