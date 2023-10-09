from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment
from django.contrib.auth.models import User 

class AppointmentForm(forms.Form):
    visitor_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    visitor_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    visitor_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    checkin = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    visitor_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'



class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']