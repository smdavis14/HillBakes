# Generated by Django 3.2.4 on 2021-08-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill_bakes', '0009_auto_20210812_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='product',
            field=models.ManyToManyField(related_name='relation', to='hill_bakes.Product'),
        ),
    ]