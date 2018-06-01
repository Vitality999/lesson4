from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_names, name='names'),
    url(r'^$', views.start_page, name='start'),
]
