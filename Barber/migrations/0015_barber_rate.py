# Generated by Django 4.1.7 on 2023-04-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0014_remove_barber_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="barber",
            name="rate",
            field=models.FloatField(default=1),
        ),
    ]
