from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.venue_list, name='venue_list'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login')
]
