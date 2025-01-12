# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

#Car Maker model  (aka brand)
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# - Name
# - Description
# - Any other fields you would like to include in car make model
    def __str__(self):
       return self.name


# <HINT> Create a Car Model model 
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    mileage = models.IntegerField()

    year = models.IntegerField(
        default=2023, 
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2025)
    ])

    CAR_TYPES = [
        ("COUPE" , "Coupe"),
        ("CONVERTIBLE" , "Convertible"),
        ("HATCHBACK" , "Hatchback"),
        ("MINI-VAN", "Minivan"),
        ("PICKUP", "Pickup"),
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')

    def __str__(self):
       return self.name