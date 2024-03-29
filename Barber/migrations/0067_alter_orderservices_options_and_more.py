# Generated by Django 4.2 on 2023-05-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0066_alter_categoryservice_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="orderservices",
            options={"ordering": ["date", "time"]},
        ),
        migrations.AlterField(
            model_name="orderservices",
            name="status",
            field=models.CharField(
                choices=[
                    ("ordering", "ordering"),
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
