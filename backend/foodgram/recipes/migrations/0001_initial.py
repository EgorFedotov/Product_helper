# Generated by Django 4.2.1 on 2023-06-10 17:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipes.validators
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Список избранного',
                'verbose_name_plural': 'Списки избранного',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название ингредиента', max_length=200, validators=[users.validators.NameValidator()], verbose_name='Название ингредиента')),
                ('measurement_unit', models.CharField(default='г', help_text='Единицы измерения', max_length=200, verbose_name='Единицы измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1, help_text='Количество', validators=[django.core.validators.MinValueValidator(1, 'Количество ингредиентов не может быть меньше 1!'), django.core.validators.MaxValueValidator(1000, 'Количество ингредиентов не может быть больше 1000!')], verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Кол-во ингредиентов',
                'verbose_name_plural': 'Кол-во ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название рецепта', max_length=200, validators=[users.validators.NameValidator()], verbose_name='Название')),
                ('image', models.ImageField(help_text='Фото блюда', upload_to='', verbose_name='Фото')),
                ('text', models.TextField(help_text='Описание рецепта', verbose_name='Описание')),
                ('cooking_time', models.PositiveSmallIntegerField(default=1, help_text='Время приготовления в минутах', validators=[django.core.validators.MinValueValidator(1, 'Время приготовления не может быть меньше 1 минуты!'), django.core.validators.MaxValueValidator(1440, 'Время приготовления не может быть более 24 часов!')], verbose_name='Время приготовления')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Введите дату создания рецепта', verbose_name='Дата создания рецепта')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название тега', max_length=200, unique=True, validators=[users.validators.NameValidator()], verbose_name='Название')),
                ('color', models.CharField(help_text='Цветовой HEX-код', max_length=7, unique=True, validators=[recipes.validators.ColorValidator()], verbose_name='HEX-код цвета')),
                ('slug', models.SlugField(help_text='Slug тега', max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(help_text='Рецепт в списке покупок', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='recipes.recipes', verbose_name='Рецепт в списке покупок')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Списки покупок',
            },
        ),
    ]
