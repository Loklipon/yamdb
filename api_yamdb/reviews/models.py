from django.db import models
from reviews.validators import year_validator


class Category(models.Model):
    """
    Класс модели `Категория`.

    Поля:
        name: TextField
        slug: SlugField
    Реализована функции str.
    """
    name = models.TextField(verbose_name="Название категории", max_length=256)
    slug = models.SlugField(
        verbose_name="Уникальное слаг категории", max_length=50, unique=True)

    def __str__(self):
        """Перевод поля к str, используюя name."""
        return self.name


class Genre(models.Model):
    """
    Класс модели `Жанр`.

    Поля:
        name: TextField
        slug: SlugField
    Реализована функции str.
    """
    name = models.TextField(verbose_name="Название жанра", max_length=256)
    slug = models.SlugField(
        verbose_name="Уникальный слаг жанра", max_length=50, unique=True)

    def __str__(self):
        """Перевод поля к str, используюя name."""
        return self.name


class Title(models.Model):
    """
    Класс модели произведений.

    Поля:
        name: TextField
        year: DateField
        description: TextField (non required)
        genre: ForeignKey to Genres
        category: ForignKey to Categories
    """
    name = models.TextField(
        verbose_name="Название произведения", max_length=256
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска произведения",
        validators=[year_validator],
    )
    description = models.TextField(
        verbose_name="Описание произведения",
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Жанры произведения",
        through='GenreTitle',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория произведения"
    )

    def __str__(self):
        """Перевод поля к str, используюя name."""
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.Case)

    def __str__(self):
        return f'{self.genre} {self.title}'
