# Generated by Django 4.2 on 2023-05-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0023_alter_customer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="area",
            field=models.CharField(max_length=255, null=True),
        ),
    ]