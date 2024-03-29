# Generated by Django 4.2 on 2023-05-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0063_alter_orderservices_status"),
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
                    ("BarberCancelled", "BarberCancelled"),
                    ("CustomerCancelled", "CustomerCancelled"),
                    ("CustomerNotCome", "CustomerNotCome"),
                ],
                default="ordering",
                max_length=20,
            ),
        ),
    ]
