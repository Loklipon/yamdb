from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name',
                    'last_name', 'bio', 'role', 'mail_confirmation_code')
    search_field = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    list_editable = ('email', 'first_name', 'last_name', 'bio', 'role', 'mail_confirmation_code')


admin.site.register(User, UserAdmin)
