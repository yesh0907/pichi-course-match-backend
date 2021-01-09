from django.contrib import admin

from pichicm_backend.authentication.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("id",)