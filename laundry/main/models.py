from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    name = models.CharField(max_length=50,null=True)
   
    def __str__(self) :
        return self.username
    
    
     
class LaundryService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(LaundryService, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)   
    status = models.CharField(max_length=20, choices=[
        ('received', 'Received'),
        ('processing', 'Processing'),
        ('ready_for_pickup', 'Ready for Pickup'),
        ('picked_up', 'Picked Up'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='received')  
    created_at = models.DateTimeField(auto_now_add=True,null=True)  # Add this line

    # Assuming 'user' is a ForeignKey field in your Booking model
    def __str__(self):
        username = self.user.username if self.user else "Unknown User"
        return f"{username}'s Booking - {self.date} {self.time}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    



class Review(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    
