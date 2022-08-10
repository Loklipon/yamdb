from django.contrib import admin

from .models import Title, Genre, Category


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
