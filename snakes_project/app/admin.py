from django.contrib import admin
from app.models import Snakes
# Register your models here.

@admin.register(Snakes)
class Admin(admin.ModelAdmin):
    list_display = ['title']