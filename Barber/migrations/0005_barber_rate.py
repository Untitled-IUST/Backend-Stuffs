# Generated by Django 4.1.7 on 2023-04-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0004_alter_rate_barbershop"),
    ]

    operations = [
        migrations.AddField(
            model_name="barber",
            name="rate",
            field=models.FloatField(default=True),
        ),
    ]