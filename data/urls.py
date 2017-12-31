from django.conf.urls import url
from . import views

app_name = "data"
urlpatterns = [
    # 정보 리스트 한번에 보는 페이지 - 10개로 페이지네이션 처리
    url(r'^list/$', views.station_list, name='station_list'),

    # 역별 자세한 수치정보를 볼 수 있는 페이지
    # url(r'^(?P<station_id>\d+)/$', views.station_detail, name="station_detail"),
    url(r'^(?P<station_id>\d+)/$', views.test_detail, name="station_detail"),
]