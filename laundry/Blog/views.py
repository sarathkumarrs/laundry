from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from main.forms import *
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
def blog(request):
    blogs=Blog.objects.all()
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    return render(request,'blog/blog.html', {'form': form,'services':services,'booking':booking,'blogs':blogs}) 

def blog_details(request,pk):
    blog=get_object_or_404(Blog, pk=pk)
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    return render(request,'blog/blog_details.html', {'form': form,'services':services,'booking':booking,'blog': blog})     

