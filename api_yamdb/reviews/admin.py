from django.contrib import admin

from .models import Title, Genre, Category, Review, Comment


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Review)
class TitleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Comment)
class TitleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
