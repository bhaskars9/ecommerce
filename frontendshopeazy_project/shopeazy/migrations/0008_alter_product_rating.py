# Generated by Django 4.1.2 on 2022-12-02 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopeazy', '0007_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=3.5),
        ),
    ]