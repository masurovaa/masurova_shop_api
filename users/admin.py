from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password", "is_staff", "is_active")}),
        ("Personal info", {"fields": ("username", "first_name", "last_name")}),
        ("Date information", {"fields": ("last_login",)}),
    )
    list_editable = ("is_active",)
