from inspect import trace
from django.shortcuts import render
from api.serializers import VehicleSerialiezer,DiscontinuedSerializer
from api.models import Discontinued,Vehicle

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
@api_view(['GET','POST'])
def vehicle_list(request):
    """
    List all Vehicles, or create a new Vehicle
    """
    if request.method == 'GET':
        vehicle = Vehicle.objects.all()
        serializer = VehicleSerialiezer(vehicle, many=True)
        return Response(serializer.data)
  
    elif request.method == 'POST':
        serializer = VehicleSerialiezer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET','PUT','PATCH','DELETE'])
def vehicle_detail(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return Response({"error":"No results found"},status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = VehicleSerialiezer(vehicle)
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        serializer = VehicleSerialiezer(vehicle, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = VehicleSerialiezer(vehicle,data=request.data,partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","POST","PUT","DELETE"])   
def discontinued_list(request):
    if request.method =="GET":
        discontinued = Discontinued.objects.all()
        serializer = DiscontinuedSerializer(discontinued,many=True)
        return Response(serializer.data)

    # if request.method =="POST":
    #     serializer = DiscontinuedSerializer(data=request.data)
    #     if serializer.is_valid():
    #         try:
    #             serializer.save()
    #             return Response(serializer.data,status=status.HTTP_201_CREATED)
    #         except:
    #             return Response(serializer.data,{"success":"Created successfully"},status=status.HTTP_201_CREATED)  

@api_view(['GET','PUT','PATCH','DELETE'])
def discontinued_detail(request,pk):

    try:
        discontinued = Discontinued.objects.get(pk=pk)
    except Discontinued.DoesNotExist:
        return Response({"error":"Object does not exist!"})  

    if request.method == "GET":
        serializer = DiscontinuedSerializer(discontinued)
        return Response(serializer.data,status=status.HTTP_200_OK)  

    elif request.method == "PUT":
        serializer = DiscontinuedSerializer(discontinued,data=request.data)    

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == "PATCH":
        serializer = DiscontinuedSerializer(discontinued,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  

    elif request.method == "DELETE":
        discontinued.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            


