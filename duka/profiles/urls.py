from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^data-collectors/$', views.CollectorListView.as_view(), name='collector_list'),
    url(r'^me/$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit/$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^p/(?P<slug>[\w\-]+)$', views.CollectorDetailView.as_view(), name='collector_detail'),
    url(r'^p/(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
            name='show'),
]
