from django.contrib import admin
from .models import User
admin.site.register(User)
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'is_superuser', 'is_seller']