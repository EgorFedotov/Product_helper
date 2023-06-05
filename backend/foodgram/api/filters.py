from rest_framework.filters import SearchFilter
import django_filters as filters
from recipes.models import Recipe
from users.models import User


class IngredientFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        label='Ссылка')
    author = filters.ModelChoiceFilter(
        queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)
