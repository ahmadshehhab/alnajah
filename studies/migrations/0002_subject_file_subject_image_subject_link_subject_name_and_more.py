# Generated by Django 4.2.3 on 2023-07-30 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='file',
            field=models.FileField(null=True, upload_to='videos_uploaded'),
        ),
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subject',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default='no name', max_length=255),
        ),
        migrations.AddField(
            model_name='subject',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]