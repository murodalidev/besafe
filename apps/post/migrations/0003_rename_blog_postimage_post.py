# Generated by Django 4.2.1 on 2023-06-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_postimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimage',
            old_name='blog',
            new_name='post',
        ),
    ]
