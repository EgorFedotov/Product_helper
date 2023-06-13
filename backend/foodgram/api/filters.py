import django_filters as filters
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter

from recipes.models import Recipes

User = get_user_model()


class IngredientFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        label='Ссылка')
    author = filters.ModelChoiceFilter(
        queryset=User.objects.all())

    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.NumberFilter(
        method='filter_is_in_shopping_cart'
    )

    class Meta:
        model = Recipes
        fields = ('tags', 'author',)

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            cart_recipes_ids = self.request.user.shopping_cart.values_list(
                'recipe__id', flat=True)
            return Recipes.objects.filter(id__in=cart_recipes_ids)
        return queryset

    def filter_is_favorited(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(favorite_list__user=self.request.user)
        return queryset
