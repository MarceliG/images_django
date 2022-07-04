from django.urls import path
from images_app.views import home

urlpatterns = [
    path("", home, name="home"),
]
