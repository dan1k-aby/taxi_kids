from rest_framework import viewsets 

from .models import Voditeli, People, Dispetchery, Order
from .serializers import VoditeliSerializer, PeopleSerializer, DispetcherySerialzier, OrderSerializer


class VoditeliViewSet(viewsets.ModelViewSet):
    queryset = Voditeli.objects.all()
    serializer_class = VoditeliSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class DispetcheryViewSet(viewsets.ModelViewSet):
    queryset = Dispetchery.objects.all()
    serializer_class = DispetcherySerialzier


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
