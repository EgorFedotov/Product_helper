from django.contrib import admin

from .models import Ingredient, Recipes, Tag, RecipeIngredient


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1


@admin.register(Recipes)
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
    inlines = [IngredientInline]
    empty_value_display = ('-пусто-')

    @admin.display(description='Количество добавлений в избранное')
    def number_of_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('measurement_unit',)
    empty_value_display = ('-пусто-')


admin.site.register(Tag)
