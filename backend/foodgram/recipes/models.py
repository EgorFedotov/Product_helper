from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from recipes.validators import ColorValidator
from users.validators import NameValidator

User = get_user_model()


class Tag(models.Model):
    """Модель тега."""
    name = models.CharField(
        unique=True,
        max_length=settings.LENGTH_FIELDS_RECIPES,
        verbose_name='Название',
        help_text='Название тега',
        validators=[NameValidator()]
    )
    color = models.CharField(
        verbose_name='HEX-код цвета',
        max_length=settings.LENGTH_FIELDS_RECIPES,
        help_text='Цветовой HEX-код',
        unique=True,
        validators=[ColorValidator]
    )
    slug = models.SlugField(
        unique=True,
        max_length=settings.LENGTH_FIELDS_RECIPES,
        verbose_name='Slug',
        help_text='Slug тега'
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиентов."""
    name = models.CharField(
        max_length=settings.LENGTH_FIELDS_RECIPES,
        verbose_name='Название ингредиента',
        help_text='Название ингредиента',
        validators=[NameValidator()]
    )
    measurement_unit = models.CharField(
        default='г',
        max_length=settings.LENGTH_FIELDS_RECIPES,
        verbose_name='Единицы измерения',
        help_text='Единицы измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_name_measurement_unit')]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецепта."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
        help_text='Автор рецепта'
    )
    name = models.CharField(
        max_length=settings.LENGTH_FIELDS_RECIPES,
        verbose_name='Название',
        help_text='Название рецепта',
        validators=[NameValidator()]
    )
    image = models.ImageField(
        verbose_name='Фото',
        help_text='Фото блюда',
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Описание рецепта',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        help_text='Теги',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                1, 'Время приготовления не может быть меньше 1 минуты!'
            ),
            MaxValueValidator(
                1440, 'Время приготовления не может быть более 24 часов!'
            )
        ],
        default=1,
        verbose_name='Время приготовления',
        help_text='Время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания рецепта',
        help_text='Введите дату создания рецепта',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    """Модель списка покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Пользователь',
        help_text='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='Рецепт в списке покупок',
        help_text='Рецепт в списке покупок',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_shopping_cart',
            ),
        )


class IngredientAmount(models.Model):
    """Модель ингридиентов в рецепте."""
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='Ингредиент',
        help_text='Ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='Рецепт',
        help_text='Рецепт',
    )
    amount = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                1, 'Количество ингредиентов не может быть меньше 1!'
            ),
            MaxValueValidator(
                1000, 'Количество ингредиентов не может быть больше 1000!'
            )
        ],
        default=1,
        verbose_name='Количество',
        help_text='Количество',
    )

    class Meta:
        verbose_name = 'Кол-во ингредиентов'
        verbose_name_plural = 'Кол-во ингредиентов'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_in_recipe',
            )
        ]

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class FavoriteRecipe(models.Model):
    """Модель избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_list',
        verbose_name='Пользователь',
        help_text='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='Избранный рецепт',
        help_text='Избранный рецепт',
    )

    class Meta:
        verbose_name = 'Список избранного'
        verbose_name_plural = 'Списки избранного'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorites'
            )
        ]

    def __str__(self):
        return f'{self.user} {self.recipe}'
