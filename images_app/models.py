from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

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
