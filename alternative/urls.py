from django.contrib import admin
from django.urls import path,include
from rest_framework import views
from .views import vehicle_detail,vehicle_list,discontinued_list,discontinued_detail

urlpatterns = [
    path('' , vehicle_list, name="vehicle"),
    path('<int:pk>/' ,vehicle_detail, name="vehicle_detail"),

    path("discontinued/", discontinued_list, name="discontinued"),
    path("discontinued/<int:pk>/",discontinued_detail, name="discontinued_detail")
    # path("discontinued/<str:year>/")

]