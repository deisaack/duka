from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'', include('duka.accounts.urls', namespace='accounts')),
    url(r'users/', include('duka.profiles.urls', namespace='profiles')),
    url(r'the-favorites/', include('duka.favorites.urls', namespace='favorites')),
    url(r'api/', include('duka.favorites.api.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^aws/', include('duka.files.urls', namespace='files')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

