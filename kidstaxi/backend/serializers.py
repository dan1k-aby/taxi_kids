from rest_framework import fields, serializers

from .models import Voditeli


class VoditeliSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Voditeli