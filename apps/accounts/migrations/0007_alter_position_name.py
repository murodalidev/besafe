# Generated by Django 4.2.1 on 2023-06-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_consultant_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(blank=True, max_length=221),
        ),
    ]
