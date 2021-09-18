from django.contrib import admin
from django.urls import path
from .views import DiscontinuedView, VehicleViewNew,discontinued_vehicles,single_discontinued_vehicle,Vehicle_Detail


app__name ="iGov"

urlpatterns = [
    path('',VehicleViewNew.as_view()),

    #vehicle_detail
    path('<int:pk>/',Vehicle_Detail.as_view()),

    #list of discontinued vehicles
    path('discontinued/',DiscontinuedView.as_view()),

    #Returns a list of vehicles searched by year
    path('discontinued/<str:year>/',discontinued_vehicles,name="discontinued"),

    #Returns detail of a discontinued vehicle
    path('discontinued_vehicle_detail/<int:pk>/',single_discontinued_vehicle,name="discontinued_vehicle_detail")
]
