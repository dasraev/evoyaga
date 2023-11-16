from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name',)
    list_display_links = ('login', 'first_name',)


admin.site.register(CustomUser, CustomUserAdmin)
