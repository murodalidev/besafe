# Generated by Django 4.2.1 on 2023-05-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Verified user'),
        ),
    ]