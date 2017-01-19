from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.venue_list, name='venue_list')
    url(r'^login.html$', views.login, name='login')
]
