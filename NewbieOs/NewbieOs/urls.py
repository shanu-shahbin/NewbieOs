from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job.urls')),
    path('', include('company.urls')),
    path('', include('customers.urls')),
    # path('', include('guidance.urls')),
    # path('', include('homeapp.urls')),

]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)