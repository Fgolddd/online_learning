from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include('apps.users.urls')),
    path('api/posts/', include('apps.post.urls')),
    path('api/comments/', include('apps.comment.urls')),
    path('api/courses/', include('apps.course.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
