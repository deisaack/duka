from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^drink/create/$', views.DrinkCreateView.as_view(), name='drink_create'),
    url(r'^drink/(?P<slug>[\w\-]+)/delete/$', views.DrinkDeleteView.as_view(), name='drink_delete'),
    url(r'^drink/(?P<slug>[\w\-]+)/$', views.DrinkDetailView.as_view(), name='drink_detail'),
    url(r'^drink/$', views.DrinkListView.as_view(), name='drink_list'),
    url(r'^drink/(?P<slug>[\w\-]+)/edit/$', views.DrinkUpdateView.as_view(), name='drink_update'),
    url(r'^create/$', views.FavoriteCreateView.as_view(), name='favorite_create'),
    url(r'^f=(?P<slug>[\w\-]+)/delete/$', views.FavoriteDeleteView.as_view(), name='favorite_delete'),
    url(r'^f=(?P<slug>[\w\-]+)/$', views.FavoriteDetailView.as_view(), name='favorite_detail'),
    url(r'^$', views.FavoriteListView.as_view(), name='favorite_list'),
    url(r'^f=(?P<slug>[\w\-]+)/edit/$', views.FavoriteUpdateView.as_view(), name='favorite_update'),
]
