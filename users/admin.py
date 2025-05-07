from django.contrib import admin
from .models import WalletUser, Household, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class WalletUserAdmin(BaseUserAdmin):
    model = WalletUser
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Custom Info", {'fields': ('household', 'role')}),
    )


admin.site.register(WalletUser, WalletUserAdmin)
admin.site.register(Household)
admin.site.register(UserProfile)
