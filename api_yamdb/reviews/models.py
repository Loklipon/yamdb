from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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
