from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from reviews.validators import year_validator
from users.models import User


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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        related_name='Reviews',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        'Отзыв',
        blank=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор ревью',
        related_name='Reviews',
        on_delete=models.CASCADE
    )
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        related_name='Comments',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        'Комментарий'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        related_name='Comments',
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
