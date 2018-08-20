from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.personel_list, name='personel_kayit'),
    url(r'^personel/(?P<pk>\d+)/$', views.personel_detail, name='personel_detail'),
    url(r'^personel/new/$', views.personel_new, name='personel_new'),
    url(r'^personel/delete/(?P<pk>\d+)/$',views.delete_personel,name='delete_personel'),
    url(r'^personel/edit/(?P<pk>\d+)/$', views.personel_edit, name='personel_edit'),
]