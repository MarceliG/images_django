from django.contrib import admin
from images_app.models import UserImage, Thumbnail
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(UserImage)
class ImageModelAdmin(admin.ModelAdmin):
    readonly_fields = ("name",)


@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    readonly_fields = (
        "thumbnail",
    )
