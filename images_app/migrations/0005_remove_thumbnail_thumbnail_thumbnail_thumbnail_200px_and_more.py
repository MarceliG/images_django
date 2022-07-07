# Generated by Django 4.0.5 on 2022-07-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0004_thumbnail_remove_userimage_thumbnail_200px_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail_200px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail_400px',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
