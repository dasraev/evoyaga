from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name','markaz_tuman')
    list_display_links = ('login', 'first_name',)
    def save_model(self, request, obj, form, change):
        if change and 'password' not in form.changed_data:
            pass
        else:
            obj.set_password(obj.password)
        obj.save()


admin.site.register(CustomUser, CustomUserAdmin)
