from django.conf.urls import url

from . import views

app_name = 'Moscow_weather'

urlpatterns = [
    url(r'^$', views.get_weather, name='get_weather'),
]