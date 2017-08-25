from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'', include('duka.accounts.urls', namespace='accounts')),
    url(r'users/', include('duka.profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
]
