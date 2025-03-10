from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')  # Admin panelda ko‘rinadigan ustunlar
    list_filter = ('is_staff', 'is_active')  # Filtrlar
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'photo')}),
        ('Courses', {'fields': ('courses',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')  # Qidirish maydoni
    ordering = ('email',)  # Tartanlash usuli

admin.site.register(User, CustomUserAdmin)
