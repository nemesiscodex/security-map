from django.conf.urls import include, url
from apps.map import views

urlpatterns = [
    url(r'^', views.index)
]
