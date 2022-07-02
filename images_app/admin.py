from django.contrib import admin
from images_app.models import UserImage
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(UserImage)
class ImageModelAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "thumbnail_200px", "thumbnail_400px")
