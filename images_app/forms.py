from asyncore import read
from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ("image",)
        read_only = ("client",)
