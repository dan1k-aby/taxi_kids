from rest_framework import viewsets 

from .models import Voditeli, People, Dispetchery
from .serializers import VoditeliSerializer, PeopleSerializer, DispetcherySerialzier


class VoditeliViewSet(viewsets.ModelViewSet):
    queryset = Voditeli.objects.all()
    serializer_class = VoditeliSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class DispetcheryViewSet(viewsets.ModelViewSet):
    queryset = Dispetchery.objects.all()
    serializer_class = DispetcherySerialzier