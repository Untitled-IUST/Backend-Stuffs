# Generated by Django 4.1.7 on 2023-03-24 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_customer_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="phone_Number",
        ),
    ]
