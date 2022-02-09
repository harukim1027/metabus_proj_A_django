from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path("accounts/", include("accounts.urls")),
    path('review/', include("adopt_review.urls")),
    path('adopt_assignment/', include("adopt_assignment.urls")),
    path('inquiry_board/', include("inquiry_board.urls")),
    path('notice/', include("notice.urls")),
    path('streetanimal/', include("streetanimal.urls")),
=======
    path('adopt_review/', include("adopt_review.urls")),
    path('notice/', include("notice.urls")),
    path('attached_images/', include("attached_images.urls")),
>>>>>>> 94d4ad8e72f627daeda2202c5ce5ce11584a09af
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

