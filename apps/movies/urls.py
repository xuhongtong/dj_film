from django.conf.urls import url

from apps.movies import views

urlpatterns = [
    url('(?P<id>\d+)/',views.detail),
]