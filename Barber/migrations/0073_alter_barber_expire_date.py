# Generated by Django 4.2.1 on 2023-05-27 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0072_barber_expire_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barber",
            name="expire_date",
            field=models.DateField(default=datetime.date(2023, 6, 27)),
        ),
    ]