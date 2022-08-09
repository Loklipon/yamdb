from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'role')
    search_field = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    list_editable = ('email', 'first_name', 'last_name', 'bio', 'role')


admin.site.register(User, UserAdmin)
