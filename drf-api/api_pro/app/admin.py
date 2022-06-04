import imp
from django.contrib import admin
from .models import ObjectModel

# Register your models here.
@admin.register(ObjectModel)
class AdminThing(admin.ModelAdmin):

    list_display=["name","timestamp","updated","description"]
    
