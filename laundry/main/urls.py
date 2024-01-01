from django.contrib import admin
from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    # path('appointment/<int:pk>/',views.appointment,name='appointment'),  
    path('appointment/', views.appointment, name='appointment'),
  
    path('blog/',views.blog,name='blog'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('services/',views.services,name='services'),
    path('signout/',views.signout, name='signout'),
    path('booking/', views.booking_form, name='booking_form'),
]
