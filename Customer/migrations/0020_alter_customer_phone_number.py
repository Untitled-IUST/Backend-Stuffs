# Generated by Django 4.2 on 2023-04-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0019_alter_customer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone_Number",
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
    ]
