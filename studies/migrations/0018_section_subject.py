# Generated by Django 4.2.4 on 2023-08-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0017_remove_subject_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ManyToManyField(blank=True, null=True, related_name='section', to='studies.subject'),
        ),
    ]
