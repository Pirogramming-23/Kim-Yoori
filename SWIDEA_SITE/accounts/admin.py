from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'bio', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('bio', 'profile_image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('추가 정보', {'fields': ('bio', 'profile_image')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)