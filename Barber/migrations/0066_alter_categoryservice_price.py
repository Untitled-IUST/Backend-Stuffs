# Generated by Django 4.2 on 2023-05-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0065_alter_categoryservice_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryservice",
            name="price",
            field=models.FloatField(default=0),
        ),
    ]
