# Generated by Django 4.1.7 on 2023-04-06 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0006_alter_barber_rate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="barber",
            name="rate",
        ),
    ]
