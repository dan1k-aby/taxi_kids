from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

router_v1.register(r'voditeli', views.VoditeliViewSet, basename="voditeli")
router_v1.register(r'people', views.PeopleViewSet, basename="people")
router_v1.register(r'dispetchery', views.DispetcheryViewSet, basename="dispetchery")

urlpatterns = [
    path('', include(router_v1.urls)),
]