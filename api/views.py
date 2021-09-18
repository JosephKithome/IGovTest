from django.shortcuts import render

from .serializers import DiscontinuedSerializer, VehicleSerialiezer
from .models import Vehicle,Discontinued
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from django.contrib.auth.models import User

# Create your views here.

# class VehicleView(generics.ListAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class =VehicleSerialiezer

class VehicleViewNew(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerialiezer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

class Vehicle_Detail(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class =VehicleSerialiezer

class DiscontinuedView(generics.ListAPIView):
    queryset = Discontinued.objects.all()
    serializer_class =DiscontinuedSerializer    

@csrf_exempt
def discontinued_vehicles(request,year):
  
    if request.method == 'GET':
        discontinued_vehicle = Discontinued.objects.filter(year=year)
        serializer = DiscontinuedSerializer(discontinued_vehicle, many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Discontinued(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def single_discontinued_vehicle(request, pk):
    try:
        vehicle = Discontinued.objects.get(pk=pk)
    except Discontinued.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = DiscontinuedSerializer(vehicle)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DiscontinuedSerializer(vehicle, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        vehicle.delete()
        return HttpResponse(status=204)



