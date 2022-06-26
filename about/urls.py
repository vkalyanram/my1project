from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('', views.validate, name='validate'),
   ]

