from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

router_v1.register(r'voditeli', views.VoditeliViewSet, basename='posts')

urlpatterns = [
    path('', include(router_v1.urls)),
]