from django.contrib import admin

from .models import Recipe, Ingredient, Tag


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'author',
    )
    list_filter = (
        'author',
        'name',
        'tags',
    )


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'measurement_unit',
    )
    search_fields = ('name')
    list_filter = ('measurement_unit')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
