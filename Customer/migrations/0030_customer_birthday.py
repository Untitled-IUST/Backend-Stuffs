# Generated by Django 4.2.1 on 2023-07-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0029_alter_customer_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="birthday",
            field=models.DateField(null=True),
        ),
    ]
