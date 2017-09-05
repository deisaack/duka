from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import FavoriteViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', FavoriteViewSet, base_name='favorite')
# urlpatterns = router.urls

urlpatterns = [
    url(r'^create/$', views.FavoriteCreateAPIView.as_view(), name='favorite_create'),
    url(r'^fav/(?P<slug>[\w\-]+)/delete/$', views.FavoriteDeleteAPIView.as_view(), name='favorite_delete'),
    url(r'^fav/(?P<slug>[\w\-]+)/$', views.FavoriteDetailAPIView.as_view(), name='favorite_detail'),
    url(r'^$', views.FavoriteListAPIView.as_view(), name='favorite_list'),
    url(r'^fav/(?P<slug>[\w\-]+)/edit/$', views.FavoriteUpdateAPIView.as_view(), name='favorite_update'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
