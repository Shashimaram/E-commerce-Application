# Generated by Django 4.2.1 on 2023-08-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_colorvariant_sizevariant_products_size_variant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorvariant',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sizevariant',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
