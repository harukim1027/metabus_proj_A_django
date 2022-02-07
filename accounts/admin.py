from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'phone_num')
        }),
        ('Personal info', {
            'fields': ('gender', 'birthdate', 'position')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    # nickname: CHAR(20) NOT NULL
    # name: CHAR(30) NOT NULL
    # password: CHAR(20) NOT NULL
    # phone_number: CHAR(16) NOT NULL
    # email: CHAR(50) NOT NULL
    # region: CHAR(20) NOT NULL
    # password_quiz: CHAR(30) NOT NULL
    # password_quiz_answer: CHAR(30) NOT NULL
    # created_at: DATETIME NOT NULL
    # updated_at: DATETIME NOT NULL

    #
    list_display = ('nickname', 'name', 'is_active', 'phone_number','email')