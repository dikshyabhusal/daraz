from django.contrib import admin
from .models import Categories,Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description','image')
admin.site.register(Product)