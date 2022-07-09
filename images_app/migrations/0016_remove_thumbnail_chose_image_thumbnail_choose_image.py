# Generated by Django 4.0.5 on 2022-07-09 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0015_remove_thumbnail_custom_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='chose_image',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='choose_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_image', to='images_app.userimage'),
        ),
    ]