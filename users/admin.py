from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ("username", "date_joined")
    ordering = ("-date_joined",)
    list_display = ("username", "date_joined", "is_active", "is_staff")
    list_filter = ("date_joined", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {"fields": ("username",)},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(CustomUser, UserAdminConfig)
