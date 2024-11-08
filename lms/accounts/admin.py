from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.enums import RoleType
from accounts.models import User, Role, Department


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ('last_login', 'is_active', 'role')
    fieldsets = ()
    list_display = ['id', 'username', 'role', 'last_login', ]
    search_fields = ('email', 'mobile_number')
    ordering = ('email',)
    readonly_fields = ['email', ]

admin.site.register(Role)
admin.site.register(Department)