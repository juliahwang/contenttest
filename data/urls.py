from django.conf.urls import url
from . import views

app_name = "data"
urlpatterns = [
    url(r'^list/$', views.station_list, name='station_list'),
]