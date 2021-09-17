from django.db.models import fields
from rest_framework import serializers
from .models import Discontinued, Vehicle


class VehicleSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class DiscontinuedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discontinued
        fields = "__all__"
