from django import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Name",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Name"'}),
    )
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Email"'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Password"'}), 
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Reenter Password",'onfocus': 'this.placeholder = ""','onblur': 'this.placeholder = "Reenter Password"'}),
    )
    class Meta:
        model = User  # Replace with your User model
        fields = [
            "name",
            "username",
            "password",
        ]  # Fields to include in the form

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

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


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['message', 'name', 'email', 'subject']