# Generated by Django 4.2 on 2023-04-26 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0045_alter_barber_area_alter_barber_user_orderservices"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="orderservices",
            unique_together={("barber", "time")},
        ),
    ]
