# from django.contrib.auth.models import UserImage
from images_app.models import UserImage
from django.db.models.signals import post_save
from django.dispatch import receiver

from images_app.models import Thumbnail


@receiver(post_save, sender=UserImage)
def create_thumbnails(sender, instance, created, **kwargs):
    tier = instance.user.tier
    print(tier)
    print("CREATED THUMBNAILS")
    thumbnails = []
    for size in tier.siezes:
        print(size)
        thumbnails.append(
            Thumbnail(
                user_image=instance, size=size, name=f"{instance.name}_{size}"
            )
        )
    Thumbnail.objects.bulk_create(thumbnails)
