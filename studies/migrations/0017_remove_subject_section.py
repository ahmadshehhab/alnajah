# Generated by Django 4.2.4 on 2023-08-06 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0016_alter_media_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='section',
        ),
    ]
