from django.contrib import admin
from .models import Category, Customer, Product, Appointment

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Appointment)