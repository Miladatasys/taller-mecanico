from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AppointmentForm
from .forms import RegisterForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username =request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("¡Has entrado a tu cuenta!"))
            return redirect('home')
        else: 
            messages.succes(request, ("Hubo un error, por favor intenta nuevamente"))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("¡Has cerrado sesión, gracias por visitar! "))
    return redirect('home')

    
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})