from django.urls import path
from . import views
from .views import register
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('appointment/', views.appointment, name='appointment'), 
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    
]
