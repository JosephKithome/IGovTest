from django.db.models import fields
from rest_framework import serializers
from .models import Discontinued, Vehicle


class VehicleSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['Make_id','Make_name','Model_id','Model_name','id']

class DiscontinuedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discontinued
        fields = "__all__"
