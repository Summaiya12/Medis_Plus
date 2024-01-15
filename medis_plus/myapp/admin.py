from django.contrib import admin
from .models import Category, DoctorDetail, Appointment, Contacts


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(DoctorDetail)
class AdminDoctorDetail(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'days', 'time']


@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'phone', 'doctor']


@admin.register(Contacts)
class AdminAppointment(admin.ModelAdmin):
    list_display = ['name', 'email']
