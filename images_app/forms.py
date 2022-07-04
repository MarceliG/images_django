from django import forms
from images_app.models import UserImage


class ImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ("original_image",)
        # fields = ("image",)
        read_only = ("custom_user",)
