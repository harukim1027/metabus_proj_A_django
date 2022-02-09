from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from notice.views import NoticeViewSet


app_name = 'notice'

router = DefaultRouter()
router.register("notices", NoticeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

=======

from notice.views import NoticeViewSet

app_name = "notice"

router = DefaultRouter()
router.register("notice", NoticeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
>>>>>>> 94d4ad8e72f627daeda2202c5ce5ce11584a09af
