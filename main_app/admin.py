from django.contrib import admin
from .models import *
# Register your models here.

class SneakerCardAdmin(admin.ModelAdmin):
    list_display = ['category' ,'title', 'description', 'price']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Brand, BrandAdmin)
admin.site.register(SneakerCard, SneakerCardAdmin)
