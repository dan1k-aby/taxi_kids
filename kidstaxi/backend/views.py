from rest_framework import viewsets 

from .models import Voditeli
from .serializers import VoditeliSerializer


class VoditeliViewSet(viewsets.ModelViewSet):
    queryset = Voditeli.objects.all()
    serializer_class = VoditeliSerializer
