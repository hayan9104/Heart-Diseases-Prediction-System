from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product



from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','speciality','email_id')
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)

# admin.py
from django.contrib import admin
from .models import Doctordb

class DoctordbAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','password')  # Display both username and email

admin.site.register(Doctordb, DoctordbAdmin)