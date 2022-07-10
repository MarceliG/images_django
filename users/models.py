from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Tier(models.Model):
    TIERS = (
        ("basic", "BASIC"),
        ("premium", "PREMIUM"),
        ("enterprise", "ENTERPRISE"),
    )
    SIZES = (
        ("small", 200),
        ("medium", 400),
    )
    tier = models.CharField(
        _("tier"),
        max_length=50,
        unique=True,
        choices=TIERS,
        default="BASIC",
        blank=False,
        null=False,
    )
    sizes = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        choices=SIZES,
        default=200,
    )

    def __str__(self):
        return str(self.tier)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=50, unique=True)
    tier = models.ForeignKey(
        Tier,
        on_delete=models.CASCADE,
        related_name="user_tier",
        null=True,
        blank=False,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)
