# Generated by Django 4.0.5 on 2022-07-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0009_alter_thumbnail_thumbnail_alter_userimage_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='size',
            field=models.IntegerField(blank=True, default=200, null=True),
        ),
    ]
