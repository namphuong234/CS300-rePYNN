from django.contrib import admin
from .models import Category, Dish


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price']

