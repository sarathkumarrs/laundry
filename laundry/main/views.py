from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def signin(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    "main:index"
                )  # Redirect to the 'index' page on successful login
            else:
                # Authentication failed, display an error message to the user
                login_form.add_error(
                    None, "Invalid credentials"
                )  # Add non-field error to the form
    else:
        login_form = LoginForm()

    return render(request,'main/signin.html',{'login_form':login_form})

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving...")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "You have signed up successfully!")
            return redirect("main:signin")
        else:
            print("Form is not valid:", form.errors)
            return render(request, "main/signup.html", {"form": form})
    form = UserRegistrationForm()
    return render(request, 'main/signup.html', {"form": form})  


def about(request):
    return render(request,'main/about.html') 

def contact(request):
    return render(request,'main/contact.html') 

def elements(request):
    return render(request,'main/elements.html') 

def appointment(request):
    return render(request,'main/appointment.html') 

def blog(request):
    return render(request,'main/blog.html') 

def blog_details(request):
    return render(request,'main/blog_details.html')     


def services(request):
    return render(request,'main/services.html')     

def signout(request):
    logout(request)
    return redirect(reverse("main:index"))