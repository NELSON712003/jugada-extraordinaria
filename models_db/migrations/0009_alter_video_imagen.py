# Generated by Django 4.1.5 on 2023-01-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_db', '0008_video_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='imagen',
            field=models.ImageField(default='app/static/img/default_image_videos.jpg', upload_to='app/static/img'),
        ),
    ]
