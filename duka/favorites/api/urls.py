from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^create/$', views.FavoriteCreateAPIView.as_view(), name='favorite_create'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', views.FavoriteDeleteAPIView.as_view(), name='favorite_delete'),
    url(r'^(?P<name>[\w\-]+)/$', views.FavoriteDetailAPIView.as_view(), name='favorite_detail'),
    url(r'^$', views.FavoriteListAPIView.as_view(), name='favorite_list'),
    url(r'^(?P<slug>[\w\-]+)/edit/$', views.FavoriteUpdateAPIView.as_view(), name='favorite_update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]