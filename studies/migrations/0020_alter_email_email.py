# Generated by Django 4.2.4 on 2023-08-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0019_email_rename_settings_setting_section_ispublic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
