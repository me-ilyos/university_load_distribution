from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.users.urls")),
    path("api/departments/", include("apps.departments.urls")),
    # path("api/professors/", include("apps.professors.urls")),
    # path("api/curriculum/", include("apps.curriculum.urls")),
    # path("api/assignments/", include("apps.distributions.urls")),
    # path("api/terms/", include("apps.academic_terms.urls")),
    # path("api/reports/", include("apps.reports.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
