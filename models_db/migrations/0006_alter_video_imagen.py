# Generated by Django 4.1.5 on 2023-01-20 18:25

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('models_db', '0005_video_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='imagen',
            field=models.ImageField(default=pathlib.PureWindowsPath('D:/Proyectos_Particulares/Ver_Videos/app/static/img/default_image_videos.jpg'), upload_to=pathlib.PureWindowsPath('D:/Proyectos_Particulares/Ver_Videos/app/static/img')),
        ),
    ]
