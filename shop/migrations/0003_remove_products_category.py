# Generated by Django 2.2 on 2022-08-31 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220831_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]