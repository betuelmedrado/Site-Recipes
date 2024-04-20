from django.contrib import admin
from .models import Category, Recipes

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    # shows the contents of the fields in the administrative area
    list_display = ['id','title','create_at','is_plubeshed']
    # To show selection fields
    list_editable = 'is_plubeshed',
    # To show links
    list_display_links = 'title', 'create_at'
    # To show fields search
    search_fields = 'id', 'title','description','slug','preparation_steps'
    # To show fields filter
    list_filter = 'category','author','is_plubeshed'
    # Amounth of pages
    list_per_page = 10
    # ordering for id
    ordering = '-id',
    # fill in automatic fields
    prepopulated_fields = {
        "slug":('title',)
        }