from django.contrib import admin
from .models import Category, Recipes

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


@admin.register(Recipes)
class Recipe(admin.ModelAdmin):
    ...