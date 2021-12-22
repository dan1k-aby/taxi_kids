from django.db import models
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Voditeli, People, Dispetchery, Order


class VoditeliSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Voditeli


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = People


class DispetcherySerialzier(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Dispetchery

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Order