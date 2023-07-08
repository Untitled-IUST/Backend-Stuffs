# Generated by Django 4.2 on 2023-05-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0062_orderservices_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderservices",
            name="status",
            field=models.CharField(
                choices=[
                    ("ordering", "ordering"),
                    ("ordered", "ordered"),
                    ("confirmed", "confirmed"),
                    ("paid", "paid"),
                ],
                default="ordering",
                max_length=9,
            ),
        ),
    ]