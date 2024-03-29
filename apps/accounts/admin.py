from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account, Position, Consultant
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('id', 'phone', 'first_name', 'last_name', 'birth_date', 'is_superuser', 'is_staff',
                    'is_active', 'is_verified', 'modified_date', 'created_date')
    readonly_fields = ('modified_date', 'created_date')
    list_filter = ('created_date', 'is_superuser', 'is_staff', 'is_active', 'is_verified')
    date_hierarchy = 'created_date'
    ordering = ()
    fieldsets = (
        (None, {'fields': ('phone', 'password', 'first_name', 'last_name', 'birth_date', 'avatar')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_verified',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('modified_date', 'created_date')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('phone', 'password1', 'password2'), }),
    )
    search_fields = ('phone', 'first_name', 'last_name')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'is_verified')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    list_filter = ('is_verified', 'position')


admin.site.register(Account, AccountAdmin)
