from django import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}), 
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Reenter Password"}),
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
        widget=forms.EmailInput(attrs={"placeholder": "Email Address"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
