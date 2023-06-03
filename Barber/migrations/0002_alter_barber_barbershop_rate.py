# Generated by Django 4.1.7 on 2023-04-05 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="barber",
            name="BarberShop",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stars", models.FloatField()),
                (
                    "barbershop",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Barber.barber",
                        to_field="BarberShop",
                    ),
                ),
            ],
        ),
    ]