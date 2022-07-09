from django.conf import settings
from django.db import models
from PIL import Image, ImageOps
import os
from users.models import CustomUser


def filename_image(filename, *args):
    """Prepare image name. If don't send size image return only name.

    Args:
        filename = image name
        args = size

    Returns:
       name or name and size
    """
    filename = str(filename)
    name = filename.split(".")[0]
    if args == ():
        return "{}".format(name)
    else:
        extension = filename.split(".")[-1]
        return "{}_{}px.{}".format(name, args[0], extension)


def thumbnail_image(image_input, size=(200, 200)):
    """Create image with diffrent resolution."""

    if not image_input or image_input == "":
        return

    image = Image.open(image_input)
    image = ImageOps.exif_transpose(image)  # stop autorotate
    image.thumbnail(size, Image.ANTIALIAS)
    new_filename = filename_image(image_input.name, size[0])
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


class UserImage(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name="user_image",
    )
    original_image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        """When save"""
        self.name = filename_image(self.original_image)
        super(UserImage, self).save(force_update=force_update)

    def __str__(self):
        """
        Returns:
            name
        """
        return "{}".format(self.name)


class Thumbnail(models.Model):
    choose_image = models.ForeignKey(
        UserImage,
        on_delete=models.CASCADE,
        null=True,
        related_name="thumbnails",
    )
    thumbnail = models.ImageField(null=True, blank=True)
    size = models.IntegerField(blank=True, null=True, default=200)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        """When save"""
        self.thumbnail = thumbnail_image(
            self.choose_image.original_image, size=(self.size, self.size)
        )
        super(Thumbnail, self).save(force_update=force_update)

    def __str__(self):
        """
        Returns:
            name
        """
        return "{}".format(self.name)
