# Generated by Django 4.2 on 2023-05-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0027_alter_customer_credit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="credit",
            field=models.FloatField(default=0.0),
        ),
    ]
