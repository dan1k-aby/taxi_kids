from rest_framework import serializers

from .models import Voditeli, People, Dispetchery


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