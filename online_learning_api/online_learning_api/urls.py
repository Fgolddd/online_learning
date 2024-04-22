from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/", include('apps.user.urls')),
    path('api/post/', include('apps.post.urls')),
    path('api/comment/', include('apps.comment.urls')),
    path('api/course/', include('apps.course.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
