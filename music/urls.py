from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #m/music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add'),
    #m/music/album/add/
    url(r'^(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
    #m/music/album/add/
    url(r'^(?P<pk>[0-9]+)/$',views.AlbumDelete.as_view(), name='album-delete'),

]
