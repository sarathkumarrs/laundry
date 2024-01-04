from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    reviews=Review.objects.all()
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    review_stars = range(1, 6)
    return render(request,'main/index.html', {'form': form,'services':services,'booking':booking,'reviews':reviews,'review_stars': review_stars})

def signin(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
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

    return render(request,'main/signin.html',{'login_form':login_form,'form': form,'services':services,'booking':booking})

def signup(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    if request.method == "POST":
        form1 = UserRegistrationForm(request.POST)
        if form1.is_valid():
            print("Form is valid. Saving...")
            user = form1.save(commit=False)
            user.set_password(form1.cleaned_data["password"])
            user.save()
            messages.success(request, "You have signed up successfully!")
            return redirect("main:signup")
        else:
            print("Form is not valid:", form1.errors)
            return render(request, "main/signup.html", {"form1": form1})
    form1 = UserRegistrationForm()
    return render(request, 'main/signup.html', {"form1": form1,'form': form,'services':services,'booking':booking})  


def about(request):
    reviews=Review.objects.all()
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    review_stars = range(1, 6)
    return render(request,'main/about.html', {'form': form,'services':services,'booking':booking,'reviews':reviews,'review_stars': review_stars}) 

def contact(request):

    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    if request.method == 'POST':
        form3 = ContactMessageForm(request.POST)
        if form3.is_valid():
            # Create a new ContactMessage object with form data
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            # Save the object to the database
            contact_message.save()
            # Redirect to a success page or do something else
            return redirect('main:index')  # Change 'success_page' to the actual URL or view name for success
    else:
        
        form3 = ContactMessageForm()

    return render(request,'main/contact.html', {'form': form,'services':services,'booking':booking,'form3':form3}) 

def elements(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    return render(request,'main/elements.html', {'form': form,'services':services,'booking':booking}) 

def appointment(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    if request.user.is_authenticated:
            # Filter bookings based on the currently logged-in user
            bookings = Booking.objects.filter(user=request.user).order_by('-created_at')

            return render(request, 'main/appointment.html', {'bookings': bookings,'form': form,'services':services,'booking':booking})
    else:
        # Handle the case when the user is not authenticated
        return render(request, 'main/appointment.html', {'form': form,'services':services,'booking':booking})  # Create a template for this case
    

def services(request):
    booking =Booking.objects.all()
    services = LaundryService.objects.all()
    form = BookingForm()
    return render(request,'main/services.html', {'form': form,'services':services,'booking':booking})     

def signout(request):
    logout(request)
    return redirect(reverse("main:index"))


def booking_form(request):
    services = LaundryService.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assuming the user is logged in
            booking.status = 'received'  # Set the default status
            booking.save()
            return redirect('main:appointment')
    else:
        form = BookingForm()
    
    return render(request, 'main/index.html', {'form': form,'services':services})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the same page after saving the review
            return redirect('main:index')  # Replace 'your_success_page' with the actual URL name
    else:
        form = ReviewForm()

    return render(request, 'main/index.html', {'form': form})    