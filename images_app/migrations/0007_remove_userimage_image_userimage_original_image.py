# Generated by Django 4.0.5 on 2022-07-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0006_remove_thumbnail_thumbnail_200px_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='image',
        ),
        migrations.AddField(
            model_name='userimage',
            name='original_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
