# Generated by Django 2.2 on 2022-09-01 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_products_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={},
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.Categ'),
            preserve_default=False,
        ),
    ]
