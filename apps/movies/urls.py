from django.conf.urls import url

from apps.movies import views

urlpatterns = [
    url('detail/?P<pk>\d+',views.detail),
]