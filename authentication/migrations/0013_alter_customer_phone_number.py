# Generated by Django 4.1.7 on 2023-03-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_customer_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone_Number",
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
