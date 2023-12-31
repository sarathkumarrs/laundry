from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    name = models.CharField(max_length=50,null=True)
   
    def __str__(self) :
        return self.username
     



class Booking(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('processing', 'Processing'),
        ('ready_for_pickup', 'Ready for Pickup'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')

    def __str__(self):
        return f"{self.name}'s Booking - {self.date} {self.time}"

