# Generated by Django 4.1.5 on 2023-01-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_db', '0020_video_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='imagen',
        ),
    ]
