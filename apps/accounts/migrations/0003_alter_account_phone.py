# Generated by Django 4.2.1 on 2023-05-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(db_index=True, max_length=12, unique=True, verbose_name='Phone number'),
        ),
    ]
