from csv import reader

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
                'recipes/filling/data/ingredients.csv', 'r',
                encoding='UTF-8'
        ) as ingredients:
            for row in reader(ingredients):
                if len(row) == 2:
                    Ingredient.objects.get_or_create(
                        name=row[0], measurement_unit=row[1],
                    )
