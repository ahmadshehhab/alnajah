# Generated by Django 4.2.4 on 2023-08-06 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0015_alter_media_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='media', to='studies.section'),
        ),
    ]