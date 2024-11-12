from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.enums import RoleType
from accounts.models import User, Department


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ('last_login', 'is_active', 'role_type')
    fieldsets = ()
    list_display = ['id', 'username', 'role_type', 'last_login', ]
    search_fields = ('email', 'mobile_number')
    ordering = ('email',)
    readonly_fields = ['email', ]

admin.site.register(Department)