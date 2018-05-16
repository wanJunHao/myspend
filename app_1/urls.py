from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'index/', views.index),
    re_path(r'^spend/(?P<method>\w+)/$', views.spend),
]
