from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput(attrs={"placeholder": "Name",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Name"'}),
    )
    username = forms.EmailField(max_length=100,
                                required=True,
                                widget=forms.EmailInput(attrs={"placeholder": "Email",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Email"'}),
    )
    password = forms.CharField(min_length=8, 
                               required=True,
                               widget=forms.PasswordInput(attrs={"placeholder": "Password",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Password"'}), 
    )
    confirm_password = forms.CharField(required=True,
                                       widget=forms.PasswordInput(attrs={"placeholder": "Reenter Password",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Reenter Password"'}),
    )
    class Meta:
        model = User  # Replace with your User model
        fields = [
            "name",
            "username",
            "password",
        ]  # Fields to include in the form

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return confirm_password
    
    
class LoginForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email Address",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Email Address"'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Password"'}),
    )


class BookingForm(forms.ModelForm):
    phone = forms.CharField(max_length=10, required=True)
    
    address = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Booking
        fields = ['service','phone', 'address', 'date', 'time', 'message']

    def clean_date(self):
        date = self.cleaned_data['date']

        # Check if the selected date is not today or in the past
        if date <= timezone.now().date():
            raise forms.ValidationError("Please select a future date.")

        return date    


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['message', 'name', 'email', 'subject']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']        