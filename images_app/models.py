from django.conf import settings
from django.db import models
from PIL import Image, ImageOps
import os

<<<<<<< HEAD
from users.models import CustomUser


class UserImage(models.Model):
=======

# class Client(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="client",
#     )
#     grup = models.ForeignKey(Group, on_delete=models.CASCADE)

#     def __str__(self):
#         """
#         Returns:
#             information
#         """
#         return "{}".format(self.user)


class ImageModel(models.Model):
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6
    # client = models.ForeignKey(
    #     Client,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     related_name="imagemodel",
    # )
<<<<<<< HEAD
    custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name="user_image",
    )
=======
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(null=True, blank=True)
    thumbnail_200px = models.ImageField(blank=True)
    thumbnail_400px = models.ImageField(blank=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        """When save"""
        self.name = filename_image(self.image)
        self.thumbnail_200px = thumbnail_image(self.image, size=(200, 200))
        self.thumbnail_400px = thumbnail_image(self.image, size=(400, 400))
        super(UserImage, self).save(force_update=force_update)

    def __str__(self):
        """
        Returns:
            name
        """
        return "{}".format(self.name)


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
