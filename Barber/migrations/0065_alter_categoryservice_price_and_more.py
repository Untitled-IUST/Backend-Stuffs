# Generated by Django 4.2 on 2023-05-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0064_alter_orderservices_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryservice",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
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
                    ("Done", "Done"),
                ],
                default="ordering",
                max_length=20,
            ),
        ),
    ]
