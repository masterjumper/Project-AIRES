from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^web/', include('web.urls', namespace='web')),
    url(r'^', include('web.urls')),
    url(
        r'^django_popup_view_field/',
        include('django_popup_view_field.urls', namespace="django_popup_view_field")
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
