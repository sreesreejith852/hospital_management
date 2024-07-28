from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task

class UserRegistrationForm(UserCreationForm):
    mobile = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'address', 'latitude', 'longitude', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'datetime', 'assigned_to']