# Generated by Django 4.0.5 on 2022-07-09 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0017_alter_thumbnail_choose_image_alter_thumbnail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='name',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
    ]
