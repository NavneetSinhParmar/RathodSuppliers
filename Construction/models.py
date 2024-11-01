# models.py
from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=255, blank=True, null=True)  # Optional email field

    def __str__(self):
        return f"{self.name} - {self.phone}"

class VehicleInfo(models.Model):
    WHEEL_CHOICES = [
        ('10 Wheel', '10 Wheel'),
        ('12 Wheel', '12 Wheel'),
        ('Others', 'Others'),
    ]

    user = models.ForeignKey(Register, related_name='vehicles', on_delete=models.CASCADE)
    wheel_type = models.CharField(max_length=20, choices=WHEEL_CHOICES)
    vehicle_no = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.wheel_type} - {self.vehicle_no} for {self.user.name}"
