from django.db import models

# Create your models here.

class Vehicle(models.Model):

    Make_id =models.CharField(max_length=20)
    Make_name = models.CharField(max_length=100)
    Model_id =models.CharField(max_length=20 )
    Model_name = models.CharField(max_length=100 )

    def __str__(self):
        return self.Model_name


    class Meta:
        verbose_name = "Vehicle"   
        verbose_name_plural = "Vehicles" 

    

class Discontinued(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    discontinued = models.BooleanField(default=False)
    year = models.CharField(max_length=20)    
    period = models.IntegerField()

    def __str__(self):
        return self.vehicle.Model_name  

    class Meta:
        verbose_name = "Discontinued"   
        verbose_name_plural = "Discontinued" 

