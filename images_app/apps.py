from django.apps import AppConfig


class ImagesAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "images_app"

    # def ready(self):
    #     import images_app.signals
