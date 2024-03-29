# Generated by Django 4.2.1 on 2023-05-29 11:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Barber", "0075_alter_barberdescription_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="barber",
            name="expire_date",
        ),
        migrations.AlterField(
            model_name="barberdescription",
            name="description",
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name="barberdescription",
            name="title",
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name="BarberPremium",
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
                ("expire_date", models.DateField(default=datetime.date(2023, 6, 29))),
                (
                    "month",
                    models.IntegerField(
                        choices=[
                            (1, "1-month"),
                            (3, "3-month"),
                            (6, "6-month"),
                            (12, "12-month"),
                        ]
                    ),
                ),
                (
                    "barber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Barber.barber"
                    ),
                ),
            ],
        ),
    ]
