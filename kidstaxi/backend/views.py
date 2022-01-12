from rest_framework import viewsets
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend

from .models import Voditeli, People, Dispetchery, Order
from .serializers import VoditeliSerializer, PeopleSerializer, DispetcherySerialzier, OrderSerializer


class VoditeliViewSet(viewsets.ModelViewSet):
    queryset = Voditeli.objects.all()
    serializer_class = VoditeliSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('Name_vod',)
    search_fields = ('Auto', 'Auto_number',) 

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('Name_man',)
    search_fields = ('Number',) 

class DispetcheryViewSet(viewsets.ModelViewSet):
    queryset = Dispetchery.objects.all()
    serializer_class = DispetcherySerialzier
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('Name',)
    search_fields = ('Number',) 


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('Name_people', 'Name_vodil',)
    search_fields = ('Order',) 
