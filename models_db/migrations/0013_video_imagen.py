# Generated by Django 4.1.5 on 2023-01-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_db', '0012_remove_video_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='imagen',
            field=models.ImageField(default='static/img/default_image_videos.jpg', upload_to='static/img'),
        ),
    ]
