# Generated by Django 4.2.3 on 2023-07-31 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0005_remove_subject_media_media_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='media',
            new_name='Subject',
        ),
    ]
