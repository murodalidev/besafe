# Generated by Django 4.2.1 on 2023-05-15 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogimage',
            old_name='is_cover',
            new_name='is_main',
        ),
    ]
