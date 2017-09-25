from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
]
