# Generated by Django 2.2 on 2022-09-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='data_added',
            field=models.DateTimeField(),
        ),
    ]
