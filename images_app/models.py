from django.conf import settings
from django.db import models
from PIL import Image, ImageOps
import os


def filename_image(filename, size):
    """Prepare image name.

    Returns:
        name
    """
    extension = filename.split(".")[-1]
    name = filename.split(".")[0]
    return "{}_{}px.{}".format(name, size, extension)


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


class ImageModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    thumbnail_200px = models.ImageField(blank=True)
    thumbnail_400px = models.ImageField(blank=True)

    def info(self):
        """fuction display neaded information.

        Returns:
            name image
        """
        return "{}".format(self.name)

    def __str__(self):
        """
        Returns:
            information contained in the `info()`
        """
        return self.info()

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def save(self):
        """When save generate thumbnail."""
        self.thumbnail_200px = thumbnail_image(self.image, size=(200, 200))
        self.thumbnail_400px = thumbnail_image(self.image, size=(400, 400))
        super(ImageModel, self).save()
