from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')


class Recipe(models.Model):
    EASY = 'E'
    MEDIUM = 'M'
    HARD = 'H'
    DIFFICULTY_CHOICES = {
        EASY: 'Easy',
        MEDIUM: 'Medium',
        HARD: 'Hard'
    }

    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY_CHOICES,
        default=EASY,
        verbose_name='Сложность'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание')
    recipe_text = models.TextField(verbose_name='Рецепт')
