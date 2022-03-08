from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'phone_number']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'username', 'phone_number', 'city', 'about')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'city', 'about')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


