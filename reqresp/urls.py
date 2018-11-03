from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    # 命名的写法
    # url(r'^weather/(?P<MingMing>正则)/(?P<MingMing2>正则)/$',views.weather)
    url(r'^response/$', views.demo_response)
]