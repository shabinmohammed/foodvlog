# Generated by Django 2.2 on 2022-09-01 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220901_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categ',
            old_name='name',
            new_name='category',
        ),
    ]
